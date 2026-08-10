"""Embeddings client using local Sentence Transformers."""
import asyncio

import structlog
from sentence_transformers import SentenceTransformer

logger = structlog.get_logger(__name__)

class EmbeddingClient:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        logger.info("loading_embedding_model", model=model_name)
        # Load the local embedding model
        self.model = SentenceTransformer(model_name)

    async def embed(self, text: str) -> list[float]:
        # Run synchronous embedding generation in a threadpool to prevent blocking the async event loop
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(None, self.model.encode, [text])
        import typing
        return typing.cast(list[float], embeddings[0].tolist())
