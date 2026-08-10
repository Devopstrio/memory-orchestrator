"""API v1 Router."""
from fastapi import APIRouter

from memory_orchestrator.api.v1.endpoints import memory

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(memory.router, prefix="/memory")
