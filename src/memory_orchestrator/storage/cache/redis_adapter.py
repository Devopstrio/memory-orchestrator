"""Redis adapter."""

class RedisAdapter:
    async def get_recent(self) -> str:
        return "Recent short term memory"

    async def add_recent(self, memory: str) -> None:
        pass
