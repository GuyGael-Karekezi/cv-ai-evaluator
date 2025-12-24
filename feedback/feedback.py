# feedback/feedback.py

def generate_feedback(features, field="AI"):
    """
    Generate human-readable feedback based on extracted features
    and the detected professional field.
    """

    strengths = []
    weaknesses = []
    suggestions = []

    # -------------------------
    # COMMON FEEDBACK
    # -------------------------
    if features["num_projects"] >= 2:
        strengths.append("Good number of projects demonstrating hands-on experience")
    else:
        weaknesses.append("Limited number of projects")
        suggestions.append("Add more projects to showcase practical skills")

    if features["experience_months"] >= 12:
        strengths.append("Solid practical experience")
    elif features["experience_months"] > 0:
        weaknesses.append("Limited work experience")
        suggestions.append("Highlight internships, research, or practical training")

    if features["degree_level"] >= 2:
        strengths.append("Advanced academic qualification")
    else:
        suggestions.append("Clearly highlight your academic coursework and achievements")

    # -------------------------
    # FIELD-SPECIFIC FEEDBACK
    # -------------------------
    if field == "AI":
        if features["ai"] >= 2:
            strengths.append("Strong AI / machine learning skill set")
        else:
            weaknesses.append("Limited AI-specific skills")
            suggestions.append("Include more AI/ML projects or coursework")

        if features["has_research"]:
            strengths.append("Research experience strengthens your AI profile")

        if features["has_publication"]:
            strengths.append("Publications significantly enhance your academic profile")

    elif field == "IT":
        if features["programming"] >= 2:
            strengths.append("Strong programming foundation")
        else:
            weaknesses.append("Programming skill coverage is limited")
            suggestions.append("Strengthen core programming and software engineering skills")

        if features["tools"] >= 2:
            strengths.append("Good exposure to industry-standard tools and platforms")
        else:
            weaknesses.append("Limited exposure to modern development tools")
            suggestions.append("Add experience with Git, Docker, CI/CD, or cloud platforms")

        if features["has_deployment"]:
            strengths.append("Deployment experience is highly valuable for IT roles")

    elif field == "ECE":
        if features["programming"] >= 2:
            strengths.append("Good embedded / programming background")
        else:
            weaknesses.append("Limited embedded programming exposure")
            suggestions.append("Add hands-on embedded or hardware-related projects")

        if features["has_research"]:
            strengths.append("Research experience strengthens your ECE profile")

    # -------------------------
    # LEADERSHIP & ACADEMICS
    # -------------------------
    if features["has_leadership"]:
        strengths.append("Leadership experience adds strong professional value")

    if features["has_teaching"]:
        strengths.append("Teaching experience reflects strong subject mastery")

    if features["has_thesis"]:
        strengths.append("Thesis work demonstrates depth and independent research ability")

    if not strengths:
        suggestions.append("Consider strengthening both technical and academic sections of your CV")

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }
