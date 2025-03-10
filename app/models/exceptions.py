from fastapi import HTTPException, status

class APIError(HTTPException):
    """Generic schema for API Errors."""

    def __init__(self, code: int, detail: str):
        super().__init__(status_code=code, detail=detail)


class InvalidParametersError(APIError):
    """Error response for invalid parameters (400 Bad Request)."""

    def __init__(self, detail: str):
        super().__init__(code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundError(APIError):
    """Error response when a resource is not found (404 Not Found)."""

    def __init__(self):
        super().__init__(code=status.HTTP_404_NOT_FOUND, detail="Resource is not found")


class InvalidCreationError(APIError):
    """Error response when a resource cannot be created (422 Unprocessable Entity)."""

    def __init__(self):
        super().__init__(code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Resource cannot be created")


class InternalServerError(APIError):
    """Error response for server issues (500 Internal Server Error)."""

    def __init__(self):
        super().__init__(code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
