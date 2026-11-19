import pytest

from groundbot.vectors import TfidfIndex


def test_identical_text_has_similarity_one():
    index = TfidfIndex(["we have confirmed your appointment"])
    assert index.scores("we have confirmed your appointment") == [pytest.approx(1.0)]


def test_text_with_no_shared_words_has_similarity_zero():
    index = TfidfIndex(["we are open from eight"])
    assert index.scores("headache") == [0.0]
