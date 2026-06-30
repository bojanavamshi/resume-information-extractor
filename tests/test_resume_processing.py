import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.__init__ import create_app  # noqa: E402
from app.models.resume_model import ResumeData  # noqa: E402
from app.services.ai_extractor import extract_resume_data  # noqa: E402
from app.services.json_formatter import format_resume_data  # noqa: E402
from app.services.text_cleaner import clean_text  # noqa: E402


def test_clean_text_normalizes_whitespace() -> None:
    raw_text = "John   Doe\n\n\tEmail: john@example.com"

    cleaned = clean_text(raw_text)

    assert cleaned == "John Doe\nEmail: john@example.com"


def test_extract_resume_data_recognizes_common_fields() -> None:
    sample_text = """
    John Doe
    john.doe@example.com
    +91 9876543210
    Skills: Python, FastAPI, SQL
    Education: B.Tech Computer Science
    Experience: 3 years in software engineering
    Projects: Resume parser for recruiters
    Certifications: AWS Certified Developer
    """

    data = extract_resume_data(sample_text)

    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"
    assert data["phone"] == "+91 9876543210"
    assert "Python" in data["skills"]
    assert "FastAPI" in data["skills"]
    assert any("B.Tech" in item for item in data["education"])
    assert data["experience"]
    assert data["projects"]
    assert data["certifications"]


def test_format_resume_data_builds_pydantic_model() -> None:
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "+91 9123456789",
        "skills": ["Python", "SQL"],
        "education": ["B.Tech Computer Science"],
        "experience": ["2 years"],
        "projects": ["Internal analytics portal"],
        "certifications": ["PMP"],
    }

    model = format_resume_data(payload)

    assert isinstance(model, ResumeData)
    assert model.name == "Jane Doe"
    assert model.skills == ["Python", "SQL"]


def test_clean_text_handles_empty_input() -> None:
    assert clean_text("") == ""


def test_extract_resume_data_parses_certification_values() -> None:
    sample_text = """
    Jane Doe
    Certifications: AWS Certified Developer
    Experience: Two years
    """

    data = extract_resume_data(sample_text)

    assert data["name"] == "Jane Doe"
    assert data["certifications"] == ["AWS Certified Developer"]


def test_create_app_builds_flask_app() -> None:
    app = create_app()

    assert app.config["SECRET_KEY"] == "local_secret_key"
    assert app.config["UPLOAD_FOLDER"] == "uploads/"
