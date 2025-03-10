from pydantic import BaseModel, Field


class CreatedResponse(BaseModel):
    """Response returned by OpenAI API model."""

    message: str = Field(..., description="Successful message")


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
