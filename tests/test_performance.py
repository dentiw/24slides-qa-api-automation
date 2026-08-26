import pytest

from src.config import settings


@pytest.mark.performance
@pytest.mark.parametrize("path", ["/products?limit=10", "/users?limit=10", "/test"])
def test_public_endpoints_respond_within_threshold(api_client, path):
    response = api_client.get(path)

    assert response.status_code == 200
    assert response.elapsed_ms < settings.max_response_time_ms, (
        f"{path} took {response.elapsed_ms:.0f} ms; "
        f"threshold is {settings.max_response_time_ms} ms"
    )
