from fastapi import APIRouter
from src.Utils.schemas import *
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Form, UploadFile, File, Depends
import shutil


# Instanstiating router
kg_router = APIRouter()


@kg_router.post("/submit-job")
async def upload_job(file_obj) -> JSONResponse:
    """
    Endpoint to submit job for kg creation
    
    """
    pass


@kg_router.get("/get-status")
async def get_job_status(job_id: str) -> JSONResponse:
    """
    
    Endpoint to get the status of the job

    
    """
    pass
