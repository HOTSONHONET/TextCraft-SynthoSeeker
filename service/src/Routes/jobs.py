from fastapi import APIRouter
from src.Utils.schemas import *
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Form, UploadFile, File, Depends
import shutil


# Instanstiating router
job_router = APIRouter()


@job_router.post("/submit-job")
async def upload_job(file_obj) -> JSONResponse:
    """
    Endpoint to submit job for job creation
    
    """
    pass


@job_router.get("/get-status")
async def get_job_status(job_id: str) -> JSONResponse:
    """
    
    Endpoint to get the status of the job

    
    """
    pass
