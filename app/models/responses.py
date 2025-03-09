from pydantic import BaseModel, Field
from typing import Optional


class APIError(BaseModel):
    """Generic schema for API Errors."""

    code: int = Field(..., description="API Error code associated with the error")
    message: str = Field(..., description="Error message associated with the error")
    request: Optional[dict] = Field(
        None, description="Request details associated with the error"
    )
    details: Optional[dict] = Field(
        None, description="Other details associated with the error"
    )


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


class InvalidParametersError(APIError):
    """Error response for invalid parameters (400 Bad Request)."""

    code: int = Field(400, description="HTTP Status Code for Invalid Parameters")
    message: str = Field(
        "Invalid parameters provided", description="Error message for invalid input"
    )


class NotFoundError(APIError):
    """Error response when a resource is not found (404 Not Found)."""

    code: int = Field(404, description="HTTP Status Code for Not Found")
    message: str = Field(
        "Specified resource(s) was not found",
        description="Error message when resource is missing",
    )


class InvalidCreationError(APIError):
    """Error response when a resource cannot be created (422 Unprocessable Entity)."""

    code: int = Field(422, description="HTTP Status Code for Invalid Creation")
    message: str = Field(
        "Unable to create resource",
        description="Error message when resource creation fails",
    )


class InternalServerError(APIError):
    """Error response for server issues (500 Internal Server Error)."""

    code: int = Field(500, description="HTTP Status Code for Internal Server Error")
    message: str = Field(
        "Internal server error", description="Error message for internal issues"
    )
