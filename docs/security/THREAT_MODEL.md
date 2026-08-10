# Security Threat Model
| Threat | Mitigation |
|---|---|
| Unauthorized Memory Access | API requires JWT auth |
| Graph Injection | Neo4j queries use parameterized inputs |
