"""Answers a patient's message with one of the clinic's approved sentences."""

from groundbot.records import Appointment
from groundbot.replies import REPLIES
from groundbot.vectors import TfidfIndex


def ranked_replies(message: str, appointment: Appointment) -> list[tuple[float, str]]:
    """Every approved sentence with its cosine similarity to the message, best first."""
    texts = [reply.text.format(time=appointment.time) for reply in REPLIES]
    scores = TfidfIndex(texts).scores(message)
    return sorted(zip(scores, texts), reverse=True)


def answer(message: str, appointment: Appointment) -> str:
    """Reply with the approved sentence closest to the patient's message."""
    return ranked_replies(message, appointment)[0][1]
