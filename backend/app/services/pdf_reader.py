import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text.
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"

        document.close()

    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")

    return text