import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.

    - Removes extra spaces
    - Removes extra blank lines
    - Removes tabs
    """

    if not text:
        return ""

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove multiple spaces
    text = re.sub(r" +", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n\s*\n", "\n", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text