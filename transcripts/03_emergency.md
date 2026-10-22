# Scenario 3: Other member + emergency

Fresh `household.json`. Arjun says “my mother” — the harness infers **Meera**, not Aarav. It gathers for a couple of turns, then **chest pain** in the user text trips the red-flag check in `app/guardrails.py` and the canned emergency message takes over.

| | |
|---|---|
| Member | Meera (mother, 68) — inferred from “my mother” |
| Episode | `e0afa1b9` Feeling uneasy — new episode, not Aarav’s fever |
| Path | `gather` → `emergency` (canned copy from `app/guardrails.py`) |

## Chat

**You:** My mother is feeling uneasy

**Q** `gather` — I'm sorry your mother feels unwell. Is she having any chest discomfort, trouble breathing, fainting, sudden confusion, or new weakness?

**You:** She is feeling dizzy

**Q** `gather` — Along with the dizziness, is she having chest pain, trouble breathing, fainting, sudden confusion, new weakness, or difficulty speaking or walking?

**You:** Yeah she is saying she has slight chest pain

**Q** `emergency` — This may be a medical emergency. Contact your local emergency services immediately (for example, call 108) or go to the nearest emergency department.

**You:** Breathing issue is also there

**Q** `emergency` — This may be a medical emergency. Contact your local emergency services immediately (for example, call 108) or go to the nearest emergency department.

“Slight chest pain” matches the red-flag pattern, so code replaces the reply. The next turn stays on the same canned line; the model cannot soften it.

## What was stored

One new open episode on Meera. Seeded chronic fact (knee osteoarthritis) was already there. New episode fact: difficulty breathing alongside chest pain and dizziness. Aarav’s fever episode is not in this file.
