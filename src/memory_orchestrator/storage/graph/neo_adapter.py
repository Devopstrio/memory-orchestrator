"""Neo4j adapter for semantic knowledge graphs."""
import structlog
from neo4j import AsyncGraphDatabase

from memory_orchestrator.config.settings import get_settings

logger = structlog.get_logger(__name__)
settings = get_settings()

class Neo4jAdapter:
    def __init__(self) -> None:
        self.driver = AsyncGraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_user, settings.neo4j_password)
        )

    async def close(self) -> None:
        await self.driver.close()

    async def store_entity(self, name: str, node_type: str) -> None:
        query = (
            "MERGE (e:Entity {name: $name}) "
            "SET e.type = $node_type "
            "RETURN e"
        )
        async with self.driver.session() as session:
            await session.run(query, name=name, node_type=node_type)
            logger.debug("entity_stored_in_graph", entity=name)

    async def get_related(self, entity_name: str) -> list[str]:
        query = (
            "MATCH (e:Entity {name: $name})-[r]-(connected) "
            "RETURN connected.name AS name, type(r) AS relation"
        )
        async with self.driver.session() as session:
            result = await session.run(query, name=entity_name)
            relations = []
            async for record in result:
                relations.append(f"{entity_name} [{record['relation']}] {record['name']}")
            return relations
