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


class UniqueWordsTests(unittest.TestCase):
    def test_duplicates_removed(self):
        from word_frequency import unique_words

        self.assertEqual(unique_words("go go stop stop stop"), ["go", "stop"])

    def test_sorted_output(self):
        from word_frequency import unique_words

        self.assertEqual(unique_words("gamma alpha beta"), ["alpha", "beta", "gamma"])

    def test_punctuation_and_case_handled(self):
        from word_frequency import unique_words

        self.assertEqual(unique_words("Dog, dog! CAT?"), ["cat", "dog"])

    def test_empty_text_returns_empty_list(self):
        from word_frequency import unique_words

        self.assertEqual(unique_words(""), [])


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


class ExportCsvTests(unittest.TestCase):
    def test_export_writes_header_and_rows(self):
        import csv
        import os
        import tempfile

        from word_frequency import export_csv

        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "words.csv")
            result = export_csv("go go stop", path, limit=2)
            self.assertEqual(result, path)
            with open(path, encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
        self.assertEqual(rows[0], ["word", "count"])
        self.assertEqual(rows[1], ["go", "2"])
        self.assertEqual(rows[2], ["stop", "1"])

    def test_export_content_only_excludes_stopwords(self):
        import csv
        import os
        import tempfile

        from word_frequency import export_csv

        text = "the cat and the dog and the bird"
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "words.csv")
            export_csv(text, path, limit=3, content_only=True)
            with open(path, encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
        self.assertEqual(rows[1:], [["bird", "1"], ["cat", "1"], ["dog", "1"]])

    def test_export_validates_limit(self):
        from word_frequency import export_csv

        with self.assertRaises(ValueError):
            export_csv("text", "unused.csv", limit=0)


if __name__ == "__main__":
    unittest.main()
