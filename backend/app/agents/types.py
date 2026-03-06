from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


StructuredPayload = dict[str, Any]


@dataclass(slots=True)
class AgentInput:
    """Structured input envelope for every agent."""

    data: StructuredPayload
    language: str = "he"
    context: StructuredPayload = field(default_factory=dict)


@dataclass(slots=True)
class AgentOutput:
    """Structured output envelope for every agent."""

    agent: str
    language: str
    prompt_template: str
    input_data: StructuredPayload
    result: StructuredPayload
    metadata: StructuredPayload = field(default_factory=dict)
