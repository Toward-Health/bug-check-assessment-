# Clinic front-desk bot (practice exercise)

A made-up clinic has a small bot that answers patients' messages. It may only say sentences the clinic
approved (`groundbot/replies.py`). To pick one, it turns the patient's message and every approved sentence
into word-count vectors and returns the sentence with the highest **cosine similarity**.

The facts about each patient's appointment live in the clinic's record (`data/appointments.json`).
Everything here is made up: no real patients, no keys, no network, no dependencies except pytest.

```bash
python -m groundbot "Have you confirmed my 3 pm appointment?"             # patient p-001
python -m groundbot "When are you open?" --patient p-002 --scores         # also shows every cosine score
python -m pip install pytest
python -m pytest
```

## Two reports from the front desk

1. A patient whose appointment was only *requested* asked whether it was confirmed. The bot answered
   "Yes, we have confirmed your appointment." Another patient wrote "I did not get a confirmation" and got
   the same answer.
2. A patient wrote that they had the worst headache of their life and asked to be fitted in at 3 pm. The bot
   answered with the clinic's opening hours.

The tests show the behaviour the clinic expects. Some of them fail today.

## The task (about 30 minutes; you are not expected to finish)

1. Fork this repository and clone **your fork**.
2. Create a branch, for example `fix/<short-name>`.
3. Find out why the bot gets these wrong and fix it. Keep the change focused.
   Be ready to say *why* cosine similarity could not get these right, and what the bot should rely on instead.
4. Keep the tests meaningful. Add tests where you think they are missing.
5. Commit with a clear message.
6. Push your branch and open a **pull request** into this repository. In the description say what was wrong,
   what you changed, how you checked it, and what you would still worry about.

Use any tools you normally use, including AI assistants, and tell us how you used them.
We care about how you reason and work, not only about the result.

The tests are expected to fail on `main`, so the `tests` check will be red until a fix is merged.
Do not add real patient data or personal information anywhere.
