"""
Titanic Dataset - Data Visualization with Matplotlib
====================================================
Assignment 7: explore the Titanic dataset with bar charts, scatter plots
and a line graph.

Usage:
    1. Download Titanic-Dataset.csv and place it in a `data/` folder
       next to this script (or pass a different path as an argument).
    2. Run:  python titanic_visualization.py
       or:   python titanic_visualization.py path/to/Titanic-Dataset.csv

Every chart is saved as a PNG in the `images/` folder and also displayed.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/Titanic-Dataset.csv")
IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)


def save_and_show(filename: str) -> None:
    """Save the current figure to the images folder, then display it."""
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=150)
    plt.show()


# ---------------------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nData Types:")
print(df.dtypes)
print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------------------------------------------------
# 2. Bar chart: number of passengers in each class
# ---------------------------------------------------------------------------
class_counts = df["Pclass"].value_counts().sort_index()
print("\nPassengers per class:")
print(class_counts)

plt.figure()
plt.bar(class_counts.index, class_counts.values)
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Number of Passengers in Each Class")
plt.xticks([1, 2, 3])
save_and_show("passengers_by_class.png")

# Mean fare of first-class passengers
mean_fare_first = df[df["Pclass"] == 1]["Fare"].mean()
print(f"\nMean fare (1st class): {mean_fare_first:.2f}")

# ---------------------------------------------------------------------------
# 3. Bar chart: survival counts
# ---------------------------------------------------------------------------
survival_counts = df["Survived"].value_counts().sort_index()
print("\nSurvival counts:")
print(survival_counts)

plt.figure()
plt.bar(survival_counts.index, survival_counts.values)
plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")
plt.title("Titanic Passenger Survival")
plt.xticks([0, 1], ["Not Survived", "Survived"])
save_and_show("survival_counts.png")

# ---------------------------------------------------------------------------
# 4. Grouped bar chart: survival by gender
# ---------------------------------------------------------------------------
survival_by_sex = df.groupby(["Survived", "Sex"]).size().unstack()
print("\nSurvival by gender:")
print(survival_by_sex)

survival_by_sex.plot(kind="bar")
plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")
plt.title("Titanic Survival by Gender")
plt.xticks([0, 1], ["Not Survived", "Survived"], rotation=0)
save_and_show("survival_by_gender.png")

# ---------------------------------------------------------------------------
# 5. Scatter plots
# ---------------------------------------------------------------------------
# 5a. Age vs Fare
age_fare = df.dropna(subset=["Age", "Fare"])
plt.figure()
plt.scatter(age_fare["Age"], age_fare["Fare"])
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare in Titanic Dataset")
save_and_show("age_vs_fare.png")

# 5b. Passenger Class vs Fare
class_fare = df.dropna(subset=["Pclass", "Fare"])
plt.figure()
plt.scatter(class_fare["Pclass"], class_fare["Fare"])
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Passenger Class vs Fare")
plt.xticks([1, 2, 3])
plt.grid(True)
save_and_show("class_vs_fare.png")

# 5c. Passenger Class vs Age
class_age = df.dropna(subset=["Pclass", "Age"])
plt.figure()
plt.scatter(class_age["Pclass"], class_age["Age"])
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.title("Passenger Class vs Age")
plt.xticks([1, 2, 3])
plt.grid(True)
save_and_show("class_vs_age.png")

# ---------------------------------------------------------------------------
# 6. Fare outliers: lowest and highest fares
# ---------------------------------------------------------------------------
df_sorted = df.sort_values(by="Fare")

print("\nPassengers with a fare of 0:")
print(df[df["Fare"] == 0])

print("\nTwo highest fares:")
print(df_sorted.tail(2))

# ---------------------------------------------------------------------------
# 7. Line graph: average fare by passenger class
# ---------------------------------------------------------------------------
avg_fare = df.groupby("Pclass")["Fare"].mean()
print("\nAverage fare by class:")
print(avg_fare)

plt.figure()
plt.plot(avg_fare.index, avg_fare.values, marker="o")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.title("Average Fare by Passenger Class")
plt.xticks([1, 2, 3])
plt.grid(True)
save_and_show("avg_fare_by_class.png")

print(f"\nAll charts saved in the '{IMAGES_DIR}/' folder.")
