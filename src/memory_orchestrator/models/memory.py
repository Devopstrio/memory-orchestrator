"""Models."""
from typing import Any

from pydantic import BaseModel, Field


class MemoryPayload(BaseModel):
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)

class MemoryResponse(BaseModel):
    context: str
    sources: list[str] = Field(default_factory=list)
