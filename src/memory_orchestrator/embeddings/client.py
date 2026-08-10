"""Embeddings client."""

class EmbeddingClient:
    async def embed(self, text: str) -> list[float]:
        return [0.1, 0.2, 0.3] * 128
