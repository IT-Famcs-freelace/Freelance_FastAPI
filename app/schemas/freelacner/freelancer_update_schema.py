from pydantic import BaseModel, Field


class FreelancerUpdate(BaseModel):
    first_name: str = Field(max_length=50, default=None)
    second_name: str = Field(max_length=50, default=None)
    sector: str = Field(max_length=50, default=None)
    rating: float = Field(max_length=50, default=None)
    resume: str = Field(default=None)
