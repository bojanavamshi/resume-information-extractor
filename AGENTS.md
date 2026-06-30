# AGENTS.md

## Project Overview

Resume Information Extractor is a FastAPI-based service that accepts uploaded resumes, extracts candidate information, and returns structured JSON data.

## Responsibilities

### Backend

- Maintain the FastAPI upload endpoint and service modules.
- Keep parsing logic modular and testable.
- Ensure security, input validation, and resilient error handling.

### Frontend

- Keep the upload experience simple and reliable.
- Present extracted results in a clear way.
- Ensure the UI works with the API contract.

### Testing

- Add regression tests for parsing and formatting behavior.
- Keep coverage above the configured threshold.
- Validate new changes through local and CI quality checks.

### Documentation

- Keep the README, manual, and contribution docs current.
- Document installation, API usage, troubleshooting, and security practices.

## Workflow

1. Create a feature branch.
2. Implement the change.
3. Add or update tests.
4. Run the local checks.
5. Open a merge request with evidence from CI.

## Coding expectations

- Follow PEP 8 and Ruff formatting.
- Prefer small, typed functions.
- Keep dependencies explicit and pinned where practical.
- Document new configuration or environment changes.

