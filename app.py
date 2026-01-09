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
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI-Powered CV Evaluation System",
    layout="centered"
)

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
        # Save uploaded file
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # --- PDF text extraction ---
        raw_text = extract_text_from_pdf("temp.pdf")

        # --- SAFER VALIDATION (CLOUD-FRIENDLY) ---
        compact_text = raw_text.replace("\n", "").replace(" ", "")

        if not raw_text or len(compact_text) < 20:
            st.error(
                "Unable to extract readable text from this PDF.\n\n"
                "The file may use a complex layout. "
                "Please try exporting the CV directly from Word or LaTeX."
            )
            st.stop()

       
        # --- Cleaning & section detection ---
        cleaned_text = clean_text(raw_text)
        sections = extract_sections(cleaned_text)

        # --- Baseline extraction ---
        base_features = extract_features(sections, field="AI")

        # --- Field detection ---
        detected_field, field_scores = detect_field(base_features)

        # --- Final field decision ---
        final_field = detected_field if manual_field == "Auto" else manual_field

        # --- Re-extract with correct ontology ---
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

    except Exception as e:
       st.error("⚠️ Internal error occurred")
       st.exception(e)
