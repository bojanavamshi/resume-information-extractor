import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.

    - Removes extra spaces
    - Removes extra blank lines
    - Removes tabs
    - Trims indentation from each line
    """

    if not text:
        return ""

    lines = []
    for raw_line in text.splitlines():
        line = raw_line.replace("\t", " ").strip()
        line = re.sub(r" +", " ", line)
        lines.append(line)

    cleaned = "\n".join(line for line in lines if line)
    return cleaned.strip()
