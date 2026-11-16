#!/usr/bin/env python3
"""Count word frequencies in text."""
import csv
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


def ngrams(text, n=2):
    if n < 1:
        raise ValueError("n must be at least 1")
    words = tokenize(text)
    return [tuple(words[index:index + n]) for index in range(len(words) - n + 1)]


def top_ngrams(text, n=2, limit=10):
    if limit < 1:
        raise ValueError("limit must be at least 1")
    counts = {}
    for gram in ngrams(text, n):
        key = " ".join(gram)
        counts[key] = counts.get(key, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def remove_stopwords(words):
    return [word for word in words if word not in STOPWORDS]


def top_content_words(text, limit=10):
    """Return top words after removing common stopwords."""
    if limit < 1:
        raise ValueError("limit must be at least 1")
    counts = {}
    for word in remove_stopwords(tokenize(text)):
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def export_csv(text, path, limit=10, content_only=False):
    """Write top words and counts to a CSV file."""
    if limit < 1:
        raise ValueError("limit must be at least 1")
    words = top_content_words(text, limit) if content_only else top_words(text, limit)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["word", "count"])
        for word, count in words:
            writer.writerow([word, count])
    return path
