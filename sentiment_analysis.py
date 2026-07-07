from pathlib import Path

import pandas as pd


CSV_PATH = Path("reviews.csv")


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


def main() -> None:
    reviews_df = load_reviews(CSV_PATH)
    print(reviews_df.head())


if __name__ == "__main__":
    main()
