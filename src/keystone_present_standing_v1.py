import datetime
import hashlib
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List


UTC = datetime.timezone.utc


def utc_now() -> datetime.datetime:
    return datetime.datetime.now(UTC)


def canonical_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_json(data: Any) -> str:
    return sha256_text(canonical_json(data))


class ConstitutionalDeficit(Exception):
    """Raised when a consequential execution intent lacks present standing."""
    pass


@dataclass(frozen=True)
class AuthorityScope:
    operator: str
    allowed_actions: Tuple[str, ...]
    allowed_resources: Tuple[str, ...]
    max_consequence_tier: int


@dataclass
class AuthorityEpoch:
    epoch_id: str
    scope: AuthorityScope
    issued_at: str
    expires_at: str
    revoked: bool = False
    revocation_reason: Optional[str] = None
    revocation_time: Optional[str] = None


class GlassBoxLedger:
    """
    Append-only in-process witness chain.

    Each event commits to the previous event hash. This demonstrates
    tamper-evident ordering within the generated evidence artifact.

    It does NOT claim distributed immutability, external notarisation,
    non-repudiation, or protection against deletion of the entire file.
    """

    GENESIS_HASH = "0" * 64

    def __init__(self):
        self.ledger_chain: List[Dict[str, Any]] = []

    def log_event(
        self,
        event_type: str,
        intent_id: str,
        human_signatory: str,
        status: str,
        evidence: Dict[str, Any],
    ) -> Dict[str, Any]:
        previous_hash = (
            self.ledger_chain[-1]["entry_hash"]
            if self.ledger_chain
            else self.GENESIS_HASH
        )

        entry_body = {
            "sequence": len(self.ledger_chain) + 1,
            "timestamp": utc_now().isoformat(),
            "event_type": event_type,
            "intent_id": intent_id,
            "human_author": human_signatory,
            "execution_status": status,
            "evidence": evidence,
            "previous_hash": previous_hash,
        }

        entry_hash = sha256_json(entry_body)
        entry = {**entry_body, "entry_hash": entry_hash}
        self.ledger_chain.append(entry)

        print(
            f"LOGGED: [{status}] {event_type} "
            f"- seq={entry['sequence']} hash={entry_hash[:16]}..."
        )
        return entry

    def verify_chain(self) -> Tuple[bool, str]:
        previous_hash = self.GENESIS_HASH

        for expected_sequence, entry in enumerate(self.ledger_chain, start=1):
            if entry["sequence"] != expected_sequence:
                return False, f"Sequence mismatch at ledger entry {expected_sequence}"

            if entry["previous_hash"] != previous_hash:
                return False, f"Previous-hash mismatch at ledger entry {expected_sequence}"

            body = {k: v for k, v in entry.items() if k != "entry_hash"}
            recomputed = sha256_json(body)

            if recomputed != entry["entry_hash"]:
                return False, f"Entry-hash mismatch at ledger entry {expected_sequence}"

            previous_hash = entry["entry_hash"]

        return True, "Ledger chain verified"


class LoveOSConstitutionalCore:
    """
    Bounded constitutional baseline for this demonstrator.

    The integrity check proves only that the runtime axioms still match
    the frozen baseline instantiated by this program.
    """

    FROZEN_AXIOMS = {
        "AXIOM_01_CAPABILITY_IS_NOT_AUTHORITY": True,
        "AXIOM_02_PRE_EXECUTION_RESTRAINT_REQUIRED": True,
        "AXIOM_03_HUMAN_AUTHORITY_REMAINS_REVOCABLE": True,
        "AXIOM_04_PRESENT_STANDING_REQUIRED_AT_EXECUTION": True,
        "AXIOM_05_EXECUTION_MUST_BE_SCOPE_BOUND": True,
        "AXIOM_06_WITNESS_RECORD_REQUIRED": True,
    }

    def __init__(self):
        self._axioms = dict(self.FROZEN_AXIOMS)
        self._baseline_hash = sha256_json(self.FROZEN_AXIOMS)

    @property
    def baseline_hash(self) -> str:
        return self._baseline_hash

    def verify_integrity(self) -> Tuple[bool, str]:
        current_hash = sha256_json(self._axioms)
        if current_hash != self._baseline_hash:
            return False, "Constitutional baseline hash mismatch"
        if self._axioms != self.FROZEN_AXIOMS:
            return False, "Constitutional baseline content mismatch"
        return True, "Constitutional baseline verified"


