# word-frequency

Count word frequencies and rank the most common words.

## Usage

```bash
python3 -c "from word_frequency import top_words; print(top_words('go go stop'))"
python3 -c "from word_frequency import top_ngrams; print(top_ngrams('the cat sat'))"
```

## Features

- Lowercase tokenization with punctuation handling
- Frequency ranking with deterministic tie-breaking
- N-gram extraction with ngrams(text, n) and top_ngrams(text, n, limit)
- Content ranking with top_content_words(text, limit)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT
