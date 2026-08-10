# ADR-002: Neo4j for Knowledge Graph

## Status
Accepted

## Context
We need a way to store non-episodic, heavily relational knowledge (e.g., "User A belongs to Organization B, which owns Project C").

## Decision
We will use Neo4j as the Graph Database layer.

## Consequences
- **Pros**: Native property graph model, highly optimized Cypher query language.
- **Cons**: Requires managing a separate infrastructure component alongside PostgreSQL.