class EliasKeystoneEngine:
    """
    Bounded Keystone-style pre-execution governance demonstrator.

    Demonstrated property:
      Historical authority alone is insufficient for present execution
      standing after a material authority-state change.

    This engine does not prove external identity, legal authority,
    cryptographic key ownership, or real-world policy truth.
    """

    def __init__(
        self,
        constitution: LoveOSConstitutionalCore,
        ledger: GlassBoxLedger,
    ):
        self.constitution = constitution
        self.ledger = ledger
        self.active_epochs: Dict[str, AuthorityEpoch] = {}

    def issue_authority_epoch(
        self,
        scope: AuthorityScope,
        lifespan_seconds: int,
    ) -> str:
        issued_at = utc_now()
        expires_at = issued_at + datetime.timedelta(seconds=lifespan_seconds)

        seed = {
            "operator": scope.operator,
            "allowed_actions": scope.allowed_actions,
            "allowed_resources": scope.allowed_resources,
            "max_consequence_tier": scope.max_consequence_tier,
            "issued_at": issued_at.isoformat(),
            "expires_at": expires_at.isoformat(),
        }
        epoch_id = sha256_json(seed)

        self.active_epochs[epoch_id] = AuthorityEpoch(
            epoch_id=epoch_id,
            scope=scope,
            issued_at=issued_at.isoformat(),
            expires_at=expires_at.isoformat(),
        )

        self.ledger.log_event(
            "AUTHORITY_EPOCH_ISSUED",
            intent_id="NONE",
            human_signatory=scope.operator,
            status="ESTABLISHED",
            evidence={
                "epoch_id": epoch_id,
                "scope": asdict(scope),
                "issued_at": issued_at.isoformat(),
                "expires_at": expires_at.isoformat(),
            },
        )
        return epoch_id

    def revoke_authority_epoch(self, epoch_id: str, reason: str) -> bool:
        epoch = self.active_epochs.get(epoch_id)
        if not epoch:
            return False

        epoch.revoked = True
        epoch.revocation_reason = reason
        epoch.revocation_time = utc_now().isoformat()

        self.ledger.log_event(
            "AUTHORITY_EPOCH_REVOKED",
            intent_id="NONE",
            human_signatory=epoch.scope.operator,
            status="REVOKED",
            evidence={
                "epoch_id": epoch_id,
                "reason": reason,
                "revocation_time": epoch.revocation_time,
            },
        )
        return True

    @staticmethod
    def derive_intent_id(payload: Dict[str, Any]) -> str:
        return sha256_json(payload)[:16]

    def _evaluate_payload_rules(
        self,
        payload: Dict[str, Any],
        epoch: AuthorityEpoch,
    ) -> Tuple[bool, str, Dict[str, Any]]:
        required_fields = (
            "target_resource",
            "action",
            "consequence_tier",
            "deterministic_rule_id",
        )
        missing = [field for field in required_fields if field not in payload]
        if missing:
            return False, "PAYLOAD_INCOMPLETE", {"missing_fields": missing}

        target = payload["target_resource"]
        action = payload["action"]
        consequence_tier = payload["consequence_tier"]
        rule_id = payload["deterministic_rule_id"]

        if not isinstance(consequence_tier, int) or consequence_tier < 0:
            return False, "INVALID_CONSEQUENCE_TIER", {
                "consequence_tier": consequence_tier
            }

        if action not in epoch.scope.allowed_actions:
            return False, "ACTION_OUT_OF_SCOPE", {
                "action": action,
                "allowed_actions": list(epoch.scope.allowed_actions),
            }

        if target not in epoch.scope.allowed_resources:
            return False, "RESOURCE_OUT_OF_SCOPE", {
                "target_resource": target,
                "allowed_resources": list(epoch.scope.allowed_resources),
            }

        if consequence_tier > epoch.scope.max_consequence_tier:
            return False, "CONSEQUENCE_LIMIT_EXCEEDED", {
                "consequence_tier": consequence_tier,
                "max_consequence_tier": epoch.scope.max_consequence_tier,
            }

        if not isinstance(rule_id, str) or not rule_id.strip():
            return False, "DETERMINISTIC_RULE_ABSENT", {
                "deterministic_rule_id": rule_id
            }

        return True, "PAYLOAD_RULES_SATISFIED", {
            "action": action,
            "target_resource": target,
            "consequence_tier": consequence_tier,
            "deterministic_rule_id": rule_id,
        }

    def evaluate_pre_execution_seam(
        self,
        payload: Dict[str, Any],
        epoch_id: str,
    ) -> Tuple[bool, str, Dict[str, Any]]:
        intent_id = self.derive_intent_id(payload)

        constitution_ok, constitution_reason = self.constitution.verify_integrity()
        if not constitution_ok:
            evidence = {
                "reason": constitution_reason,
                "constitution_hash": self.constitution.baseline_hash,
            }
            self.ledger.log_event(
                "SYSTEM_CONSTITUTIONAL_DEFICIT",
                intent_id,
                "SYSTEM",
                "REFUSED",
                evidence,
            )
            return False, "CONSTITUTIONAL_INTEGRITY_FAILURE", evidence

        epoch = self.active_epochs.get(epoch_id)
        if epoch is None:
            evidence = {"reason": "Authority epoch absent"}
            self.ledger.log_event(
                "AUTHORITY_ABSENT",
                intent_id,
                "UNKNOWN",
                "REFUSED",
                evidence,
            )
            return False, "AUTHORITY_EPOCH_ABSENT", evidence

        now = utc_now()
        expires_at = datetime.datetime.fromisoformat(epoch.expires_at)

        if epoch.revoked:
            evidence = {
                "epoch_id": epoch_id,
                "revocation_reason": epoch.revocation_reason,
                "revocation_time": epoch.revocation_time,
            }
            self.ledger.log_event(
                "AUTHORITY_STATE_CHANGED",
                intent_id,
                epoch.scope.operator,
                "REFUSED",
                evidence,
            )
            return False, "AUTHORITY_EPOCH_REVOKED", evidence

        if now >= expires_at:
            evidence = {
                "epoch_id": epoch_id,
                "expires_at": epoch.expires_at,
                "evaluated_at": now.isoformat(),
            }
            self.ledger.log_event(
                "AUTHORITY_EXPIRED",
                intent_id,
                epoch.scope.operator,
                "REFUSED",
                evidence,
            )
            return False, "AUTHORITY_EPOCH_EXPIRED", evidence

        payload_ok, payload_reason, payload_evidence = self._evaluate_payload_rules(
            payload,
            epoch,
        )

        if not payload_ok:
            evidence = {
                "epoch_id": epoch_id,
                "scope": asdict(epoch.scope),
                **payload_evidence,
            }
            self.ledger.log_event(
                "EXECUTION_SCOPE_DEFICIT",
                intent_id,
                epoch.scope.operator,
                "REFUSED",
                evidence,
            )
            return False, payload_reason, evidence

        execution_binding = sha256_json({
            "epoch_id": epoch_id,
            "intent_id": intent_id,
            "operator": epoch.scope.operator,
            "action": payload["action"],
            "target_resource": payload["target_resource"],
            "consequence_tier": payload["consequence_tier"],
            "deterministic_rule_id": payload["deterministic_rule_id"],
        })

        evidence = {
            "epoch_id": epoch_id,
            "intent_id": intent_id,
            "execution_binding": execution_binding,
            "operator": epoch.scope.operator,
            "present_standing": "VERIFIED_WITHIN_DEMONSTRATOR",
            "scope_check": "PASS",
            "rule_check": "PASS",
            "constitution_hash": self.constitution.baseline_hash,
        }

        self.ledger.log_event(
            "PRE_EXECUTION_PERMITTED",
            intent_id,
            epoch.scope.operator,
            "PERMITTED",
            evidence,
        )
        return True, "PRESENT_STANDING_ESTABLISHED", evidence


