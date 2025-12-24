# feature_engineering/field_detector.py

def detect_field(features):
    """
    Detect dominant field (AI, IT, ECE) based on extracted features.
    Returns (field_name, confidence_dict)
    """

    scores = {
        "AI": 0,
        "IT": 0,
        "ECE": 0
    }

    # -------------------------
    # AI signals
    # -------------------------
    scores["AI"] += features["ai"] * 3
    scores["AI"] += features["has_research"] * 3
    scores["AI"] += features["has_publication"] * 4
    scores["AI"] += features["has_conference"] * 3
    scores["AI"] += features["frameworks"] * 2

    # -------------------------
    # IT signals
    # -------------------------
    scores["IT"] += features["programming"] * 2
    scores["IT"] += features["tools"] * 3
    scores["IT"] += features["has_deployment"] * 3
    scores["IT"] += features["num_projects"] * 2
    scores["IT"] += features["has_leadership"] * 2

    # -------------------------
    # ECE signals
    # -------------------------
    scores["ECE"] += features["programming"] * 1
    scores["ECE"] += features["tools"] * 1
    scores["ECE"] += features["has_research"] * 1

    # Embedded / hardware indicators are implicit in ontology hits
    # (captured in programming + tools + project text)

    # -------------------------
    # Select best field
    # -------------------------
    detected_field = max(scores, key=scores.get)

    return detected_field, scores
