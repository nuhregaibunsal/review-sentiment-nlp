# i2i Academy NLP - Sentiment Analysis

Sentiment analysis pipeline for English product reviews using Pandas and TextBlob. It cleans the text, scores polarity, and labels each review as Positive, Negative, or Neutral.

## Features

- Loads reviews from a CSV file (with a built-in mock fallback so it runs out-of-the-box)
- Text preprocessing: lowercasing, punctuation removal, and stop-word filtering
- Sentiment scoring with the pre-trained TextBlob library
- Positive / Negative / Neutral labeling based on polarity thresholds
- Prints the final sentiment distribution

## Installation

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

## Usage

```bash
python sentiment_analysis.py
```

## Tech Stack

- Python
- Pandas
- TextBlob
