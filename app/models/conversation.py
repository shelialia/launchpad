from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import uuid


class Prompt(BaseModel):
    """Represents a single message in a conversation."""

    role: str = Field(..., description="Chat roles: system, user, assistant, function")
    content: str = Field(..., description="Message content")


class Conversation(BaseModel):
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


class ConversationPUT(BaseModel):
    """Schema for modifying an existing conversation."""

    name: Optional[str] = Field(
        None, max_length=200, description="Updated conversation title"
    )
    params: Optional[Dict[str, str]] = Field(
        None, description="Updated model parameters"
    )
