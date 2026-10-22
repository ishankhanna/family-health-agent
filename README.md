# Family Health Agent

A small triage harness for one household. The LLM infers *who* a message is about, *which episode* it belongs to, and what to ask next. Code owns memory and the two hard exits (emergency / doctor transfer). See [flow.md](flow.md). Product vision: [PRODUCT.md](PRODUCT.md).

**Seeded family:** Arjun (you), Priya (wife, 34), Aarav (son, 6), Meera (mother, 68).

## Design

- **One loop, one model call.** GPT-6.1 Sol returns JSON: member, episode, facts, disposition, reply. No agent framework.
- **LLM vs code.** The model does fuzzy work (kinship, pronouns, follow-up questions, home-care wording). `guardrails.py` can upgrade a turn to emergency from red-flag text and always replaces emergency/doctor copy with canned messages.
- **State is the memory.** Members, open episodes, facts, and turns live in `household.json` and are reloaded on startup. `house.summary()` feeds that context back to the model. Follow-ups attach to an open episode; a new condition opens a new one.
- **Extensibility, not features.** `hooks.py` is unused. Labs, a knowledge base, and telemedicine can plug in later without changing the loop.

## Run

```bash
cd FamilyHealthAgent
python3 -m pip install -r requirements.txt
```

Copy `openai_key.txt.example` to `openai_key.txt` and paste your key (one line, no quotes), or set `OPENAI_API_KEY`. Then:

```bash
python3 cli.py
```

Type as the parent, e.g. `My son feels warm.` Ctrl-C to exit. Each turn is saved to `household.json` so the next run continues the same household. Delete that file to start over.

Do not include `openai_key.txt` or `household.json` in a zip or git push. Both are gitignored.

## Transcripts

1. [Child fever → home](transcripts/01_child_fever_home.md)
2. [Same episode → doctor](transcripts/02_same_episode_doctor.md)
3. [Other member → emergency](transcripts/03_emergency.md)
4. [Multiple members, multiple episodes](transcripts/04_multi_member_episodes.md)
