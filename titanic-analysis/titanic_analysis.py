"""
Titanic Dataset - Exploratory Data Analysis with Pandas
=======================================================
Assignment 6: load, explore, filter, aggregate and clean the Titanic dataset.

Usage:
    1. Download Titanic-Dataset.csv and place it in a `data/` folder
       next to this script (or pass a different path as an argument).
    2. Run:  python titanic_analysis.py
       or:   python titanic_analysis.py path/to/Titanic-Dataset.csv
"""

import sys
from pathlib import Path

import pandas as pd

DATA_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/Titanic-Dataset.csv")
OUTPUT_PATH = Path("titanic_copy.csv")


def section(title: str) -> None:
    """Print a section heading."""
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# ---------------------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)

# ---------------------------------------------------------------------------
# 2. Dataset overview
# ---------------------------------------------------------------------------
section("Shape (rows, columns)")
print(df.shape)

section("Column Names")
print(list(df.columns))

section("Data Types")
print(df.dtypes)

section("Statistical Summary")
print(df.describe())

section("First Five Rows")
print(df.head())

section("Last Five Rows")
print(df.tail())

section("Dataset Information")
df.info()

# ---------------------------------------------------------------------------
# 3. Basic analysis
# ---------------------------------------------------------------------------
section("Passenger Names (first 5)")
print(df["Name"].head())

section("Passengers by Class")
print(df["Pclass"].value_counts().sort_index())

section("Average Age")
print(df["Age"].mean())

section("Highest Fare")
print(df["Fare"].max())

section("Average Fare")
print(df["Fare"].mean())

# ---------------------------------------------------------------------------
# 4. Filtering
# ---------------------------------------------------------------------------
section("Passengers Older Than 60")
print(df[df["Age"] > 60])

section("Passengers Who Survived (first 5)")
print(df[df["Survived"] == 1][["Name", "Sex", "Age"]].head())

# ---------------------------------------------------------------------------
# 5. Aggregation and grouping
# ---------------------------------------------------------------------------
section("Survival Counts")
print(df["Survived"].value_counts())

section("Survival Rate by Gender")
print(df.groupby("Sex")["Survived"].mean())

section("Top 10 Highest Fares")
print(df.sort_values("Fare", ascending=False)[["Name", "Fare"]].head(10))

section("Average Age by Gender")
print(df.groupby("Sex")["Age"].mean())

section("Passengers by Embarkation Port")
print(df["Embarked"].value_counts())

# ---------------------------------------------------------------------------
# 6. Data cleaning
# ---------------------------------------------------------------------------
section("Missing Values (before cleaning)")
print(df.isnull().sum())

# Cabin is ~77% missing, so drop it
df = df.drop(columns=["Cabin"])

# Remove duplicate rows
df = df.drop_duplicates()
print("\nDuplicate rows removed")

# Fill missing values: mean for numeric columns, mode for categorical columns
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
print("Missing values handled")

section("Missing Values (after cleaning)")
print(df.isnull().sum())

# ---------------------------------------------------------------------------
# 7. Save the cleaned dataset
# ---------------------------------------------------------------------------
df.to_csv(OUTPUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUTPUT_PATH}")
