"""Household members, episodes, and memory facts."""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class Member:
    id: str
    name: str
    age: int
    relationship: str


@dataclass
class Episode:
    id: str
    member_id: str
    title: str
    status: str = "open"
    created: float = field(default_factory=time.time)


@dataclass
class Fact:
    member_id: str
    key: str
    value: str
    episode_id: str | None = None


@dataclass
class Household:
    members: list[Member]
    episodes: list[Episode] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)
    turns: list[dict] = field(default_factory=list)

    def episode(self, eid: str) -> Episode | None:
        return next((e for e in self.episodes if e.id == eid), None)

    def open_episode(self, member_id: str, title: str) -> Episode:
        episode = Episode(id=uuid.uuid4().hex[:8], member_id=member_id, title=title)
        self.episodes.append(episode)
        return episode

    def add_fact(self, member_id: str, key: str, value: str, episode_id: str | None = None) -> None:
        for fact in self.facts:
            if (fact.member_id, fact.key, fact.episode_id) == (member_id, key, episode_id):
                fact.value = value
                return
        self.facts.append(Fact(member_id, key, value, episode_id))

    def summary(self) -> str:
        members = "\n".join(
            f"- {m.id}: {m.name}, {m.relationship}, age {m.age}" for m in self.members
        )
        episodes = "\n".join(
            f"- {e.id} [{e.status}] {e.member_id}: {e.title}" for e in self.episodes
        ) or "- none"
        facts = "\n".join(
            f"- {f.member_id}"
            + (f"/{f.episode_id}" if f.episode_id else "")
            + f": {f.key}={f.value}"
            for f in self.facts
        ) or "- none"
        turns = "\n".join(f"- {t['role']}: {t['text']}" for t in self.turns[-8:]) or "- none"
        return (
            f"MEMBERS\n{members}\n\nEPISODES\n{episodes}\n\n"
            f"FACTS\n{facts}\n\nRECENT TURNS\n{turns}"
        )

    def save(self, path: Path | None = None) -> None:
        (path or STORE).write_text(json.dumps(asdict(self), indent=2))


STORE = Path(__file__).resolve().parent.parent / "household.json"


def load(path: Path = STORE) -> Household:
    if not path.exists():
        return seed()
    raw = json.loads(path.read_text())
    return Household(
        members=[Member(**m) for m in raw["members"]],
        episodes=[Episode(**e) for e in raw.get("episodes", [])],
        facts=[Fact(**f) for f in raw.get("facts", [])],
        turns=raw.get("turns", []),
    )


def seed() -> Household:
    return Household(
        members=[
            Member("self", "Arjun", 36, "self"),
            Member("priya", "Priya", 34, "wife"),
            Member("aarav", "Aarav", 6, "son"),
            Member("meera", "Meera", 68, "mother"),
        ],
        facts=[
            Fact("meera", "chronic", "osteoarthritis in both knees"),
            Fact("aarav", "allergy", "none known"),
        ],
    )