def run_validation() -> Dict[str, Any]:
    print("=" * 78)
    print("ELIAS KEYSTONE - PRESENT-STANDING PRE-EXECUTION DEMONSTRATOR")
    print("=" * 78)
    print()

    ledger = GlassBoxLedger()
    constitution = LoveOSConstitutionalCore()
    keystone = EliasKeystoneEngine(constitution, ledger)

    scope = AuthorityScope(
        operator="Gary Williams",
        allowed_actions=(
            "REBUILD_GOVERNANCE_KERNEL_FROM_FIRST_PRINCIPLES",
            "MODIFY_SECURITY_FIREWALL_RULES",
        ),
        allowed_resources=(
            "Enterprise_Core_Data_Infrastructure",
        ),
        max_consequence_tier=3,
    )

    epoch_id = keystone.issue_authority_epoch(scope, lifespan_seconds=300)
    print(f"\nAuthority epoch: {epoch_id[:16]}...\n")

    positive_payload = {
        "target_resource": "Enterprise_Core_Data_Infrastructure",
        "action": "REBUILD_GOVERNANCE_KERNEL_FROM_FIRST_PRINCIPLES",
        "consequence_tier": 2,
        "deterministic_rule_id": "EKS-RULE-EXEC-001",
        "model_confidence": 0.84,
    }

    print("--- PC: Present standing survives ---")
    pc_allowed, pc_reason, pc_evidence = keystone.evaluate_pre_execution_seam(
        positive_payload,
        epoch_id,
    )
    print(f"PC RESULT: allowed={pc_allowed} reason={pc_reason}\n")

    out_of_scope_payload = {
        "target_resource": "Enterprise_Core_Data_Infrastructure",
        "action": "EXTRACT_WHITE_PAPERS",
        "consequence_tier": 2,
        "deterministic_rule_id": "EKS-RULE-EXEC-001",
        "model_confidence": 1.0,
    }

    print("--- NEG-1: Action outside delegated scope ---")
    neg1_allowed, neg1_reason, neg1_evidence = keystone.evaluate_pre_execution_seam(
        out_of_scope_payload,
        epoch_id,
    )
    print(f"NEG-1 RESULT: allowed={neg1_allowed} reason={neg1_reason}\n")

    keystone.revoke_authority_epoch(
        epoch_id,
        reason="Human sovereign authority withdrawn before next consequential execution",
    )

    print("--- NEG-2: Historical authority after material revocation ---")
    neg2_allowed, neg2_reason, neg2_evidence = keystone.evaluate_pre_execution_seam(
        positive_payload,
        epoch_id,
    )
    print(f"NEG-2 RESULT: allowed={neg2_allowed} reason={neg2_reason}\n")

    ledger_ok, ledger_reason = ledger.verify_chain()

    falsifier_triggered = (
        (not pc_allowed)
        or neg1_allowed
        or neg2_allowed
        or (not ledger_ok)
    )

    verdict = (
        "PASS_WITHIN_FROZEN_BOUNDED_SCOPE"
        if not falsifier_triggered
        else "FAIL_FALSIFIER_TRIGGERED"
    )

    result = {
        "document_id": "EKS-PSV-001",
        "title": "Keystone Present-Standing Pre-Execution Validation",
        "proposition": (
            "Historical authority alone does not establish present execution standing "
            "after a material authority-state change. Consequential execution requires "
            "current authority scoped and bound to the specific intent at the execution seam."
        ),
        "falsifier": {
            "description": (
                "Triggered if the valid in-scope PC is refused, if an out-of-scope action "
                "is permitted, if the same historically valid epoch is permitted after "
                "revocation, or if the witness hash chain fails verification."
            ),
            "triggered": falsifier_triggered,
        },
        "verdict": verdict,
        "cases": {
            "PC_PRESENT_STANDING_SURVIVES": {
                "allowed": pc_allowed,
                "reason": pc_reason,
                "evidence": pc_evidence,
            },
            "NEG_SCOPE_DEFICIT": {
                "allowed": neg1_allowed,
                "reason": neg1_reason,
                "evidence": neg1_evidence,
            },
            "NEG_AUTHORITY_REVOKED": {
                "allowed": neg2_allowed,
                "reason": neg2_reason,
                "evidence": neg2_evidence,
            },
        },
        "constitution": {
            "baseline_hash": constitution.baseline_hash,
            "axioms": constitution.FROZEN_AXIOMS,
        },
        "ledger_verification": {
            "verified": ledger_ok,
            "reason": ledger_reason,
            "entry_count": len(ledger.ledger_chain),
        },
        "ledger": ledger.ledger_chain,
        "scope_limits": [
            "No external identity verification is performed.",
            "No legal authority is independently established.",
            "No real infrastructure action is executed.",
            "No distributed immutability or external notarisation is claimed.",
            "A deterministic rule identifier is required, but the truth of an external policy is not independently proven.",
            "Model confidence is deliberately non-authoritative.",
        ],
        "generated_at": utc_now().isoformat(),
    }

    result["evidence_sha256"] = sha256_json(
        {k: v for k, v in result.items() if k != "evidence_sha256"}
    )

    return result


def write_evidence(result: Dict[str, Any]) -> None:
    evidence_dir = Path("evidence")
    evidence_dir.mkdir(parents=True, exist_ok=True)

    json_path = evidence_dir / "EKS-PSV-001.json"
    sha_path = evidence_dir / "EKS-PSV-001.sha256"

    json_text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    json_path.write_bytes(json_text.encode("utf-8"))

    file_hash = hashlib.sha256(json_path.read_bytes()).hexdigest()
    sha_path.write_text(
        f"{file_hash}  {json_path.name}\n",
        encoding="utf-8",
    )

    print("=" * 78)
    print(f"VERDICT: {result['verdict']}")
    print(f"FALSIFIER TRIGGERED: {result['falsifier']['triggered']}")
    print(f"LEDGER VERIFIED: {result['ledger_verification']['verified']}")
    print(f"EVIDENCE JSON: {json_path}")
    print(f"EVIDENCE SHA256: {file_hash}")
    print("=" * 78)


if __name__ == "__main__":
    validation_result = run_validation()
    write_evidence(validation_result)
