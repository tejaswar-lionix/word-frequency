#!/usr/bin/env python3
"""Count word frequencies in text."""
import re

STOPWORDS = frozenset(
    {
        "a", "an", "and", "are", "as", "at", "be", "but", "by", "for",
        "from", "has", "have", "he", "in", "is", "it", "its", "of", "on",
        "that", "the", "to", "was", "were", "will", "with", "you", "your",
    }
)
WORD_PATTERN = re.compile(r"[a-z0-9']+")


def tokenize(text):
    return WORD_PATTERN.findall(text.lower())


def count_words(text):
    counts = {}
    for word in tokenize(text):
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(text, limit=10):
    if limit < 1:
        raise ValueError("limit must be at least 1")
    counts = count_words(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def remove_stopwords(words):
    return [word for word in words if word not in STOPWORDS]
