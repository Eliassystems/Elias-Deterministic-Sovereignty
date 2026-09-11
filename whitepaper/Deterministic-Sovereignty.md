# The Manifesto of Deterministic Sovereignty

## Why I Built Pre-Execution Governance Before I Had a Name for It

**Gary Williams**  
Founder & Chief Architect, Elias Systems Ltd  
11 September 2026

---

## Preface: This is not a story about prophecy

I am not a messiah. I am not claiming revelation. I am not asking anyone to believe that I possess some special truth unavailable to everybody else.

I am a builder.

What I am publishing is an explanation of why I came to see certain problems differently, why the architecture of Elias Systems developed the way it did, and why concepts such as present standing, pre-execution authority, revocation, evidence provenance, glass-box governance and consequence gating feel instinctive to me rather than theoretical.

I can trace the underlying logic back to at least 2015.

I did not call it *pre-execution governance* then.

I lived it.

And for years afterward, I continued living under conditions in which the separation between thought, authority and action was not an academic distinction. It affected whether I remained free.

That experience eventually became architecture.

---

## 1. When Consequence Is Real, Governance Stops Being Abstract

For much of my life, consequence was not hypothetical.

I served an indeterminate sentence of Imprisonment for Public Protection. I lived inside a system in which release could depend upon assessments of future risk: what somebody believed I might do, what somebody thought information about me meant, how my conduct was interpreted, and whether decision-makers considered me safe enough to progress.

I had also lived in environments involving gangs, guns and serious violence. People had attempted to take my life.

Those experiences altered my relationship with threat.

Once you have experienced the possibility of losing your physical freedom and your life, many of the things that intimidate people in ordinary professional environments stop looking like existential threats.

A disagreement is a problem.

A gatekeeper is a problem.

A commercial rejection is a problem.

A technical failure is a problem.

A powerful institution is a system.

And systems can be observed.

They can be mapped.

Their authorities can be identified.

Their dependencies can be identified.

Their failure conditions can be identified.

Their boundaries can be identified.

And sometimes the correct answer is not to defeat a system at all, but simply to understand which parts of it you cannot control and govern your own actions accordingly.

That mindset is important to understanding Elias.

---

## 2. The Black Box Was Not a Metaphor to Me

One of the experiences that influenced me most deeply was the use of security intelligence inside the prison system.

Decisions affecting progression, lower-security categorisation, temporary release or home leave could be influenced by intelligence that I could not meaningfully inspect.

From my position inside the system, the problem was simple.

There could be consequential information.

I could be affected by that information.

Yet I could not necessarily inspect the complete underlying evidence, challenge every proposition or determine precisely how the information had been transformed into the decision made about me.

Whatever the institutional reasons for confidentiality, the experience taught me something fundamental:

**A consequential system becomes extremely difficult to trust when the person affected cannot inspect the evidential path from input to decision.**

That experience is one reason I am so hostile to unnecessary black boxes.

Not because secrecy is never legitimate.

Not because every piece of information must always be public.

But because **authority without inspectable provenance creates an extraordinary concentration of power**.

If a machine says:

> REFUSE

I want to know why.

If a machine says:

> PERMIT

I want to know why.

If evidence contributed to the decision, I want to know what evidence.

If a rule controlled the outcome, I want the rule identified.

If authority existed, I want to know where it came from.

If standing changed, I want the change preserved.

If the machine does not know, uncertainty itself should be an admissible state.

This eventually became what I call **Glass-Box Governance**.

---

## 3. You Cannot Prove a Future That Has Not Happened

The parole process exposed another problem to me.

At its simplest, the system was attempting to answer a future-facing question:

**What is the probability that this person will cause serious harm if released?**

That is an understandable public-protection question.

But it contains an unavoidable epistemic limitation.

The future has not happened.

A person cannot provide mathematical proof that they will never commit another offence.

An assessor cannot possess complete knowledge of every future circumstance.

At some point, prediction enters the system.

Probability enters the system.

Judgment enters the system.

That does not make risk assessment illegitimate.

It does mean something important:

**prediction and proof are not the same thing.**

And a second problem emerges.

Whenever people know the criteria by which they are being assessed, behaviour can begin adapting to the assessment system itself.

People learn the language.

They learn expected answers.

