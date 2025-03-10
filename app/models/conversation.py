from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional
import uuid
from enum import Enum
from beanie import Document, init_beanie
from app.models.responses import InvalidParametersError


class QueryRoleType(str, Enum):
    """Chat roles for each individual message."""

    SYSTEM = "system"  # Message is a system message
    USER = "user"  # Message is a prompt from the user
    ASSISTANT = "assistant"  # Message is a reply from the LLM model
    FUNCTION = "function"  # Message is a function call message


class Prompt(BaseModel):
    """Represents a single message in a conversation."""

    role: QueryRoleType = Field(
        ..., description="Chat roles: system, user, assistant, function"
    )
    content: str = Field(..., description="Message content")


class Conversation(Document):
    """Represents a series of interactions with an LLM."""

    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()), description="Unique conversation ID"
    )
    name: str = Field(..., max_length=200, description="Title of the conversation")
    params: Dict[str, str] = Field(
        default_factory=dict, description="Customizable AI model parameters"
    )
    tokens: int = Field(
        0, ge=0, description="Total number of tokens used in the conversation"
    )
    messages: list[Prompt] = Field(
        default_factory=list, description="List of chat messages"
    )


class ConversationFull(Conversation):
    """Complete conversation schema including messages."""

    messages: List[Prompt] = Field(
        default_factory=list, description="List of chat messages"
    )


class ConversationPOST(BaseModel):
    """Schema for creating a new conversation."""

    name: str = Field(..., max_length=200, description="Title of the conversation")
    model: str = Field(..., description="LLM model identifier")
    params: Dict[str, str] = Field(
        default_factory=dict, description="Custom parameters for the AI model"
    )

    @field_validator("params")
    def validate_params(cls, value):
        """Ensure only valid OpenAI parameters are passed."""
        allowed_params = {"temperature", "max_tokens", "top_p"}

        if value:
            for param in value:
                if param not in allowed_params:
                    raise InvalidParametersError(details={"invalid_param": param})

        return value


class ConversationPUT(BaseModel):
    """Schema for modifying an existing conversation."""

    name: Optional[str] = Field(
        None, max_length=200, description="Updated conversation title"
    )
    params: Optional[Dict[str, str]] = Field(
        None, description="Updated model parameters"
    )
