"""HC01 synthetic v0.16 ACTIVE/REVOKED authority. TEST ONLY. No patient data.

Sessions are volatile, expire after 15 minutes, and are lost on restart.
This is NOT independently administered healthcare authority.
"""
import base64, hashlib, json, os, re, secrets, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

SCHEMA = 'HC01-OFFHOST-LIFECYCLE-0.16'
SCOPE = 'SYNTHETIC_TEST_NO_PATIENT_DATA'
try:
    seed = base64.b64decode(os.environ['HC01_V016_SIGNER_SEED_B64'], validate=True)
    if len(seed) != 32: raise ValueError('incorrect seed length')
    SIGNER = Ed25519PrivateKey.from_private_bytes(seed)
except Exception as exc:
    raise SystemExit('Synthetic signer configuration invalid') from exc
pub = SIGNER.public_key().public_bytes(serialization.Encoding.Raw,serialization.PublicFormat.Raw)
PIN = hashlib.sha256(pub).hexdigest().upper()
SESSIONS = {}
LOCK = threading.Lock()
TTL = 900

class Handler(BaseHTTPRequestHandler):
    server_version = 'HC01-TestOnly-0.16'
    sys_version = ''

    def reply(self, status, body):
        data = json.dumps(body, sort_keys=True, separators=(',', ':')).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-store, max-age=0')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass

    def session(self, sid):
        if not re.fullmatch('[0-9a-f]{24}', sid): return None
        auth = self.headers.get('Authorization','')
        if not auth.startswith('Bearer '): return None
        supplied = hashlib.sha256(auth[7:].encode()).digest()
        with LOCK:
            s = SESSIONS.get(sid)
            if not s or s['expires'] < time.time(): return None
            if not secrets.compare_digest(supplied, s['token_hash']): return None
            return dict(s)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == '/healthz':
            return self.reply(200,{'ready':True,'synthetic':True,'version':'0.16','public_key_sha256':PIN})
        if url.path == '/v1/public-key':
            return self.reply(200,{'public_key_ed25519_b64':base64.b64encode(pub).decode('ascii'),'public_key_sha256':PIN})
        if url.path != '/v1/authority':
            return self.reply(404,{'error':'NOT_FOUND'})
        q = parse_qs(url.query,keep_blank_values=True)
        if set(q) != {'nonce','session_id'} or len(q['nonce']) != 1 or len(q['session_id']) != 1:
            return self.reply(400,{'error':'INPUT_INVALID'})
        nonce, sid = q['nonce'][0], q['session_id'][0]
        if not re.fullmatch('[0-9a-f]{32}',nonce):
            return self.reply(400,{'error':'NONCE_INVALID'})
        session = self.session(sid)
        if session is None:
            return self.reply(401,{'error':'SESSION_UNAUTHORIZED_OR_EXPIRED'})
        now = int(time.time())
        payload = {'schema':SCHEMA,'scope':SCOPE,'release_id':'HC01-SYNTHETIC-ONLY',
                   'session_id':sid,'nonce':nonce,'authority':session['authority'],
                   'generation':session['generation'],'issued_at':now,'expires_at':now+30}
        canon = json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
        signature = base64.b64encode(SIGNER.sign(canon)).decode('ascii')
        self.reply(200,{'payload':payload,'signature_ed25519_b64':signature,'public_key_sha256':PIN})

    def do_POST(self):
        path = urlparse(self.path).path
        size = self.headers.get('Content-Length','')
        if not size.isdigit() or int(size) > 256:
            return self.reply(400,{'error':'INVALID_BODY_SIZE'})
        try: data = json.loads(self.rfile.read(int(size)))
        except Exception: return self.reply(400,{'error':'INVALID_JSON'})
        if path == '/v1/sessions':
            if data != {'purpose':'HC01_V016_SYNTHETIC_LIFECYCLE'}:
                return self.reply(400,{'error':'INVALID_PURPOSE'})
            sid, token = secrets.token_hex(12), secrets.token_urlsafe(32)
            with LOCK:
                for key in list(SESSIONS):
                    if SESSIONS[key]['expires'] < time.time(): del SESSIONS[key]
                if len(SESSIONS) >= 64:
                    return self.reply(429,{'error':'SESSION_CAPACITY_REACHED'})
                SESSIONS[sid] = {'token_hash':hashlib.sha256(token.encode()).digest(),
                                 'authority':'ACTIVE','generation':1,'expires':time.time()+TTL}
            return self.reply(201,{'session_id':sid,'session_token':token,
                                    'expires_in_seconds':TTL,'scope':SCOPE,'authority':'ACTIVE'})
        m = re.fullmatch(r'/v1/sessions/([0-9a-f]{24})/(revoke|end)',path)
        if not m or data != {}: return self.reply(404,{'error':'NOT_FOUND'})
        sid, action = m.groups()
        if self.session(sid) is None:
            return self.reply(401,{'error':'SESSION_UNAUTHORIZED_OR_EXPIRED'})
        with LOCK:
            s = SESSIONS.get(sid)
            if not s: return self.reply(404,{'error':'SESSION_NOT_FOUND'})
            if action == 'end':
                del SESSIONS[sid]
                return self.reply(200,{'status':'ENDED'})
            if s['authority'] != 'REVOKED':
                s['authority']='REVOKED'
                s['generation'] += 1
            return self.reply(200,{'status':'REVOKED','generation':s['generation']})

if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0',int(os.getenv('PORT','10000'))),Handler).serve_forever()
