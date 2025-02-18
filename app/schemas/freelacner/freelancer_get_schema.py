from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class FreelancerGet(BaseModel):
    id: UUID


    first_name: str
    second_name: str
    sector: str
    rating: float
    resume: str

    class Config:
        from_attributes = True
