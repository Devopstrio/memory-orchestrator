"""API Tests."""
from fastapi.testclient import TestClient
from memory_orchestrator.main import app
import pytest
from unittest.mock import patch

client = TestClient(app)

@pytest.mark.asyncio
@patch("memory_orchestrator.api.v1.endpoints.memory.mem_router")
async def test_store_memory(mock_mem_router) -> None:
    # Mock the async method
    from unittest.mock import AsyncMock
    mock_mem_router.process_store = AsyncMock()
    
    response = client.post("/v1/memory/store", json={
        "content": "The user likes blue cars.",
        "metadata": {"user_id": "123"}
    })
    
    assert response.status_code == 201
    assert response.json()["success"] is True
    mock_mem_router.process_store.assert_called_once_with("The user likes blue cars.")

@pytest.mark.asyncio
@patch("memory_orchestrator.api.v1.endpoints.memory.mem_router")
async def test_retrieve_memory(mock_mem_router) -> None:
    # Mock the async method to return a specific string
    from unittest.mock import AsyncMock
    mock_mem_router.process_retrieve = AsyncMock(return_value="Synthesized from Cache: test | Vector: test")
    
    response = client.get("/v1/memory/retrieve?query=cars")
    assert response.status_code == 200
    assert "Synthesized" in response.json()["context"]
    mock_mem_router.process_retrieve.assert_called_once_with("cars")
