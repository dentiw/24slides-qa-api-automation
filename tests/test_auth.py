import pytest
from jsonschema import validate

from src.config import settings
from src.schemas import LOGIN_SCHEMA


@pytest.mark.smoke
@pytest.mark.positive
def test_login_returns_tokens_and_expected_user(api_client):
    response = api_client.post(
        "/auth/login",
        json={"username": settings.username, "password": settings.password},
    )

    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=LOGIN_SCHEMA)
    assert body["username"] == settings.username
    assert body["accessToken"] != body["refreshToken"]


@pytest.mark.negative
def test_login_rejects_invalid_password(api_client):
    response = api_client.post(
        "/auth/login",
        json={"username": settings.username, "password": "definitely-invalid"},
    )

    assert response.status_code == 400
    assert "Invalid credentials" in response.json()["message"]


@pytest.mark.negative
def test_login_rejects_missing_required_password(api_client):
    response = api_client.post("/auth/login", json={"username": settings.username})

    assert response.status_code == 400
    assert response.json()["message"]


@pytest.mark.negative
def test_protected_profile_rejects_invalid_token(api_client):
    api_client.set_bearer_token("invalid-token")
    response = api_client.get("/auth/me")

    assert response.status_code == 401
    assert "message" in response.json()
