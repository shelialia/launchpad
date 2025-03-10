from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException, status


class CreatedResponse(BaseModel):
    """Response for successfully created resource with an ID."""

    id: str = Field(..., format="uuid", description="Unique ID of the created resource")


class UpdatedResponse(BaseModel):
    """Response for successfully updated resource."""

    message: str = Field(
        "Successfully updated resource", description="Confirmation message"
    )


class DeletedResponse(BaseModel):
    """Response for successfully deleted resource."""

    message: str = Field(
        "Successfully deleted resource", description="Confirmation message"
    )
    