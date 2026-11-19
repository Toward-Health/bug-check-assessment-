import argparse

from groundbot.bot import answer, ranked_replies
from groundbot.records import load_appointment


def main() -> None:
    parser = argparse.ArgumentParser(prog="groundbot", description="Ask the clinic bot a question.")
    parser.add_argument("message", help="what the patient wrote")
    parser.add_argument("--patient", default="p-001", help="p-001, p-002 or p-003 (made-up patients)")
    parser.add_argument("--scores", action="store_true", help="show the cosine similarity of every reply")
    args = parser.parse_args()

    appointment = load_appointment(args.patient)
    print(f"record: {appointment.patient_id} status={appointment.status} time={appointment.time}")
    if args.scores:
        for score, text in ranked_replies(args.message, appointment):
            print(f"  {score:.3f}  {text}")
    print(f"bot: {answer(args.message, appointment)}")


if __name__ == "__main__":
    main()
