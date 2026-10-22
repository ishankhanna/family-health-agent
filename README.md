# Family Health Agent

A small family health chat. The model figures out who you mean and whether this is a new problem or a follow-up. Code remembers the family, and it owns the two hard exits: emergency, or handoff to a doctor.

How it runs: [flow.md](flow.md). What it could become: [PRODUCT.md](PRODUCT.md).

**Family in this demo:** Arjun (you), Priya (wife, 34), Aarav (son, 6), Meera (mother, 68).

## Design

- **One loop.** Each message is one GPT-6.1 Sol call. It returns JSON: who, which episode, new facts, what to do next, and a reply. No extra framework.
- **Split of work.** The model handles messy language (names, “he”, what to ask). `app/guardrails.py` can force an emergency from red-flag words, and always uses fixed text for emergency and doctor handoff.
- **Memory.** Members, open problems, facts, and chat live in `household.json` and load again on startup. A follow-up sticks to an open problem. A new illness opens a new one.
- **Room to grow.** `app/hooks.py` is empty on purpose. Lab reports, a knowledge base, and telemedicine can plug in later.

## Run

```bash
cd FamilyHealthAgent
python3 -m pip install -r requirements.txt
```

Copy `openai_key.txt.example` to `openai_key.txt` and paste your key (one line, no quotes), or set `OPENAI_API_KEY`. Then:

```bash
python3 app/cli.py
```

Type as the parent, e.g. `My son feels warm.` Ctrl-C to quit. Chat is saved to `household.json`. Delete that file to start over.

Do not zip or push `openai_key.txt` or `household.json`. Both are gitignored.

## Transcripts

1. [Child fever → home](transcripts/01_child_fever_home.md)
2. [Same episode → doctor](transcripts/02_same_episode_doctor.md)
3. [Other member → emergency](transcripts/03_emergency.md)
4. [Multiple members, multiple episodes](transcripts/04_multi_member_episodes.md)
