"""PgVector adapter."""

class PgVectorAdapter:
    async def store(self, embedding: list[float], content: str) -> None:
        pass

    async def search(self, embedding: list[float]) -> list[str]:
        return ["Similar memory 1"]
