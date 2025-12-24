# main.py

from data.sample_cvs import SAMPLE_CVS
from preprocessing.cleaner import clean_text
from feature_engineering.extractor import extract_features
from scoring.rule_based import compute_score
from modeling.train_model import train_model

feature_rows = []
scores = []

print("\n=== CV AI EVALUATION SYSTEM ===\n")

for cv in SAMPLE_CVS:
    clean = clean_text(cv["text"])
    features = extract_features(clean)
    score = compute_score(features)

    feature_rows.append(features)
    scores.append(score)

    print(f"CV ID: {cv['id']}")
    print("Extracted Features:", features)
    print("Rule-Based Score:", score)
    print("-" * 40)

# Train ML model
model = train_model(feature_rows, scores)

print("\nML Model trained successfully.")
