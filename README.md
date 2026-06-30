# Resume Information Extractor

A production-ready FastAPI service for extracting structured candidate information from uploaded PDF resumes.

## Overview

The Resume Information Extractor helps recruiters and hiring teams automate the first pass of resume review by extracting structured fields such as name, email, phone, skills, education, experience, projects, and certifications from PDF documents.

## Features

- Upload PDF resumes through a REST endpoint
- Extract structured candidate data from raw text
- Return JSON-compatible payloads for downstream systems
- Run locally or in Docker with a containerized API
- Use automated quality gates for formatting, linting, typing, testing, and security

## Project Structure

- backend/: FastAPI application and parsing services
- frontend/: Vite frontend for the upload experience
- tests/: regression tests for parsing and formatting
- specs/: specification, plan, and task documents

## Installation

### Prerequisites

- Python 3.10+
- pip
- Docker (optional)

### Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

### Run the API

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## API Usage

### Upload a resume

```bash
curl -X POST "http://127.0.0.1:8000/resume/upload" -F "file=@sample.pdf"
```

## Development

```bash
pre-commit install
pytest
ruff check backend tests
ruff format --check backend tests
pre-commit run pyupgrade --all-files
mypy backend
```

## Testing

```bash
pytest --cov=backend --cov-report=xml --cov-report=html
```

## Docker

```bash
docker build -t resume-information-extractor:latest .
docker compose up --build
```

## Security

- Review the security policy in SECURITY.md.
- Run Bandit, Semgrep, pip-audit, and Gitleaks in CI and locally.

## Releases and Git Tags

Releases use semantic version tags that match the project version in pyproject.toml, for example v1.0.0.

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

To publish all local tags:

```bash
git push origin --tags
```

## Contributing

See CONTRIBUTING.md for contribution guidelines.

## License

This project is distributed under the AGPL-3.0-or-later license. See LICENSE for details.

