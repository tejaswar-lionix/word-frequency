import unittest

from word_frequency import count_words, remove_stopwords, tokenize, top_words


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


if __name__ == "__main__":
    unittest.main()
