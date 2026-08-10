"""Neo4j adapter."""

class Neo4jAdapter:
    async def store_entity(self, name: str, node_type: str) -> None:
        pass

    async def get_related(self, entity_name: str) -> list[str]:
        return ["Connected entity 1"]
