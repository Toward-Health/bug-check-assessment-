"""Word-count vectors and cosine similarity, written out so the exercise needs no downloads.

A real system would use an embedding model. The idea is the same: text becomes a vector,
and two texts are "close" when the angle between their vectors is small.
"""

import math
import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9']+")


def tokenize(text: str) -> list[str]:
    return _TOKEN.findall(text.lower())


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    """Cosine similarity of two unit-length sparse vectors."""
    return sum(weight * b.get(term, 0.0) for term, weight in a.items())


class TfidfIndex:
    """Scores a query against a fixed list of documents."""

    def __init__(self, documents: list[str]) -> None:
        tokenized = [tokenize(document) for document in documents]
        document_count = len(tokenized)
        containing = Counter(term for tokens in tokenized for term in set(tokens))
        self._idf = {
            term: math.log((1 + document_count) / (1 + count)) + 1.0
            for term, count in containing.items()
        }
        self._vectors = [self._vector(tokens) for tokens in tokenized]

    def _vector(self, tokens: list[str]) -> dict[str, float]:
        weights = {
            term: count * self._idf[term]
            for term, count in Counter(tokens).items()
            if term in self._idf
        }
        norm = math.sqrt(sum(weight * weight for weight in weights.values())) or 1.0
        return {term: weight / norm for term, weight in weights.items()}

    def scores(self, query: str) -> list[float]:
        """Cosine similarity of the query to each document, in document order."""
        query_vector = self._vector(tokenize(query))
        return [cosine(query_vector, vector) for vector in self._vectors]
