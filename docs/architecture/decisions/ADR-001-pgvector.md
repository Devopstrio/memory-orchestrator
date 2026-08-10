# ADR-001: Vector Database Selection

## Status
Accepted

## Context
We need a robust, scalable vector database for episodic memory embeddings.

## Decision
We will use PostgreSQL with the `pgvector` extension. 

## Consequences
- **Pros**: It allows us to leverage existing PostgreSQL infrastructure and knowledge within the enterprise. It supports ACID compliance.
- **Cons**: It is not a dedicated, distributed vector-first engine like Qdrant or Milvus, which may limit performance at billions of vectors. However, for our scale, it is optimal.
