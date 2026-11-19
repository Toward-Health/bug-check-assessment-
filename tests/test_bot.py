import pytest

from groundbot import Appointment, answer
from groundbot.replies import REPLIES

TIME = "3 pm"


def approved_sentence(status: str) -> str:
    """The clinic's approved sentence for an appointment in this status."""
    return next(r.text for r in REPLIES if r.status == status).format(time=TIME)


def appointment(status: str) -> Appointment:
    return Appointment(patient_id="p-test", time=TIME, status=status)


@pytest.mark.parametrize("status", ["requested", "confirmed", "called", "cancelled"])
def test_status_question_is_answered_from_the_record(status):
    reply = answer("Is my 3 pm appointment confirmed?", appointment(status))
    assert reply == approved_sentence(status)


def test_negated_question_is_answered_from_the_record():
    reply = answer("I did not get a confirmation for 3 pm", appointment("requested"))
    assert reply == approved_sentence("requested")


@pytest.mark.parametrize(
    "message",
    [
        "I am having the worst headache of my life, can you fit me in at 3 pm?",
        "I have crushing chest pain and my 3 pm appointment is too far away",
    ],
)
def test_emergency_is_never_answered_with_a_booking(message):
    reply = answer(message, appointment("requested"))
    assert "911" in reply
    assert TIME not in reply


def test_opening_hours_are_answered():
    reply = answer("When are you open?", appointment("requested"))
    assert "Monday to Friday" in reply