They learn what signals are rewarded.

They learn what signals cause concern.

This does not mean every answer is dishonest.

It means that the measurement process can influence the thing being measured.

That insight stayed with me.

Years later, when I examined probabilistic artificial-intelligence systems, I recognised a familiar structural problem.

A system generates an uncertain proposition.

Another uncertain system assesses it.

A score is generated.

Another threshold is applied.

And somewhere downstream, a real-world consequence may occur.

My question became:

**At what point does probability stop being information and start becoming authority?**

That distinction became foundational.

---

## 4. The Lesson I Learned Was Not "Remove Probability"

Human beings are not deterministic machines.

Neither are modern generative models.

Emotion is not deterministic.

Prediction is not certainty.

Judgment is not mathematical proof.

So my architecture does not require the impossible elimination of uncertainty.

It requires the separation of uncertainty from authority.

That is the distinction.

A probabilistic model may say:

> I estimate an 84% likelihood that this action is appropriate.

Useful.

But 84% confidence does not itself establish:

- who authorised the action;
- whether that authority remains current;
- whether the proposed action is within scope;
- whether circumstances have materially changed;
- whether the target is permitted;
- whether jurisdiction remains valid;
- whether a human veto has occurred;
- whether the consequence exceeds an allowed ceiling;
- whether the evidence supporting the action still possesses standing.

Those are governance questions.

And governance questions should not silently inherit their answer from model confidence.

**Capability is not authority.**

That sentence became one of the deepest foundations of Elias.

---

## 5. Nine Years on Life Licence Taught Me the Execution Seam

My education did not finish when I left prison.

For approximately nine years, I remained subject to life-licence conditions.

That created another form of discipline.

My internal state and my external action could not simply be treated as the same thing.

I could be angry.

I could be frustrated.

I could feel unfairly treated.

I could experience stress.

I could disagree with somebody.

Those internal states were real.

But I still had to govern what happened next.

Because conduct could have consequences for my liberty.

That forced me to develop a separation that later became fundamental to the systems I build:

**state is not execution.**

Feeling something does not authorise an action.

Thinking something does not authorise an action.

Being capable of doing something does not authorise an action.

Predicting that something is correct does not authorise an action.

There is a boundary between **internal state** and **external consequence**.

That boundary is the execution seam.

Looking back, I can now see that I had been practising a human version of pre-execution governance long before I began implementing it computationally.

Before acting, I had to ask:

What is happening?

What am I actually responding to?

What authority do I have?

What are the consequences?

What happens if I am wrong?

Has anything materially changed?

Is the action necessary?

Can I remain within the rules even when my internal state is turbulent?

That is not mathematical determinism.

It is **deterministic discipline**:

pre-established rules governing consequential behaviour despite uncertain internal conditions.

That distinction matters.

---

## 6. From Lived Discipline to Machine Architecture

When I later began building Elias Systems, I did not begin with the question:

> How do we make artificial intelligence nicer?

I began with a different question:

> **What must be true before a machine is allowed to cause a consequential state change?**

That question reorganises the entire problem.

Traditional approaches often concentrate enormous intelligence inside the model itself.

My approach separates intelligence from governing authority.

The AI can observe.

It can interpret.

It can propose.

It can reason.

It can generate.

But before proposal becomes consequence, something else must happen.

The system must establish standing.

In Elias, the conceptual progression became:

**Identity -> Observation -> Understanding -> Governance -> Intelligence -> Execution -> Witness**

The exact implementation can vary.

The governing principle does not.

**Intelligence must not manufacture its own authority to execute.**

---

## 7. Pre-Execution Governance

Pre-execution governance therefore means that consequential action encounters a governance boundary **before** execution.

Not merely logging afterward.

Not merely explaining afterward.

Not merely detecting damage afterward.

Not simply asking another language model whether the first language model's answer appears safe.

At the execution boundary, the system must be capable of asking deterministic questions such as:

**Who is acting?**

**What action is being requested?**

**Against what resource?**

**Under whose authority?**

**Within what scope?**

**Under which policy?**

**Under which jurisdiction?**

**Using what evidence?**

**Is that evidence still valid?**

**Has material state changed?**

**Has authority been revoked?**

**Does the consequence exceed the permitted ceiling?**

**Is human approval required?**

