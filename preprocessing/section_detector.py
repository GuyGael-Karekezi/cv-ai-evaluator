import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills"],
    "projects": ["projects", "academic projects"],
    "experience": ["experience", "work experience"],
    "education": ["education"],
    "certifications": ["certifications"]
}

def extract_sections(text):
    sections = {}
    text = text.lower()

    for section, keywords in SECTION_HEADERS.items():
        pattern = "|".join(keywords)
        match = re.search(pattern, text)
        if match:
            start = match.end()
            sections[section] = text[start:start+1500]
        else:
            sections[section] = ""

    return sections
