"""Tests for user endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_users():
    """Test listing all users."""
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_user():
    """Test getting a specific user."""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data
    assert "email" in data


def test_get_user_not_found():
    """Test getting a non-existent user."""
    response = client.get("/users/99999")
    assert response.status_code == 404


def test_create_user():
    """Test creating a new user."""
    new_user = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "securepassword123"
    }
    response = client.post("/users/", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["is_active"] is True
