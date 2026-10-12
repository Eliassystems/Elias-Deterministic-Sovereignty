# HC-01 v0.14 synthetic off-host authority

Test-only read-only signed REVOKED freshness endpoint. No patient records or operational healthcare authority.

GET `/healthz` and `/v1/authority?nonce=<32 lowercase hex>`.

Requires a secret environment value `HC01_SIGNER_SEED_B64` containing 32 random bytes encoded as base64; never put this value into source control.

This demonstrates off-host signature verification but **does not establish** independent administrative control, persistent production state, production non-bypassability, or protected alternate execution paths. HTTP TLS is expected at Render ingress; client must verify HTTPS certificate and pin the signer public key.
