from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    first_name: str = Field(max_length=50)
    second_name: str = Field(max_length=50)
    rating: int = Field(max_length=50)
