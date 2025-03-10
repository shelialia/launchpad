from fastapi import HTTPException, status

class APIError(HTTPException):
    """
    Base class for all API errors.

    This class extends FastAPI's HTTPException and provides a structured way
    to raise errors with a specific status code and detailed message.
    """

    def __init__(self, code: int, detail: str):
        """
        Initializes an APIError.

        Args:
            code (int): The HTTP status code for the error.
            detail (str): A descriptive error message.
        """
        super().__init__(status_code=code, detail=detail)


class InvalidParametersError(APIError):
    """
    Exception raised when invalid parameters are provided in the request.

    Returns a 400 Bad Request response.
    """

    def __init__(self, detail: str):
        """
        Initializes an InvalidParametersError.

        Args:
            detail (str): A descriptive message about the invalid parameters.
        """
        super().__init__(code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundError(APIError):
    """
    Exception raised when a requested resource is not found.

    Returns a 404 Not Found response.
    """

    def __init__(self):
        """
        Initializes a NotFoundError with a default error message.
        """
        super().__init__(code=status.HTTP_404_NOT_FOUND, detail="Resource is not found")


class InvalidCreationError(APIError):
    """
    Exception raised when a resource cannot be created due to invalid data or constraints.

    Returns a 422 Unprocessable Entity response.
    """

    def __init__(self):
        """
        Initializes an InvalidCreationError with a default error message.
        """
        super().__init__(code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Resource cannot be created")


class InternalServerError(APIError):
    """
    Exception raised when there is an internal server error.

    Returns a 500 Internal Server Error response.
    """

    def __init__(self):
        """
        Initializes an InternalServerError with a default error message.
        """
        super().__init__(code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
