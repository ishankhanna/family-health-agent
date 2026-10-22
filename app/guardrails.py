"""Deterministic safety layer."""

import re

EMERGENCY = (
    "This may be a medical emergency. Contact your local emergency services immediately "
    "(for example, call 108) or go to the nearest emergency department."
)

DOCTOR = (
    "This case is being transferred to a human doctor for review. "
    "A clinician will follow up. If symptoms worsen or you are worried, seek in-person care."
)

RED_FLAGS = [
    r"can'?t breathe|cannot breathe|trouble breathing|difficulty breathing|short(ness)? of breath",
    r"chest pain|pressure in (my|his|her|their) chest",
    r"unresponsive|unconscious|passed out|won'?t wake",
    r"severe allerg|anaphyla|lips? (are |is )?swell|throat (is )?clos",
    r"blue lips|not breathing",
    r"seizure|convulsion",
]


def is_emergency(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(pattern, lowered) for pattern in RED_FLAGS)


def apply(disposition: str, user_text: str, reply: str) -> tuple[str, str]:
    if is_emergency(user_text) or disposition == "emergency":
        return "emergency", EMERGENCY
    if disposition == "doctor":
        return "doctor", DOCTOR
    return disposition, reply
