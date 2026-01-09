import pdfplumber
from pdfminer.high_level import extract_text as pdfminer_extract_text


def extract_text_from_pdf(pdf_path):
    """
    Robust PDF text extraction with fallback.
    - First tries pdfplumber (better layout)
    - Falls back to pdfminer if pdfplumber crashes
    """

    # ---------- Attempt 1: pdfplumber ----------
    try:
        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)
                except Exception:
                    # Skip problematic page
                    continue

        text = "\n".join(text_parts)
        if text.strip():
            return text

    except Exception:
        pass

    # ---------- Attempt 2: pdfminer fallback ----------
    try:
        text = pdfminer_extract_text(pdf_path)
        if text and text.strip():
            return text
    except Exception:
        pass

    # ---------- If everything fails ----------
    raise ValueError(
        "PDF text extraction failed using both pdfplumber and pdfminer."
    )
