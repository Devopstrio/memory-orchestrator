"""Memory Compactor for summarizing and fading working memory."""
import asyncio
import structlog
from memory_orchestrator.storage.cache.redis_adapter import RedisAdapter
from memory_orchestrator.storage.vector.pg_adapter import PgVectorAdapter
from memory_orchestrator.embeddings.client import EmbeddingClient

logger = structlog.get_logger(__name__)

class MemoryCompactor:
    """Runs in the background to summarize Redis working memory into PgVector episodic memory."""
    def __init__(self) -> None:
        self.cache = RedisAdapter()
        self.vector = PgVectorAdapter()
        self.embeddings = EmbeddingClient()
        
    async def summarize_and_fade(self, raw_text: str) -> str:
        # In a real environment, call an LLM (OpenAI/Anthropic) to summarize.
        # For this orchestrator core, we simulate compaction logic.
        return f"[Summarized Memory]: {raw_text[:50]}..."

    async def run_compaction_cycle(self) -> None:
        """Polls cache for old memory and moves it to vector store."""
        logger.info("starting_compaction_cycle")
        recent = await self.cache.get_recent()
        if recent:
            summary = await self.summarize_and_fade(recent)
            vec = await self.embeddings.embed(summary)
            await self.vector.store(vec, summary)
            logger.info("memory_compacted_and_stored", summary_len=len(summary))
