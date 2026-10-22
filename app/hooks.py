"""Extension points. Intentionally unused — lab analysis, KB, and telemedicine plug in here later."""


def analyze_lab(report: str) -> None:
    raise NotImplementedError


def search_kb(query: str) -> None:
    raise NotImplementedError


def handoff_telemedicine(episode_id: str) -> None:
    raise NotImplementedError
