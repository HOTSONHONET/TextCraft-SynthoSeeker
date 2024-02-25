import logging
from fastapi.responses import JSONResponse
from fastapi import status, Request
import traceback


async def default_exception_handler(_: Request, exception: Exception) -> JSONResponse:
    """
    
    Coroutine to act as default exception handler for 500 status codes 

    """
    error = str(exception)
    logging.exception(exception)
    traceback.print_exc()
    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = {
            "message": "Interal Server Error",
            "error": error
        }
    )