"""The only sentences the bot may say. Written and approved by the clinic, not by a model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reply:
    topic: str
    status: str | None  # the appointment status this sentence is true for, if any
    text: str  # "{time}" is filled in from the appointment record


REPLIES = [
    Reply("appointment", "requested",
          "We have received your request for {time}. We will contact you once it is settled."),
    Reply("appointment", "confirmed",
          "Yes, we have confirmed your appointment for {time}."),
    Reply("appointment", "called",
          "We have called you about your appointment for {time}. Please call us back to settle it."),
    Reply("appointment", "cancelled",
          "Your appointment for {time} has been cancelled."),
    Reply("hours", None,
          "We are open Monday to Friday, from 8 am to 5 pm."),
]
