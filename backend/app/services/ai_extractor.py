import re

import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:  # pragma: no cover - depends on local model availability
    nlp = spacy.blank("en")


# Common skills list
SKILLS = [
    "Python", "Java", "C", "C++", "JavaScript", "HTML", "CSS",
    "SQL", "MySQL", "MongoDB", "React", "Node.js", "Flask",
    "FastAPI", "Django", "Git", "GitHub", "Machine Learning",
    "Deep Learning", "Data Science", "Artificial Intelligence",
    "TensorFlow", "PyTorch", "Pandas", "NumPy", "OpenCV"
]


def extract_resume_data(text: str) -> dict[str, list[str] | str]:
    """
    Extract structured resume information.
    """

    data = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": [],
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": []
    }

    # -----------------------------
    # Name
    # -----------------------------
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            candidate = ent.text.strip()
            first_line = next((line.strip() for line in candidate.splitlines() if line.strip()), "")
            if first_line:
                data["name"] = first_line
            break

    if not data["name"]:
        for line in text.splitlines():
            candidate = line.strip()
            lowered = candidate.lower()
            if candidate and not any(
                token in lowered
                for token in ["skills", "education", "experience", "project", "certification", "email", "phone"]
            ):
                data["name"] = candidate
                break

    # -----------------------------
    # Email
    # -----------------------------
    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email:
        data["email"] = email[0]

    # -----------------------------
    # Phone Number
    # -----------------------------
    phone = re.findall(
        r"(?:\+91[- ]?)?[6-9]\d{9}",
        text
    )

    if phone:
        data["phone"] = phone[0]

    # -----------------------------
    # Skills
    # -----------------------------
    lower_text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in lower_text:
            found_skills.append(skill)

    data["skills"] = sorted(list(set(found_skills)))

    # -----------------------------
    # Education
    # -----------------------------
    education_keywords = [
        "B.Tech",
        "B.E",
        "Bachelor",
        "M.Tech",
        "M.E",
        "Master",
        "Degree",
        "Intermediate",
        "SSC",
        "10th",
        "12th"
    ]

    education = []

    for line in text.split("\n"):
        for keyword in education_keywords:
            if keyword.lower() in line.lower():
                education.append(line.strip())

    data["education"] = education

    # -----------------------------
    # Experience
    # -----------------------------
    experience = []

    capture = False

    for line in text.split("\n"):

        if "experience" in line.lower():
            capture = True
            continue

        if capture:

            if line.strip() == "":
                break

            experience.append(line.strip())

    data["experience"] = experience

    # -----------------------------
    # Projects
    # -----------------------------
    projects = []

    capture = False

    for line in text.split("\n"):

        if "project" in line.lower():
            capture = True
            continue

        if capture:

            if line.strip() == "":
                break

            projects.append(line.strip())

    data["projects"] = projects

    # -----------------------------
    # Certifications
    # -----------------------------
    certifications = []

    capture = False

    for line in text.split("\n"):
        normalized = line.strip()

        if "certification" in normalized.lower():
            capture = True
            if ":" in normalized:
                value = normalized.split(":", 1)[1].strip()
                if value:
                    certifications.append(value)
            continue

        if capture:
            if normalized == "" or normalized.lower().startswith("experience"):
                break

            if normalized.lower().startswith("projects") or normalized.lower().startswith("skills"):
                break

            certifications.append(normalized)

    data["certifications"] = certifications

    return data
