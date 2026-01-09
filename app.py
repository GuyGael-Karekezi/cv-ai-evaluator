import streamlit as st

# --- field detection ---
from feature_engineering.field_detector import detect_field

# --- preprocessing ---
from preprocessing.pdf_parser import extract_text_from_pdf
from preprocessing.cleaner import clean_text
from preprocessing.section_detector import extract_sections

# --- feature engineering ---
from feature_engineering.extractor import extract_features

# --- scoring & feedback ---
from scoring.rule_based import compute_score
from feedback.feedback import generate_feedback


# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="AI-Powered CV Evaluation System", layout="centered")

st.title("AI-Powered CV Evaluation System")
st.write(
    "Upload your CV in PDF format to receive an explainable AI-based evaluation, "
    "including field detection, scoring, and personalized feedback."
)

uploaded_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])

manual_field = st.selectbox(
    "Select Field (optional override)",
    ["Auto", "AI", "IT", "ECE"]
)

# -------------------------------
# PIPELINE
# -------------------------------
if uploaded_file is not None:
    try:
        # Save uploaded PDF temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # --- Text processing ---
        raw_text = extract_text_from_pdf("temp.pdf")

        if not raw_text or len(raw_text.strip()) < 50:
           st.error(
                     "Unable to extract enough text from this PDF. "
                     "Please ensure the CV contains selectable text."
    )
          st.stop()

        cleaned_text = clean_text(raw_text)
        sections = extract_sections(cleaned_text)

        # --- Initial feature extraction (neutral baseline) ---
        base_features = extract_features(sections, field="AI")

        # --- Auto-detect field ---
        detected_field, field_scores = detect_field(base_features)

        # --- Decide final field ---
        final_field = detected_field if manual_field == "Auto" else manual_field

        # --- Re-extract features using final field ontology ---
        features = extract_features(sections, field=final_field)

        # --- Scoring & feedback ---
        score = compute_score(features)
        feedback = generate_feedback(features, field=final_field)

        # -------------------------------
        # OUTPUT
        # -------------------------------
        st.subheader("Detected Field")
        st.write(f"**{final_field}**")

        with st.expander("Field confidence details"):
            st.write(field_scores)

        st.subheader(f"Overall Score: {score}/100")

        st.subheader("Strengths")
        for s in feedback.get("strengths", []):
            st.write("✔️", s)

        st.subheader("Weaknesses")
        for w in feedback.get("weaknesses", []):
            st.write("⚠️", w)

        st.subheader("Suggestions")
        for sug in feedback.get("suggestions", []):
            st.write("➡️", sug)

        with st.expander("Extracted features (debug)"):
            st.write(features)

    except Exception:
        # -------------------------------
        # GRACEFUL FAILURE (NO CRASH)
        # -------------------------------
        st.error(
            "⚠️ Unable to process this PDF.\n\n"
            "Please upload a **text-based CV** (not a scanned image).\n"
            "If the issue persists, try exporting your CV directly from Word or LaTeX."
        )
