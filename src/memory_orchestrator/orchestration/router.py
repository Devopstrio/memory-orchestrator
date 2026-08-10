"""Orchestration engine."""
from memory_orchestrator.embeddings.client import EmbeddingClient
from memory_orchestrator.storage.cache.redis_adapter import RedisAdapter
from memory_orchestrator.storage.graph.neo_adapter import Neo4jAdapter
from memory_orchestrator.storage.vector.pg_adapter import PgVectorAdapter


class MemoryRouter:
    def __init__(self) -> None:
        self.vector = PgVectorAdapter()
        self.graph = Neo4jAdapter()
        self.cache = RedisAdapter()
        self.embeddings = EmbeddingClient()

    async def process_store(self, content: str) -> None:
        vec = await self.embeddings.embed(content)
        await self.vector.store(vec, content)
        await self.cache.add_recent(content)

    async def process_retrieve(self, query: str) -> str:
        vec = await self.embeddings.embed(query)
        v_res = await self.vector.search(vec)
        c_res = await self.cache.get_recent()
        return f"Synthesized from Cache: {c_res} | Vector: {v_res}"
