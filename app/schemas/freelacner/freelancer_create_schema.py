from pydantic import BaseModel, Field
from schemas.lead.lead_status import LeadStatus


class FreelancerCreate(BaseModel):
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    sector: str = Field(max_length=50)
    rating: int = Field(max_length=50)
    resume: str = Field()
