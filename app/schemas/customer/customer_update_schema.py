from pydantic import BaseModel, Field


class CustomerUpdate(BaseModel):
    first_name: str = Field(max_length=50, default=None)
    second_name: str = Field(max_length=50, default=None)
    rating: float = Field(max_length=50, default=None)
