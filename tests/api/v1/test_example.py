import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_example_endpoint():
    """Test the example endpoint."""
    response = client.get("/api/v1/example/example")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the example endpoint!"} 