from typing import List, Dict, Union
from dataclasses import dataclass
from pydantic import BaseModel
from enum import Enum


class JobStatus(Enum):
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'



@dataclass
class SubmitJob:
    pass