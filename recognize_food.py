"""
Recognize a specific type of food from an image and show
its glycemic impact category.
"""

import csv
import sys
from pathlib import Path

from PIL import Image
from transformers import pipeline

MODEL_NAME = "nateraw/food" #Vision model fine-tuned on Food-101
CATEGORIES_FILE = "food_categories.csv"
TOP_K = 3 #number of predictions to show

def load_categories(path=CATEGORIES_FILE):
    """Read the CSV into a dict: food name -> row (gi, category, source)."""
    categories = {}
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            categories[row["food"]] = row
    return categories


def classify(classifier, image_path, top_k=TOP_K):
    """Return a list of (label, score) predictions for one photo."""
    image = Image.open(image_path).convert("RGB")
    results = classifier(image, top_k=top_k)
    return [(result["label"], result["score"]) for result in results]

def main():
    #The photo path comes from the command line
    if len(sys.argv) < 2:
        print("Usage: python recognize_food.py <path_to_photo>")
        return 1

    image_path = Path(sys.argv[1])
    if not image_path.exists():
        print(f"File not found: {image_path}")
        return 1

    print("Loading model...")
    classifier = pipeline("image-classification", model = MODEL_NAME)
    categories = load_categories()

    predictions = classify(classifier, image_path)

    print(f"\nResults for {image_path.name}:")
    for label, score in predictions:
        print(f" {label:<25} {score:6.1%}")

    #Lookup the most likely type of food in the table
    best_label, _ = predictions[0]
    info = categories.get(best_label)
    if info is None:
        print(f"\n{best_label}: not in the table (yet).")
    else:
        print(f"\n{best_label}: GI {info['gi']} -> {info['category']}")

    return 0

if __name__ == "__main__":
    sys.exit(main())

