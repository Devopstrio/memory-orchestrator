# Low Level Design (LLD)

## 1. API Interfaces
The FastAPI app exposes:
- `POST /v1/memory/store`
  - Accepts a `MemoryPayload` containing the raw text and metadata.
  - Generates embeddings using `sentence-transformers` asynchronously.
  - Persists the vector to `pgvector` and relationships to `Neo4j`.
- `GET /v1/memory/retrieve`
  - Accepts a query string.
  - Queries `Redis`, `pgvector`, and `Neo4j` concurrently.
  - Returns a unified `MemoryResponse`.

## 2. Storage Adapters
- **PgVectorAdapter**: Uses `asyncpg` to execute raw SQL against PostgreSQL. The schema includes an `id`, `text`, `metadata`, and `embedding` (type `vector(384)`).
- **Neo4jAdapter**: Uses the official `neo4j` async driver to execute Cypher queries. Nodes represent entities extracted from the text.
- **RedisAdapter**: Uses `redis.asyncio` for short TTL storage.

## 3. Background Compaction
A background asyncio task runs periodically to select old vectors (older than 30 days) and uses an LLM summarization pipeline to compress multiple raw vectors into a single summary vector, deleting the old granular records.
