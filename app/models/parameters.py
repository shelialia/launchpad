from pydantic import BaseModel, Field
from typing import List


class IDParam(BaseModel):
    """Represents a unique ID string required in the path."""

    id: str = Field(..., format="uuid", description="A unique ID string")


class SecondaryIDParam(BaseModel):
    """Represents a secondary unique ID string required in the path."""

    secondary_id: str = Field(
        ..., format="uuid", description="A unique secondary ID string"
    )


class IDListParam(BaseModel):
    """Represents a list of optional IDs provided in the query."""

    ids: List[str] = Field(..., description="A list of optional UUIDs")
