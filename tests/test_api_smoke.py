import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from main import app  # noqa: E402


client = TestClient(app)


def test_home_endpoint_returns_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Resume Information Extractor API is Running"
