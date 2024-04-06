from fastapi import FastAPI
from src.router import router
from fastapi.middleware.cors import CORSMiddleware
from src.lifetime import register_start_events, register_shutdown_events
from src.Middlewares.exception_handler import default_exception_handler
import os


def start_service() -> FastAPI:
    """
    
    Function to initialize the app and return an instance of it
    
    """
    
    # Setting project dir name as the application title
    app_name = os.getcwd().split("/")[-1]
    app = FastAPI(
        title = app_name
    )

    # Integrating CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"]
    )

    # Registering start up and shutdown events
    register_start_events(app)
    register_shutdown_events(app)


    # Adding exception handling middleware
    app.add_exception_handler(
        Exception,
        default_exception_handler
    )
    
    # Ingrating routes
    app.include_router(router = router)

    return app