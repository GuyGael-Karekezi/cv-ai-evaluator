# AI-Powered CV Evaluation System

An explainable AI system that analyzes CVs (PDF format), detects the professional field, evaluates skills and experience, and provides personalized feedback through a web-based interface.

This project is designed for **educational, research, and portfolio purposes**, focusing on transparency and human-centered AI rather than black-box models.

---

## 🔍 What the System Does

- Parses CVs in **PDF format**
- Automatically detects the candidate’s **professional field** (AI, IT, or ECE)
- Extracts skills using a **synonym-aware ontology**
- Identifies academic and industry signals (projects, research, publications, leadership)
- Computes an **explainable score (0–100)**
- Generates **human-readable feedback**:
  - Strengths
  - Weaknesses
  - Suggestions for improvement

---

## 🧠 Key Features

- 📄 PDF CV parsing
- 🧹 Text cleaning and section detection
- 🧩 Synonym-aware skill extraction
- 🏷️ Automatic field detection with manual override
- 📊 Rule-based, explainable scoring
- 💬 Field-aware feedback generation
- 🌐 Interactive web app built with Streamlit

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **Techniques:**  
  - Rule-based AI  
  - NLP preprocessing  
  - Ontology-driven feature extraction  
  - Explainable decision logic  

---

## 📂 Project Structure

```

cv_ai_project/
├── app.py                  # Streamlit application
├── requirements.txt        # Project dependencies
├── preprocessing/          # PDF parsing, cleaning, section detection
├── feature_engineering/    # Feature extraction and field detection
├── ontology/               # Skill ontologies and synonyms
├── scoring/                # Rule-based scoring logic
├── feedback/               # Feedback generation
├── tests/                  # Synthetic CV tests
└── .gitignore

````

---

## ▶️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/GuyGael-Karekezi/cv-ai-evaluator.git
   cd cv-ai-evaluator
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open the browser at:

   ```
   http://localhost:8501
   ```

---

## ⚠️ Disclaimer

This tool is intended for **educational and research use only**.
It does **not** replace human recruiters, hiring managers, or official academic evaluation processes.

---

## 👤 Authors

**Ishimwe Karekezi Guy Gael**
AI Student, Carnegie Mellon University Africa

**Iradukunda Kevin Jonathan** 
ECE Student, Carnegie Mellon University Africa

* Email: [iguygael@andrew.cmu.edu](mailto:iguygael@andrew.cmu.edu)
* LinkedIn: [https://www.linkedin.com/in/guy-gael-891895367](https://www.linkedin.com/in/guy-gael-891895367)

