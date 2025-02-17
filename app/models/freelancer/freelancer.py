from uuid import uuid4

from models import Base
from models.general.timestampable_model import TimeStampableModel
from sqlalchemy import UUID, Column, String, Text, Numeric


class Freelancer(Base, TimeStampableModel):
    __tablename__ = "tbl_user"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, default=uuid4())
    first_name = Column(String(30), nullable=False, unique=False)
    second_name = Column(String(30), nullable=False, unique=False)
    sector = Column(String(30), nullable=False, unique=False)
    rating = Column(Numeric(4, 2), nullable=False)
    resume = Column(Text(), nullable=False)

