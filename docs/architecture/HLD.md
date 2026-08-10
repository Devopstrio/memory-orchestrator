# High Level Design (HLD)

## 1. Introduction
The Memory Orchestrator is the cognitive backbone of the Devopstrio Enterprise Context Engineering platform. It provides a unified API for managing short-term (working) memory, long-term semantic (episodic) memory, and relationship-based (graph) memory for LLM agents.

## 2. Architecture
The system employs a 3-tier memory model:
1. **Working Memory (Redis)**: Extremely fast access to recent conversational context (e.g., the last 5 minutes of a chat session).
2. **Episodic Memory (PgVector)**: A PostgreSQL database extended with the `pgvector` plugin to store semantic embeddings of past interactions or documents.
3. **Relational Memory (Neo4j)**: A graph database that maps entities (Users, Organizations, Topics) and the relationships between them.

## 3. Data Flow
When an AI agent requests memory context for a specific query:
1. The Orchestrator Router analyzes the query.
2. It fetches short-term context from Redis.
3. It performs a similarity search in PgVector to find top-K semantic matches.
4. It queries Neo4j to pull any graph nodes directly related to the entities identified in the query.
5. The Synthesizer merges and deduplicates these streams before returning a unified JSON payload to the agent.
