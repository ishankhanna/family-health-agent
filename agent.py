"""One structured LLM turn, then programmatic guardrails and state updates."""

from __future__ import annotations

import json
import os
from pathlib import Path

from openai import OpenAI

from guardrails import apply
from state import Household

ROOT = Path(__file__).parent
MODEL = "gpt-6.1-sol"

SYSTEM = """You are a family-health triage assistant for one household.
Reason about WHO a message is about and WHICH episode it belongs to.
Never write emergency or doctor-handoff wording — the program replaces those.

Return ONLY a JSON object:
{
  "member_id": "self|priya|aarav|meera"|null,
  "episode_id": "<existing id or null>",
  "new_episode_title": "short title or null if attaching/unknown",
  "facts": [{"key": "...", "value": "..."}],
  "disposition": "gather|home|doctor|emergency",
  "reply": "one focused follow-up question OR home-monitoring steps. Empathic, concise."
}

Rules:
- Infer member from names, kinship ("my son"), or pronouns given recent turns. Ask once if truly ambiguous.
- Attach follow-ups to an open episode of that member. Open a new episode only for a new condition.
- Ask for missing triage (duration, severity, red flags, associated symptoms) — one question at a time.
- Use remembered facts. Use disposition=home only when you have enough to advise self-care.
- disposition=doctor if non-emergent but needs a clinician. disposition=emergency for red flags.
"""


def load_api_key() -> str:
    if key := os.environ.get("OPENAI_API_KEY"):
        return key.strip()
    path = ROOT / "openai_key.txt"
    if path.exists() and (key := path.read_text().strip()):
        return key
    raise SystemExit("Missing OpenAI key. Put it in openai_key.txt or set OPENAI_API_KEY.")


def complete(prompt: str) -> dict:
    response = OpenAI(api_key=load_api_key()).chat.completions.create(
        model=MODEL,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    )
    return json.loads(response.choices[0].message.content or "{}")


def turn(house: Household, user: str) -> str:
    house.turns.append({"role": "user", "text": user})
    data = complete(f"HOUSEHOLD\n{house.summary()}\n\nUSER\n{user}")
    member_id = data.get("member_id")
    episode_id = data.get("episode_id")
    if member_id and data.get("new_episode_title") and not house.episode(episode_id or ""):
        episode_id = house.open_episode(member_id, data["new_episode_title"]).id
    for fact in data.get("facts") or []:
        if member_id and fact.get("key"):
            house.add_fact(member_id, fact["key"], str(fact.get("value", "")), episode_id)
    disposition, reply = apply(data.get("disposition", "gather"), user, data.get("reply") or "")
    house.turns.append(
        {
            "role": "assistant",
            "text": reply,
            "disposition": disposition,
            "member_id": member_id,
            "episode_id": episode_id,
        }
    )
    return reply
