# Scenario 4: Multiple members, multiple episodes

One session. The harness keeps a **separate open episode per person** and switches when Arjun names someone else. After Priya and Arjun’s cases, “Aarav's rash” **calls back** to the original rash episode instead of opening a fourth.

| Member | Episode | Path |
|---|---|---|
| Aarav | `a491d657` Small rash on arm | `home`, then `gather` on callback |
| Priya | `ea0ddb2a` Headache reported as migraine | `home` |
| Arjun (`self`) | `ea089a20` Fall down stairs | `doctor` |

Three episodes, all still `open`. None of them were merged.

## Aarav — new episode

**You:** Aarav has a small rash on his arm

**Q** `gather` — How long has Aarav had the rash?

**You:** Since morning

**Q** `gather` — Does Aarav have a fever or seem unwell?

**You:** no all good

**Q** `gather` — Glad Aarav is feeling well. What does the rash look like—flat, raised, or blistered?

**You:** flat

**Q** `gather` — Does the rash fade briefly when you press firmly on it?

**You:** yes

**Q** `gather` — Is the rash itchy, painful, or not bothering Aarav?

**You:** no

**Q** `home` — Since Aarav feels well and the rash isn’t bothering him, monitor it for now. Wash gently, avoid new creams or soaps, and take a photo to compare tomorrow. Watch for spreading, fever, pain, blistering, or spots that stop fading when pressed.

## Priya — second episode, different member

**You:** Priya has a migraine

**Q** `gather` — I’m sorry Priya is hurting. Did the headache start suddenly and reach its worst intensity within a minute?

**You:** No started gradually

**Q** `gather` — Does Priya have any new weakness, trouble speaking, confusion, vision loss, or fever with a stiff neck?

**You:** No

**Q** `gather` — How long has Priya had this headache?

**You:** She has had it since an hour. It gets sightly triggered by sunlight

**Q** `gather` — How severe is Priya’s headache on a scale of 0–10, where 10 is the worst pain imaginable?

**You:** 6

**Q** `gather` — Has Priya had similar headaches before, or is this her first headache like this?

**You:** yes she has

**Q** `gather` — Is this headache similar to Priya’s usual headaches in severity and symptoms, or is anything different this time?

**You:** similar

**Q** `home` — Since this feels like her usual headaches, Priya can rest in a quiet, darkened room, drink water, and have a light snack if she has missed a meal. She can use her usual headache medicine as directed if it is normally safe for her. Monitor her pain and watch for any new or different symptoms.

Aarav’s rash episode was left open. This did not attach to it.

## Arjun — third episode, self

**You:** I just fell down stairs

**Q** `gather` — I'm sorry that happened. Did you hit your head or lose consciousness, even briefly?

**You:** No, my foot is hurting

**Q** `gather` — Without forcing it, are you able to put weight on the sore foot and take four steps?

**You:** No

**Q** `doctor` — This case is being transferred to a human doctor for review. A clinician will follow up. If symptoms worsen or you are worried, seek in-person care.

## Aarav — callback to the same episode

After two other people’s cases, Arjun mentions the rash again. Same `episode_id` (`a491d657`), not a new episode and not mixed into the fall or migraine.

**You:** Aarav's rash is burning slightly now

**Q** `gather` — I'm sorry it's bothering him now. Has the rash spread or developed swelling or blisters?

## What was stored

Facts are keyed by `member_id` + `episode_id`: rash appearance/blanching on Aarav, migraine history/severity on Priya, fall + cannot take four steps on Arjun. Switching the subject opened a new episode; naming Aarav’s rash again reused the first one.
