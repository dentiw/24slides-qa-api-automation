# DummyJSON API Automation - 24Slides Task 2

This repository demonstrates a maintainable API automation framework using Python, Requests, Pytest, JSON Schema, and environment-based configuration. DummyJSON was selected under the assessment's **"or similar"** option because it provides public product resources and a realistic token-based authentication flow without requiring reviewers to create a paid account.

## Coverage

- Successful authentication and token value validation
- Invalid-password handling
- Missing-required-parameter handling
- Invalid-token authorization handling
- Product pagination and response-value validation
- Product search and relevant-value validation
- Unknown-resource handling
- Authenticated profile retrieval
- JSON schema validation for authentication and product collections
- Response-time assertions for multiple endpoints

## Prerequisites

- Python 3.10 or newer

## Setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env`. The checked-in values are credentials published by DummyJSON specifically for its demo. Runtime access and refresh tokens are obtained during tests and are never committed. For a private API, replace the demo credentials locally; `.env` is excluded by `.gitignore`.

## Run tests

```bash
# Full suite
pytest

# Parallel suite with a self-contained HTML report
pytest -n auto --html=reports/api-report.html --self-contained-html

# By category
pytest -m smoke
pytest -m negative
pytest -m performance
```

## Architecture

```text
src/config.py       Environment-backed configuration
src/api_client.py   Reusable HTTP client, logging, auth, timing
src/schemas.py      Central JSON contracts
tests/conftest.py   Isolated clients and authentication fixtures
tests/test_*.py     Business-focused tests
```

The API client applies a network timeout, logs every request without secrets, and stores measured response time for assertions. Tests do not depend on execution order and can run in parallel.

## Performance threshold

`MAX_RESPONSE_TIME_MS` defaults to 1000 ms, as requested in the assessment. On a slow external network, reviewers can override it locally while retaining the same measurable service-level check.
