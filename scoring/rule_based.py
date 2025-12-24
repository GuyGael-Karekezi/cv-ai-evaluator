def normalize(value, cap):
    return min(value / cap, 1.0)


def compute_score(features):
    # --- normalization ---
    ai_norm = normalize(features["ai"], 3)
    prog_norm = normalize(features["programming"], 3)
    proj_norm = normalize(features["num_projects"], 2)
    exp_norm = normalize(features["experience_months"], 24)
    deg_norm = normalize(features["degree_level"], 3)

    academic_norm = normalize(
        features["has_research"]
        + features["has_publication"]
        + features["has_thesis"]
        + features["has_teaching"]
        + features["has_conference"],
        3
    )

    # --- weighted score (0–1) ---
    raw_score = (
        0.25 * ai_norm +
        0.20 * prog_norm +
        0.20 * proj_norm +
        0.20 * academic_norm +
        0.15 * deg_norm
    )

    # --- calibration ---
    final_score = 30 + 70 * raw_score

    return round(final_score, 1)
