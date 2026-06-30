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
pre-commit run pyupgrade --all-files
mypy backend
bandit -r backend -ll
semgrep --config=auto --error --quiet backend
vulture backend
```

Pre-commit runs formatting, modernization, security, and type-checking hooks. Install it once per checkout with `pre-commit install`, then run the full hook set with:

```bash
pre-commit run --all-files
```

## Release tags

Create annotated semantic version tags for releases, keeping the tag aligned with pyproject.toml.

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## Reporting issues

Include the operating system, Python version, steps to reproduce, expected behavior, and actual behavior.

## Code of conduct

Please follow the standards described in CODE_OF_CONDUCT.md.