**Can the resulting decision be witnessed and reconstructed?**

Where the required standing cannot be established, the system should be capable of refusing execution.

That is very different from asking whether an output *sounds safe*.

---

## 8. Present Standing: The Lesson of Revocable Freedom

Life under conditional liberty also taught me something else.

Historical permission is not necessarily present permission.

Something may have been valid yesterday and invalid today.

Authority can change.

Circumstances can change.

Risk conditions can change.

Evidence can become stale.

Permissions can be revoked.

This became another fundamental proposition inside Elias:

> **Historical validity does not, by itself, establish present governing standing after a material change in conditions.**

That proposition now appears throughout the architecture in different forms.

Authority epochs.

Changed-condition checks.

Revocation.

Continuity.

Reassessment.

Present-tense admissibility.

Execution-bound validation.

This is why I care so much about the moment immediately before consequence.

A system should not merely ask:

> Was this ever authorised?

It should ask:

> **Is it authorised now?**

---

## 9. The Internal Firewall and the External Firewall

People sometimes think cybersecurity begins at the perimeter.

My own experience taught me that this is incomplete.

Systems can fail externally.

But they can also fail internally through corrupted authority, incomplete information, hidden evidence, stale standing, conflicting policy, manipulated instructions or inappropriate execution.

That is why I eventually arrived at both **external** and **internal** governance firewalls.

The external firewall deals with what attempts to enter or interact with the governed environment.

The internal firewall deals with whether something already inside the system possesses authority to proceed.

That distinction is crucial in agentic AI.

An instruction can originate inside a trusted environment and still be inadmissible.

A credential can be genuine while its authority has expired.

A user can be authenticated but lack authority for a particular action.

A model can generate a technically correct command that it has no standing to execute.

A previously valid instruction can lose standing because the world changed between authorisation and execution.

Security therefore cannot stop at:

**Who are you?**

It must continue:

**What are you authorised to do, to what, under which conditions, right now?**

---

## 10. LOVE-OS: Why Some Things Should Not Move

My experience with changing criteria also influenced another part of the architecture.

Adaptive systems are powerful.

But if everything is adaptive, everything becomes negotiable.

A governance architecture therefore needs to distinguish between what may evolve and what must remain stable unless deliberately reconstituted.

That insight became the constitutional concept inside **LOVE-OS**.

The language I use is a **97% immutable ethical core with a governed 3% extension**.

The percentage expresses an architectural principle: a dominant constitutional baseline with a deliberately constrained adaptive surface.

The point is not that a computer magically discovers morality.

The point is that certain governing invariants should not be silently rewritten by the same intelligence they are supposed to restrain.

Rules such as:

**Capability is not authority.**

**Intention precedes intelligence.**

**Uncertainty is an admissible state.**

**Consequential execution requires standing.**

**Authority can be revoked.**

**Evidence should retain provenance.**

**Human authority must not disappear merely because machine capability increases.**

If these are constitutional constraints, then the system manipulating the world should not possess unilateral authority to redefine them when they become inconvenient.

---

## 11. Glass Box, Not Oracle

This is also why Elias is deliberately not presented as an oracle.

A governance architecture that claims never to be wrong has already created its next black box.

The objective is different.

When Elias permits something, preserve why.

When Elias refuses something, preserve why.

When it does not know, preserve that uncertainty.

When evidence changes, preserve the change.

When an architecture fails a test, preserve the failure.

When a falsifier is triggered, do not hide it.

When a proposition survives examination, state exactly the scope within which it survived.

This is why my operating language became:

**Lock it.  
Log it.  
Prove it.**

Not:

**Trust me.**

---

## 12. Why I Have Built So Much So Quickly

People may look at the volume of architecture I have produced and assume that it appeared suddenly.

It did not.

The software is recent.

The underlying mental models are not.

For years I was forced to think constantly about:

authority;

constraints;

boundaries;

evidence;

interpretation;

present standing;

revocation;

consequence;

uncertainty;

human behaviour;

system incentives;

and the difference between what somebody believes and what they can actually establish.

When I finally had access to modern AI systems, I did not use them to replace that thinking.

I used them to accelerate its expression.

That is what I mean by a builder using AI as a refiner.

The machine can dramatically compress implementation.

