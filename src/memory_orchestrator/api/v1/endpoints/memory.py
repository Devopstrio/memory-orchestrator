"""Memory endpoints."""
import structlog
from fastapi import APIRouter
from pydantic import BaseModel

from memory_orchestrator.models.memory import MemoryPayload, MemoryResponse
from memory_orchestrator.orchestration.router import MemoryRouter

router = APIRouter(tags=["Memory"])
logger = structlog.get_logger("memory")
mem_router = MemoryRouter()

class BasicResponse(BaseModel):
    success: bool
    message: str

@router.post("/store", response_model=BasicResponse, status_code=201)
async def store_memory(payload: MemoryPayload) -> BasicResponse:
    logger.info("storing_memory", content_length=len(payload.content))
    await mem_router.process_store(payload.content)
    return BasicResponse(success=True, message="Memory Stored")

@router.get("/retrieve", response_model=MemoryResponse)
async def retrieve_memory(query: str) -> MemoryResponse:
    logger.info("retrieving_memory", query=query)
    ctx = await mem_router.process_retrieve(query)
    return MemoryResponse(context=ctx, sources=["cache", "pgvector"])
