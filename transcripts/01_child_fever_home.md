# Scenario 1: Child fever → home monitoring

Arjun says “my son feels warm.” The harness infers **Aarav**, opens one episode, asks triage questions one at a time, then advises **home monitoring**. A later Crocin question stays on the same episode.

| | |
|---|---|
| Member | Aarav (son, 6) — inferred from “my son”, never asked who |
| Episode | `Feeling warm` (opened on turn 1, reused through the end) |
| Path | `gather` until enough context, then `home` |

## Chat

**You:** My son feels warm

**Q** `gather` — Have you checked Aarav’s temperature with a thermometer, and if so, what was the reading?

**You:** 101 fahrenheit

**Q** `gather` — Is Aarav alert and breathing comfortably, without a stiff neck, an unusual rash, or difficulty waking?

**You:** Yes, that is all good

**Q** `gather` — That’s reassuring. How long has Aarav had the fever?

**You:** It has been 2 hours

**Q** `gather` — Is Aarav drinking fluids and urinating about as usual?

**You:** Yes that is fine. He is not eating much as he does not feel like eating

**Q** `home` — It’s reassuring that Aarav is drinking and urinating normally. A reduced appetite is common with fever—offer small portions if he wants them, but don’t force food. Keep offering fluids, let him rest, and monitor his temperature, alertness, breathing, and urination.

**You:** Can I give him Crocin 500mg?

**Q** `gather` — Crocin is paracetamol, and children’s doses depend on weight. Don’t give Aarav a full 500 mg tablet for now. How much does he weigh in kilograms?

**You:** 40 kilogram

**Q** `gather` — Thanks. Before giving Crocin, has Aarav taken any paracetamol or other fever/cold medicine in the past 24 hours—and if so, how much and when?

**You:** no

**Q** `home` — At Aarav’s reported weight of 40 kg, a 500 mg dose is within the usual paracetamol dose range. If the Crocin contains only paracetamol, you can give one 500 mg tablet if he is uncomfortable and can swallow tablets safely. Leave at least 6 hours between doses; give no more than 4 tablets in 24 hours. Avoid other medicines containing paracetamol. He doesn’t need medicine just for a temperature of 101°F if comfortable. Continue fluids and monitor his alertness, breathing, and urination.

**You:** okay

**Q** `home` — Keep offering Aarav fluids and let him rest; it’s okay if he eats less for now. Use Crocin only if he’s uncomfortable, following the dosing limits discussed. Monitor his temperature, alertness, breathing, and urination.

## What was stored

Episode stayed open on Aarav. Facts written along the way: temperature 101°F, duration 2 hours, alert / breathing comfortably, no stiff neck or unusual rash, drinking and urinating as usual, reduced appetite, weight 40 kg, no paracetamol in the last 24 hours.
