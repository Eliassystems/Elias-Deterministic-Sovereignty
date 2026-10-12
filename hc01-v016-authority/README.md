# HC-01 v0.16 — synthetic authority lifecycle test

**TEST ONLY**. No patient data, clinical permission, actual healthcare release, or production consequence.

- Creates one-time 15-minute test sessions, with bearer capabilities returned only when created.
- Returns Ed25519-signed synthetic ACTIVE and REVOKED decisions scoped to the test session, with client nonce and 30-second TTL.
- Revocation is irreversible within a session; on service restart, test sessions disappear and calls refuse rather than silently authorize.
- Signing seed must be set as a Render environment secret `HC01_V016_SIGNER_SEED_B64`; it must never be committed to Git.
- Public Render HTTPS ingress does **not** establish independent administration, production non-bypassability, or protection against the host operator's alternative execution paths.
- No auto-deploy, and existing EIE and HC01 v0.14 services must remain unchanged.
