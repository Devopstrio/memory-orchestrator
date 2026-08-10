"""Main entrypoint for memory-orchestrator."""
import structlog
import uvicorn
from fastapi import FastAPI

from memory_orchestrator.api.v1.router import api_v1_router
from memory_orchestrator.config.settings import get_settings

settings = get_settings()
logger = structlog.get_logger("memory_orchestrator.main")

app = FastAPI(title="Memory Orchestrator")

app.include_router(api_v1_router)

if __name__ == "__main__":
    logger.info("starting_memory_orchestrator", host=settings.host, port=settings.port)
    uvicorn.run("memory_orchestrator.main:app", host=settings.host, port=settings.port, reload=True)
