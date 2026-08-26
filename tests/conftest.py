import pytest

from src.api_client import ApiClient
from src.config import settings


@pytest.fixture
def api_client():
    client = ApiClient(settings.base_url)
    yield client
    client.session.close()


@pytest.fixture
def access_token(api_client):
    response = api_client.post(
        "/auth/login",
        json={
            "username": settings.username,
            "password": settings.password,
            "expiresInMins": 30,
        },
    )
    assert response.status_code == 200, response.text
    return response.json()["accessToken"]


@pytest.fixture
def authenticated_client(api_client, access_token):
    api_client.set_bearer_token(access_token)
    return api_client
