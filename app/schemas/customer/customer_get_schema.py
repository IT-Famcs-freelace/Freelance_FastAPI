from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class CustomerGet(BaseModel):
    id: UUID


    first_name: str
    second_name: str
    rating: float

    class Config:
        from_attributes = True
