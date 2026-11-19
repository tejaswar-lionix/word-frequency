# word-frequency

Count word frequencies and rank the most common words.

## Usage

```bash
python3 -c "from word_frequency import top_words; print(top_words('go go stop'))"
python3 -c "from word_frequency import top_ngrams; print(top_ngrams('the cat sat'))"
python3 -c "from word_frequency import export_csv; print(export_csv('go go stop', 'words.csv'))"
python3 -c "from word_frequency import unique_words; print(unique_words('go go stop'))"
python3 -c "from word_frequency import longest_words; print(longest_words('go stop running'))"
```

## Features

- Lowercase tokenization with punctuation handling
- Frequency ranking with deterministic tie-breaking
- Sorted unique words with unique_words(text)
- N-gram extraction with ngrams(text, n) and top_ngrams(text, n, limit)
- Content ranking with top_content_words(text, limit)
- Longest words with longest_words(text, limit)
- CSV export with export_csv(text, path, limit, content_only)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
