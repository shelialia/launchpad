from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException, status


class APIError(HTTPException):
    """Generic schema for API Errors."""

    def __init__(code: int, detail: str):
        super().__init__(status_code=code, detail=detail)


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

    def __init__(detail: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundError(APIError):
    """Error response when a resource is not found (404 Not Found)."""

    def __init__(detail: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InvalidCreationError(APIError):
    """Error response when a resource cannot be created (422 Unprocessable Entity)."""

    def __init__(detail: str):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


class InternalServerError(APIError):
    """Error response for server issues (500 Internal Server Error)."""

    def __init__(detail: str):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
