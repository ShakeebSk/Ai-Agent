from enum import Enum
from dataclasses import dataclass, field
from typing import Any
from __future__ import annotations


class AgentEventType(str, Enum):
    # Agent Life Cycle
    AGENT_START = "agent_start"
    AGENT_END = "agent_end"
    AGENT_ERROR = "agent_error"

    # Test streaming
    TEXT_DELTA = "text_delta"
    TEXT_COMPLETE = "text_complete"


class AgentEvent:
    type: AgentEventType
    data: dict[str:Any] = field(default_factory=dict)

    @classmethod
    def agent_start(cls, message: str) -> AgentEvent:
        return cls(type=AgentEventType.AGENT_START, data={"message": message})

