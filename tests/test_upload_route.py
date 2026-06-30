import sys
from pathlib import Path

import fitz
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from main import app  # noqa: E402

from app.services.pdf_reader import extract_text_from_pdf  # noqa: E402

client = TestClient(app)


def test_upload_rejects_non_pdf() -> None:
    response = client.post(
        "/resume/upload",
        files={"file": ("sample.txt", b"not a pdf", "text/plain")},
    )

    assert response.status_code == 400
    assert "Only PDF files are allowed" in response.text


def test_extract_text_from_pdf_reads_content(tmp_path: Path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Sample Resume Content")
    document.save(pdf_path)
    document.close()

    text = extract_text_from_pdf(str(pdf_path))

    assert "Sample Resume Content" in text


def test_upload_accepts_pdf(tmp_path: Path) -> None:
    pdf_path = tmp_path / "resume.pdf"
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Jane Doe\nPython\nFastAPI")
    document.save(pdf_path)
    document.close()

    with pdf_path.open("rb") as handle:
        response = client.post(
            "/resume/upload",
            files={"file": ("resume.pdf", handle.read(), "application/pdf")},
        )

    assert response.status_code == 200
    assert response.json()["status"] == "success"
