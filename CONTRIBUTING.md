# Contributing Guide

Thank you for contributing to the Resume Information Extractor project.

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pre-commit install
```

## Workflow

1. Create a branch for your change.
2. Implement the feature or fix.
3. Add or update tests where appropriate.
4. Run the local quality checks.
5. Open a merge request with a clear summary.

## Quality checks

Run the following before submitting changes:

```bash
pytest
ruff check backend tests
ruff format --check backend tests
mypy backend
bandit -r backend -ll
```

## Reporting issues

Include the operating system, Python version, steps to reproduce, expected behavior, and actual behavior.

## Code of conduct

Please follow the standards described in CODE_OF_CONDUCT.md.

