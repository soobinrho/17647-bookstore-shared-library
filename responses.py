from fastapi import Response, status
from fastapi.responses import JSONResponse

RESPONSE_NO_CONTENT = Response(status_code=status.HTTP_204_NO_CONTENT)

RESOPNSE_500_SERVER_ERROR = JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    content={"message": "Unexpected server-side error."},
)

RESPONSE_503_CIRCUIT_BREAKER_OPEN = JSONResponse(
    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    content={
        "message": "The recommendation external API seems to be unavailable. Please try again later."
    },
)

# =====
# Books
# =====
RESPONSE_INVALID_PRICE = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": "Invalid price. It must be a valid number, and it must have between 0 to 2 decimal places."
    },
)

RESPONSE_INVALID_QUANTITY = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={"message": "Invalid quantity. It must be a valid number."},
)

# =========
# Customers
# =========
RESPONSE_INVALID_EMAIL = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": 'Invalid email. It must match the regular expression "[^@]+@[^@]+\\.[^@]+".'
    },
)

RESPONSE_INVALID_STATE = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content={
        "message": "Invalid state. It must be a valid 2-letter U.S. state abbreviation."
    },
)

# ===
# BFF
# ===
RESPONSE_UNAUTHENTICATED = JSONResponse(
    status_code=status.HTTP_401_UNAUTHORIZED,
    content={"message": "Please provide a valid JWT."},
)
