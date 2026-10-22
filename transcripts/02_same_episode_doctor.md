# Scenario 2: Same episode + doctor transfer

This continues scenario 1. On restart the CLI loaded `household.json`. Arjun did not name Aarav. The harness attached “his fever” to the open **Feeling warm** episode, reused earlier facts, and escalated because the temperature rose to 104°F. A follow-up about Dolo stayed on that same episode and kept the canned doctor message — it did not fall back to home-care dosing.

| | |
|---|---|
| Member | Aarav — from “his” / “him”, not re-identified |
| Episode | `9a468464` Feeling warm — **same id as scenario 1**, no new episode |
| Path | `doctor` (canned handoff text from `guardrails.py`) |

## Chat

*(Prior context: Aarav, 101°F for 2 hours, drinking, alert, Crocin discussed. Then a new `python3 cli.py`.)*

**You:** His fever is now 104F after a few hours

**Q** `doctor` — This case is being transferred to a human doctor for review. A clinician will follow up. If symptoms worsen or you are worried, seek in-person care.

**You:** Should I give him Dolo 650?

**Q** `doctor` — This case is being transferred to a human doctor for review. A clinician will follow up. If symptoms worsen or you are worried, seek in-person care.

Both replies are the fixed doctor message. After handoff, code keeps replacing the wording so the model cannot go back to casual home advice.

## What was stored

Still one open episode on Aarav. `temperature` was updated in place from 101°F to 104°F. New fact `fever_progression=Increased from 101°F to 104°F over a few hours`. `medication_question` was updated to the Dolo 650 mg ask. No second episode was opened.
