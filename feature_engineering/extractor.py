# feature_engineering/extractor.py

from ontology.skills import SKILL_ONTOLOGY
from ontology.ece_skills import ECE_SKILLS
from ontology.synonyms import SKILL_SYNONYMS


def skill_present(skill, text):
    """
    Check if a canonical skill or any of its synonyms
    appears in the given text.
    """
    variants = SKILL_SYNONYMS.get(skill, [skill])
    for v in variants:
        if v in text:
            return True
    return False


def extract_features(sections, field="AI"):
    """
    Extract numerical features from resume sections.
    Supports AI and ECE fields.
    Includes academic signals and synonym-aware skill detection.
    """

    # -------------------------------
    # Select correct ontology
    # -------------------------------
    if field == "ECE":
        skill_ontology = ECE_SKILLS
    else:  # default AI
        skill_ontology = SKILL_ONTOLOGY

    # -------------------------------
    # Initialize features
    # -------------------------------
    features = {
        # technical
        "programming": 0,
        "ai": 0,
        "frameworks": 0,
        "tools": 0,

        # projects & experience
        "num_projects": 0,
        "has_deployment": 0,
        "experience_months": 0,

        # education
        "degree_level": 1,  # default: Bachelor

        # academic signals
        "has_research": 0,
        "has_publication": 0,
        "has_thesis": 0,
        "has_teaching": 0,
        "has_conference": 0,
        "has_leadership": 0,
    }

    # -------------------------------
    # Extract & normalize text
    # -------------------------------
    skills_text = sections.get("skills", "").lower()
    projects_text = sections.get("projects", "").lower()
    experience_text = sections.get("experience", "").lower()
    education_text = sections.get("education", "").lower()

    combined_text = (
        skills_text + " " +
        projects_text + " " +
        experience_text + " " +
        education_text
    )

    # -------------------------------
    # SKILL MATCHING (synonym-aware)
    # -------------------------------
    for category, skills in skill_ontology.items():
        matched = set()  # prevent double counting
        for skill in skills:
            if skill_present(skill, combined_text):
                matched.add(skill)
        if category in features:
            features[category] += len(matched)

    # -------------------------------
    # PROJECT FEATURES
    # -------------------------------
    features["num_projects"] = projects_text.count("project")

    if any(k in projects_text for k in ["deploy", "deployment", "docker"]):
        features["has_deployment"] = 1

    # -------------------------------
    # EXPERIENCE ESTIMATION
    # -------------------------------
    if "1 year" in experience_text:
        features["experience_months"] = 12
    elif "6 months" in experience_text:
        features["experience_months"] = 6

    # -------------------------------
    # EDUCATION LEVEL
    # -------------------------------
    if any(k in education_text for k in ["msc", "master"]):
        features["degree_level"] = 2
    elif "phd" in education_text:
        features["degree_level"] = 3

    # -------------------------------
    # ACADEMIC SIGNALS (synonym-aware)
    # -------------------------------
    if any(k in combined_text for k in [
        "research", "research assistant", "research intern", "lab"
    ]):
        features["has_research"] = 1

    if any(k in combined_text for k in [
        "publication", "paper", "journal", "conference", "proceedings"
    ]):
        features["has_publication"] = 1

    if any(k in combined_text for k in [
        "thesis", "dissertation"
    ]):
        features["has_thesis"] = 1

    if any(k in combined_text for k in [
        "teaching assistant", "ta", "instructor"
    ]):
        features["has_teaching"] = 1

    if any(k in combined_text for k in [
        "neurips", "icml", "iclr", "cvpr", "eccv", "aaai"
    ]):
        features["has_conference"] = 1

    if any(k in combined_text for k in [
        "lead", "leader", "chair", "president", "coordinator"
    ]):
        features["has_leadership"] = 1

    return features
