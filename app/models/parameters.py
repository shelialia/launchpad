from pydantic import BaseModel, Field


class IDParam(BaseModel):
    """Represents a unique ID string required in the path."""

    id: str = Field(..., format="uuid", description="A unique ID string")
