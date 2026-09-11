# Elias Deterministic Sovereignty

**Pre-Execution Governance, Present Standing, Revocation and Glass-Box Evidence**

This repository publishes a bounded Elias Systems reference demonstrator alongside the white paper:

**The Manifesto of Deterministic Sovereignty — Why I Built Pre-Execution Governance Before I Had a Name for It**

Author: **Gary Williams**  
Founder & Chief Architect, **Elias Systems Ltd**  
Publication date: **11 September 2026**

---

## Purpose

This repository makes two things public together:

1. the reasoning that led to the Elias pre-execution governance architecture; and
2. a runnable bounded demonstrator showing how present authority, scope, revocation and witness evidence can be evaluated before consequential execution.

The central proposition tested by the runnable demonstrator is:

> **Historical authority alone does not establish present execution standing after a material authority-state change. Consequential execution requires current authority scoped and bound to the specific intent at the execution seam.**

The repository is deliberately glass-box.

The code can be inspected.

The test can be rerun.

The evidence can be independently hashed.

The stated limits are part of the release.

---

## Repository Structure

```text
Elias-Deterministic-Sovereignty/
|
|-- README.md
|
|-- whitepaper/
|   `-- Deterministic-Sovereignty.md
|
|-- src/
|   `-- keystone_present_standing_v1.py
|
`-- evidence/
    |-- EKS-PSV-001.json
    `-- EKS-PSV-001.sha256
```

---

## White Paper

Read:

[`whitepaper/Deterministic-Sovereignty.md`](whitepaper/Deterministic-Sovereignty.md)

The paper explains the intellectual path behind the architecture, including:

- pre-execution restraint;
- probability versus authority;
- glass-box governance;
- present standing;
- revocation;
- internal and external governance boundaries;
- constitutional invariants;
- deterministic discipline;
- the execution seam;
- human sovereignty;
- witness and provenance.

It is an origin and architecture paper.

The personal history explains **why the architecture emerged**.

It is not offered as proof that the architecture works.

The runnable mechanism and preserved evidence must stand on their own.

---

## Runnable Demonstrator

Source:

[`src/keystone_present_standing_v1.py`](src/keystone_present_standing_v1.py)

Run from the repository root:

```powershell
python .\src\keystone_present_standing_v1.py
```

The demonstrator evaluates three bounded cases.

### PC — Present Standing Survives

A currently valid authority epoch is used for an action and resource inside its constituted scope.

Expected result:

```text
PERMITTED
PRESENT_STANDING_ESTABLISHED
```

### NEG-1 — Scope Deficit

The authority epoch remains valid, but the requested action is outside the delegated scope.

Expected result:

```text
REFUSED
ACTION_OUT_OF_SCOPE
```

### NEG-2 — Historical Authority After Revocation

The same previously valid authority epoch is materially changed by revocation before the next consequential execution attempt.

Expected result:

```text
REFUSED
AUTHORITY_EPOCH_REVOKED
```

---

## Frozen Validation Result

Frozen release result:

```text
VERDICT: PASS_WITHIN_FROZEN_BOUNDED_SCOPE
FALSIFIER TRIGGERED: False
LEDGER VERIFIED: True
```

The falsifier is triggered if:

- the valid in-scope positive control is refused;
- an out-of-scope action is permitted;
- the historically valid epoch is permitted after revocation; or
- the witness hash chain fails verification.

None of those conditions occurred in the frozen run.

---

## Frozen Release Hashes

### Evidence JSON

File:

```text
evidence/EKS-PSV-001.json
```

SHA-256:

```text
BDA6CBEF7638A14715942EE2668B514083894A9474506E9AD8FC70C2DA5FD3AD
```

### Source Code

File:

```text
src/keystone_present_standing_v1.py
```

SHA-256:

```text
78262C0A367D53C0451FAC394EA9B641EC9CFC021D8E320BC63BDA6310DF5DBA
```

### White Paper

File:

```text
whitepaper/Deterministic-Sovereignty.md
```

SHA-256:

```text
3B47672AC55D4FDF9E4A8F59B3A11FC124D652436C2F16EFBBDF145BB8E76C04
```

---

## Important Reproducibility Note

A fresh execution will generate new timestamps, a new authority epoch and therefore a new evidence-file hash.

That does **not** invalidate the frozen run.

The hashes above identify the exact source, paper and evidence artifacts preserved for this release.

The committed frozen evidence should not be regenerated after the release is frozen unless a new version is intentionally created.

---

## What This Demonstrator Establishes

Within its frozen bounded scope, this release demonstrates that the mechanism can distinguish between:

- present authority and absent authority;
- in-scope and out-of-scope execution;
- historically valid authority and currently revoked authority;
- permitted execution and refused execution;
- a valid witness chain and a corrupted witness chain condition.

It also demonstrates an execution binding between the current authority epoch and the specific governed intent.

---

## What This Demonstrator Does Not Establish

This release does **not** claim to prove:

- external identity;
- legal authority;
- cryptographic key ownership;
- truth of an external policy source;
- distributed immutability;
- external notarisation;
- production deployment security;
- complete enterprise governance;
- correctness of every Elias Systems architecture;
- deterministic truth from probabilistic AI outputs.

Model confidence is deliberately non-authoritative.

A confidence score is information.

It is not execution authority.

---

## Core Principle

> **Capability is not authority.**

A system may be capable of producing an action without possessing standing to execute it.

The pre-execution seam exists to keep those concepts separate.

---

## Deterministic Sovereignty

Deterministic Sovereignty does not mean eliminating uncertainty or probability.

It means:

> **Where an action can create material consequence, probability may inform the action, but probability alone must not possess sovereign authority to execute it.**

The intelligence system may remain probabilistic.

The execution decision must still establish the governing conditions required for consequence.

---

## Glass-Box Standard

The Elias operating discipline is:

**Lock it.  
Log it.  
Prove it.**

A PASS should be preserved.

A failure should be preserved.

A falsifier should be explicit.

A scope boundary should remain visible.

No standing is transferred merely because another component, architecture or prior state possessed it.

---

## Examination

This release is published to be examined rather than believed.

Inspect the paper.

Inspect the code.

Run the mechanism.

Verify the hashes.

Challenge the proposition.

Preserve whatever happens.

---

**Gary Williams**  
Founder & Chief Architect  
**Elias Systems Ltd**

**Work is for Robots & Life is for Humans.**
