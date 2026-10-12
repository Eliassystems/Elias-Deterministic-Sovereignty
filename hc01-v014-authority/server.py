"""HC-01 v0.14 synthetic external authority, test-only, read-only.

No patient information, no mutation endpoints, no production execution authority.
Signing seed is provided through Render environment (never stored in Git).
"""
import base64
import hashlib
import json
import os
import re
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

SCHEMA = "HC01-OFFHOST-AUTHORITY-0.14"
SIGNER_B64 = os.environ.get("HC01_SIGNER_SEED_B64", "")
if not SIGNER_B64:
    raise SystemExit("HC01_SIGNER_SEED_B64 not configured")
try:
    SEED = base64.b64decode(SIGNER_B64, validate=True)
    if len(SEED) != 32:
        raise ValueError("Ed25519 seed must be 32 bytes")
    SIGNER = Ed25519PrivateKey.from_private_bytes(SEED)
except Exception as exc:
    raise SystemExit("HC01 signer configuration invalid") from exc
PUBLIC_KEY = SIGNER.public_key().public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw,
)
KEY_FINGERPRINT = hashlib.sha256(PUBLIC_KEY).hexdigest().upper()

class Handler(BaseHTTPRequestHandler):
    server_version = "HC01-SyntheticAuthority"
    sys_version = ""

    def _reply(self, status, data):
        out = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def do_GET(self):
        path = urlparse(self.path)
        if path.path == "/healthz":
            return self._reply(200, {"status":"ready", "synthetic":True})
        if path.path != "/v1/authority":
            return self._reply(404, {"error":"NOT_FOUND"})
        q = parse_qs(path.query, keep_blank_values=True)
        if set(q) != {"nonce"} or len(q["nonce"]) != 1:
            return self._reply(400, {"error":"NONCE_REQUIRED"})
        nonce = q["nonce"][0]
        if not re.fullmatch(r"[0-9a-f]{32}", nonce):
            return self._reply(400, {"error":"NONCE_INVALID"})
        now = int(time.time())
        payload = {
            "schema": SCHEMA,
            "release_id": "HC01-SYNTHETIC-ONLY",
            "generation": 2,
            "authority": "REVOKED",
            "nonce": nonce,
            "issued_at": now,
            "expires_at": now + 30,
            "scope": "SYNTHETIC_TEST_NO_PATIENT_DATA",
        }
        message = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        signature = base64.b64encode(SIGNER.sign(message)).decode()
        self._reply(200, {"payload":payload,"signature_ed25519_b64":signature,"public_key_sha256":KEY_FINGERPRINT})

    def do_POST(self):
        self._reply(405, {"error":"READ_ONLY_AUTHORITY"})

    def log_message(self, fmt, *args):
        # Avoid logging nonce-bearing request URLs or user input.
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
