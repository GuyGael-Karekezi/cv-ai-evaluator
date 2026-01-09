import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Reliable text extraction using pdfplumber only.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        raise ValueError("No extractable text found in PDF")

    return text
