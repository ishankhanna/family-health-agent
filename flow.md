# Flow

`python3 app/cli.py` loads or seeds a household and loops on stdin. Each line is one `turn()`.

```
app/cli.py  →  agent.turn()  →  gpt-6.1-sol JSON  →  guardrails.apply()  →  reply
                    │                                      │
                    └──────── state.py (members / episodes / facts / turns)
```

1. **`app/cli.py`** — loads `household.json` if present (else seeds Arjun / Priya / Aarav / Meera), reads a line, prints the reply, saves after each turn.
2. **`agent.turn()`** — appends the user text, sends `house.summary()` plus the message to GPT-6.1 Sol (`openai_key.txt` or `OPENAI_API_KEY`), and gets structured JSON: who it is about, which episode, new facts, disposition, reply.
3. **`app/state.py`** — if the model opens a new condition, create an episode; upsert extracted facts onto that member/episode.
4. **`app/guardrails.py`** — code owns the last word. Red-flag text or `disposition=emergency` becomes the canned ER message. `disposition=doctor` becomes the canned doctor-transfer message. Otherwise the model's question or home-care text is shown as-is.
5. **`app/hooks.py`** — unused on purpose. Labs, KB, and telemedicine plug in later without changing the loop.

The LLM does fuzzy work (member, episode, what to ask). Code does safety and memory. One call per turn, no extra agents.
