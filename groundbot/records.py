"""The clinic's appointment record: the facts the bot is allowed to rely on."""

import json
from dataclasses import dataclass
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "appointments.json"


@dataclass(frozen=True)
class Appointment:
    patient_id: str
    time: str
    status: str  # "requested", "confirmed", "called" or "cancelled"


def load_appointment(patient_id: str, path: Path = DATA_FILE) -> Appointment:
    """Return the appointment of a made-up patient. Raises KeyError for an unknown id."""
    records = json.loads(path.read_text(encoding="utf-8"))
    return Appointment(**records[patient_id])
