from app.models.resume_model import ResumeData


def format_resume_data(data: dict) -> ResumeData:
    """
    Convert extracted dictionary into ResumeData model.
    """

    return ResumeData(
        name=data.get("name", ""),
        email=data.get("email", ""),
        phone=data.get("phone", ""),
        skills=data.get("skills", []),
        education=data.get("education", []),
        experience=data.get("experience", []),
        projects=data.get("projects", []),
        certifications=data.get("certifications", [])
    )