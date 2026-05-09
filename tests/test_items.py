"""Tests for item endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_items():
    """Test listing all items."""
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3  # Sample data initialized


def test_get_item():
    """Test getting a specific item."""
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "price" in data


def test_get_item_not_found():
    """Test getting a non-existent item."""
    response = client.get("/items/99999")
    assert response.status_code == 404


def test_create_item():
    """Test creating a new item."""
    new_item = {
        "name": "Test Item",
        "description": "A test item",
        "price": 99.99,
        "category": "Test"
    }
    response = client.post("/items/", json=new_item)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 99.99
    assert "id" in data


def test_update_item():
    """Test updating an existing item."""
    update_data = {"price": 150.00}
    response = client.put("/items/1", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 150.00
    assert data["id"] == 1


def test_delete_item():
    """Test deleting an item."""
    # Create an item first
    new_item = {
        "name": "Delete Me",
        "description": "To be deleted",
        "price": 10.00,
        "category": "Test"
    }
    create_response = client.post("/items/", json=new_item)
    item_id = create_response.json()["id"]

    # Delete it
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 204

    # Verify it's gone
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