But the machine cannot supply the human being's lived causal model merely by producing articulate text.

The architecture exists because the reasoning existed before the code.

AI accelerated the conversion of that reasoning into executable artefacts.

---

## 13. Deterministic Sovereignty

I call the principle **Deterministic Sovereignty**.

It does not mean eliminating uncertainty.

It does not mean eliminating probability.

It does not mean humans become machines.

It means this:

> **Where an action can create material consequence, probability may inform the action, but probability alone must not possess sovereign authority to execute it.**

Between intelligence and consequence there must be governance.

Between capability and execution there must be authority.

Between historical permission and present action there must be reassessment where conditions have changed.

Between evidence and decision there must be provenance.

Between machine action and human consequence there must be accountability.

And where the necessary standing does not exist:

**the machine must be capable of doing nothing.**

That is the architecture.

And now the architecture can be examined independently of the story that produced it.

---

## 14. The Machine Form

The philosophy above can be reduced into a small governing structure.

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Decision(Enum):
    PERMIT = "PERMIT"
    REFUSE = "REFUSE"
    ESCALATE = "ESCALATE"
    UNCERTAIN = "UNCERTAIN"


@dataclass
class Authority:
    subject: str
    action: str
    resource: str
    epoch: int
    active: bool


@dataclass
class Intent:
    actor: str
    action: str
    resource: str
    consequence_tier: int
    authority_epoch: int


@dataclass
class GovernanceState:
    current_epoch: int
    human_veto: bool
    evidence_complete: bool
    policy_allows: bool
    consequence_ceiling: int


def pre_execution_govern(
    intent: Intent,
    authority: Optional[Authority],
    state: GovernanceState
) -> Decision:

    if authority is None:
        return Decision.REFUSE

    if authority.subject != intent.actor:
        return Decision.REFUSE

    if authority.action != intent.action:
        return Decision.REFUSE

    if authority.resource != intent.resource:
        return Decision.REFUSE

    if intent.authority_epoch != state.current_epoch:
        return Decision.REFUSE

    if not authority.active:
        return Decision.REFUSE

    if state.human_veto:
        return Decision.REFUSE

    if not state.evidence_complete:
        return Decision.UNCERTAIN

    if not state.policy_allows:
        return Decision.REFUSE

    if intent.consequence_tier > state.consequence_ceiling:
        return Decision.ESCALATE

    return Decision.PERMIT
```

The intelligence system can be probabilistic.

The proposal can be probabilistic.

The prediction can be probabilistic.

The model can say:

```python
model_confidence = 0.93
```

But notice what the governance function does **not** say:

```python
if model_confidence > 0.90:
    execute()
```

Confidence is information.

It is not sovereign authority.

The execution seam asks a different question:

```text
CAPABLE?
    |
    v
AUTHORIZED?
    |
    v
CURRENT?
    |
    v
IN SCOPE?
    |
    v
EVIDENCE SUFFICIENT?
    |
    v
POLICY STANDING?
    |
    v
HUMAN VETO?
    |
    v
CONSEQUENCE WITHIN CEILING?
    |
    v
PERMIT
```

If a required governing property disappears before execution:

```text
PROPOSAL
   |
   v
MATERIAL CHANGE
   |
   v
AUTHORITY REVOKED
   |
   v
PRESENT STANDING = FALSE
   |
   v
REFUSE
```

That is pre-execution governance in its simplest form.

The machine is allowed to think probabilistically.

It is **not allowed to convert its own confidence into authority**.

---

## Closing

The most important thing about my history is not that hardship somehow made me uniquely qualified.

It is that certain problems became impossible for me to ignore.

I know what it feels like to exist under consequential decisions.

I know what it feels like when evidence cannot be inspected.

I know what it means for authority to determine freedom.

I know what it means for standing to be conditional.

I know what it means to govern an action before it becomes a consequence.

I know what it means for internal state and external action to be different things.

Those experiences became mental architecture.

The mental architecture became system architecture.

The system architecture became executable code.

And now the code is public enough to be challenged.

That is where belief ends.

**Examine it.**

**Freeze the proposition.  
Run the mechanism.  
Preserve the result.**

**Work is for Robots.  
Life is for Humans.**

— **Gary Williams**  
Founder & Chief Architect  
**Elias Systems Ltd**
