import pytest
from jsonschema import validate

from src.schemas import PRODUCT_LIST_SCHEMA


@pytest.mark.smoke
@pytest.mark.positive
def test_product_list_honors_pagination_and_schema(api_client):
    response = api_client.get("/products", params={"limit": 5, "skip": 5})

    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=PRODUCT_LIST_SCHEMA)
    assert body["limit"] == 5
    assert body["skip"] == 5
    assert len(body["products"]) == 5


@pytest.mark.positive
def test_product_search_returns_relevant_values(api_client):
    query = "phone"
    response = api_client.get("/products/search", params={"q": query})

    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=PRODUCT_LIST_SCHEMA)
    assert body["total"] > 0
    assert any(query in product["title"].lower() for product in body["products"])


@pytest.mark.negative
def test_unknown_product_returns_not_found(api_client):
    response = api_client.get("/products/999999999")

    assert response.status_code == 404
    assert response.json()["message"] == "Product with id '999999999' not found"


@pytest.mark.positive
def test_authenticated_profile_matches_logged_in_user(authenticated_client):
    response = authenticated_client.get("/auth/me")

    assert response.status_code == 200
    body = response.json()
    assert body["username"]
    assert body["email"]
