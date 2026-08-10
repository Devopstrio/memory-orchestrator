"""API Tests."""
import pytest
from fastapi.testclient import TestClient

from memory_orchestrator.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_store_memory() -> None:
    response = client.post("/v1/memory/store", json={
        "content": "The user likes blue cars.",
        "metadata": {"user_id": "123"}
    })
    assert response.status_code == 201
    assert response.json()["success"] is True

@pytest.mark.asyncio
async def test_retrieve_memory() -> None:
    response = client.get("/v1/memory/retrieve?query=cars")
    assert response.status_code == 200
    assert "Synthesized" in response.json()["context"]
