import string
from pathlib import Path

import pandas as pd
from textblob import TextBlob


CSV_PATH = Path("reviews.csv")

POSITIVE_THRESHOLD = 0.1
NEGATIVE_THRESHOLD = -0.1

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "is", "are", "was",
    "were", "be", "been", "being", "to", "of", "in", "on", "at", "for", "with",
    "this", "that", "these", "those", "it", "its", "as", "by", "from", "i",
    "you", "he", "she", "we", "they", "my", "your", "our", "their", "me",
}


def build_mock_reviews() -> pd.DataFrame:
    mock_reviews = [
        "This product is absolutely fantastic and exceeded my expectations!",
        "Terrible quality, it broke after just one day. Very disappointed.",
        "The item arrived on time and works as described.",
        "I love it! Best purchase I have made all year.",
        "Awful customer service and the product never worked.",
        "It is okay, nothing special but does the job.",
        "Highly recommend this to anyone, superb value for money.",
        "Waste of money, completely useless and poorly built.",
        "Decent product, though the packaging could be improved.",
        "Amazing experience from start to finish, five stars!",
        "The color faded quickly and the material feels cheap.",
        "Neutral feelings about this, it neither impressed nor disappointed me.",
    ]
    return pd.DataFrame({"review": mock_reviews})


def load_reviews(csv_path: Path) -> pd.DataFrame:
    if csv_path.exists():
        reviews_df = pd.read_csv(csv_path)
        print(f"Loaded {len(reviews_df)} reviews from '{csv_path}'.")
    else:
        reviews_df = build_mock_reviews()
        print(f"'{csv_path}' not found - using {len(reviews_df)} mock reviews.")
    return reviews_df


def clean_text(raw_text: str) -> str:
    lowercased = raw_text.lower()
    no_punctuation = lowercased.translate(
        str.maketrans("", "", string.punctuation)
    )
    meaningful_words = [
        word for word in no_punctuation.split() if word not in STOP_WORDS
    ]
    return " ".join(meaningful_words)


def calculate_sentiment_score(text: str) -> float:
    return TextBlob(text).sentiment.polarity


def label_sentiment(score: float) -> str:
    if score > POSITIVE_THRESHOLD:
        return "Positive"
    if score < NEGATIVE_THRESHOLD:
        return "Negative"
    return "Neutral"


def run_pipeline(reviews_df: pd.DataFrame) -> pd.DataFrame:
    reviews_df["cleaned_review"] = reviews_df["review"].apply(clean_text)
    reviews_df["sentiment_score"] = reviews_df["review"].apply(
        calculate_sentiment_score
    )
    reviews_df["sentiment_label"] = reviews_df["sentiment_score"].apply(
        label_sentiment
    )
    return reviews_df


def print_distribution(reviews_df: pd.DataFrame) -> None:
    distribution = reviews_df["sentiment_label"].value_counts()

    print("\nSentiment distribution")
    print("-" * 30)
    for label in ("Positive", "Negative", "Neutral"):
        count = int(distribution.get(label, 0))
        print(f"{label:<10}: {count}")
    print("-" * 30)
    print(f"{'Total':<10}: {len(reviews_df)}")


def main() -> None:
    reviews_df = load_reviews(CSV_PATH)
    reviews_df = run_pipeline(reviews_df)
    print_distribution(reviews_df)


if __name__ == "__main__":
    main()
