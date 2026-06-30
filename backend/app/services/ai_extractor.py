import re

import spacy

# Load spaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = spacy.blank("en")


SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "MySQL",
    "MongoDB",
    "React",
    "Node.js",
    "Flask",
    "FastAPI",
    "Django",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Artificial Intelligence",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "OpenCV",
]


def extract_resume_data(text: str) -> dict:  # pylint: disable=too-many-branches,too-many-locals
    data = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": [],
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": [],
    }

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    lower_text = text.lower()

    # ---------------- NAME ----------------
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            if "\n" not in name and len(name.split()) <= 5:  # avoid long junk matches
                data["name"] = name
                break

    if not data["name"] and lines:
        for line in lines[:5]:
            if not any(
                x in line.lower()
                for x in ["email", "phone", "skills", "experience", "project", "education"]
            ):
                data["name"] = line
                break

    # ---------------- EMAIL ----------------
    email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if email_match:
        data["email"] = email_match.group()

    # ---------------- PHONE ----------------
    phone_match = re.search(r"(?:\+91[- ]?)?[6-9]\d{9}", text)
    if phone_match:
        data["phone"] = phone_match.group()

    # ---------------- SKILLS ----------------
    found_skills = {skill for skill in SKILLS if skill.lower() in lower_text}
    data["skills"] = sorted(found_skills)

    # ---------------- EDUCATION ----------------
    education_keywords = [
        "b.tech",
        "b.e",
        "bachelor",
        "m.tech",
        "m.e",
        "master",
        "degree",
        "intermediate",
        "ssc",
        "10th",
        "12th",
    ]

    data["education"] = [
        line for line in lines if any(k in line.lower() for k in education_keywords)
    ]

    # ---------------- EXPERIENCE ----------------
    data["experience"] = _extract_section(
        lines, "experience", stop_words=["projects", "education", "skills"]
    )

    # ---------------- PROJECTS ----------------
    data["projects"] = _extract_section(
        lines, "project", stop_words=["experience", "education", "skills"]
    )

    # ---------------- CERTIFICATIONS ----------------
    certs = []
    capture = False

    for line in lines:
        low = line.lower()

        if "certification" in low:
            capture = True
            parts = line.split(":", 1)
            if len(parts) > 1:
                certs.append(parts[1].strip())
            continue

        if capture:
            if any(x in low for x in ["experience", "projects", "education", "skills"]):
                break
            certs.append(line)

    data["certifications"] = certs

    return data


# ---------------- HELPER FUNCTION ----------------
def _extract_section(lines, start_keyword, stop_words):
    capture = False
    section = []

    for line in lines:
        low = line.lower()

        if start_keyword in low:
            capture = True
            parts = line.split(":", 1)
            if len(parts) > 1 and parts[1].strip():
                section.append(parts[1].strip())
            continue

        if capture:
            if any(word in low for word in stop_words):
                break
            section.append(line)

    return section
