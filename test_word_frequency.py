import unittest

from word_frequency import (
    count_words,
    ngrams,
    remove_stopwords,
    tokenize,
    top_ngrams,
    top_words,
)


class FrequencyTests(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(tokenize("Hello, WORLD! it's fine."), ["hello", "world", "it's", "fine"])

    def test_count_words(self):
        self.assertEqual(count_words("go go stop"), {"go": 2, "stop": 1})

    def test_top_words_orders_by_count_then_name(self):
        text = "beta alpha beta alpha gamma"
        self.assertEqual(top_words(text, 2), [("alpha", 2), ("beta", 2)])

    def test_top_words_validates_limit(self):
        with self.assertRaises(ValueError):
            top_words("anything", 0)

    def test_remove_stopwords(self):
        self.assertEqual(remove_stopwords(["the", "cat", "is", "here"]), ["cat", "here"])


class NgramTests(unittest.TestCase):
    def test_bigrams(self):
        self.assertEqual(
            ngrams("the cat sat"),
            [("the", "cat"), ("cat", "sat")],
        )

    def test_trigram_counts(self):
        self.assertEqual(
            top_ngrams("the cat sat the cat sat", 3),
            [("the cat sat", 2), ("cat sat the", 1), ("sat the cat", 1)],
        )

    def test_top_ngrams_ranking_and_tie_break(self):
        text = "a b c a b c a b d"
        self.assertEqual(
            top_ngrams(text, 2, 2),
            [("a b", 3), ("b c", 2)],
        )

    def test_ngram_validates_n(self):
        with self.assertRaises(ValueError):
            ngrams("text", 0)
        with self.assertRaises(ValueError):
            top_ngrams("text", 0)

    def test_short_text_returns_empty(self):
        self.assertEqual(ngrams("one"), [])
        self.assertEqual(top_ngrams("one"), [])


class ContentWordsTests(unittest.TestCase):
    def test_top_content_words_filters_stopwords(self):
        from word_frequency import top_content_words

        text = "the cat and the dog and the bird"
        self.assertEqual(
            top_content_words(text, 3),
            [("bird", 1), ("cat", 1), ("dog", 1)],
        )

    def test_top_content_words_validation(self):
        from word_frequency import top_content_words

        with self.assertRaises(ValueError):
            top_content_words("text", 0)


if __name__ == "__main__":
    unittest.main()
