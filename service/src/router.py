from fastapi import APIRouter
from src.Routes.jobs import job_router


router = APIRouter()

@router.get("/")
async def health_check():
    """
    
    Endpoint to check app is live or not
    
    """
    return "App is live"

router.include_router(
    router = job_router,
    prefix = "/job",
    tags = ["jobs"]
)


