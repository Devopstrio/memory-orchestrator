"""PgVector adapter for episodic memory."""
import asyncpg
import structlog

from memory_orchestrator.config.settings import get_settings

logger = structlog.get_logger(__name__)
settings = get_settings()

class PgVectorAdapter:
    def __init__(self) -> None:
        self.dsn = settings.pg_dsn
        self.pool: asyncpg.Pool | None = None

    async def connect(self) -> None:
        if not self.pool:
            self.pool = await asyncpg.create_pool(self.dsn)

    async def store(self, embedding: list[float], content: str) -> None:
        await self.connect()
        if self.pool is None:
            raise RuntimeError("Database connection pool is not initialized.")
        async with self.pool.acquire() as conn:
            # We assume a table "memories" with columns id, content, embedding
            await conn.execute(
                "INSERT INTO memories (content, embedding) VALUES ($1, $2)",
                content,
                str(embedding)  # pgvector accepts string formatted arrays '[1,2,3]'
            )
            logger.debug("vector_stored", content_preview=content[:20])

    async def search(self, embedding: list[float], top_k: int = 5) -> list[str]:
        await self.connect()
        if self.pool is None:
            raise RuntimeError("Database connection pool is not initialized.")
        async with self.pool.acquire() as conn:
            # `<->` operator performs L2 distance (cosine distance via `<=>` could also be used)
            rows = await conn.fetch(
                """
                SELECT content FROM memories
                ORDER BY embedding <-> $1
                LIMIT $2
                """,
                str(embedding), top_k
            )
            logger.debug("vector_search_complete", matches=len(rows))
            return [row["content"] for row in rows]
