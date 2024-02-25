from typing import Awaitable, Callable
from fastapi import FastAPI


def register_start_events(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """
    
    Events to start on app
    
    """

    @app.on_event('startup')
    async def _startup() -> None:
        """
        Registering startup events

        """
        pass

    return _startup

def register_shutdown_events(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """
    
    Events to end on app
    
    """

    @app.on_event('shutdown')
    async def _shutdown() -> None:
        """
        Registering shutdown events

        """
        pass

    return _shutdown
