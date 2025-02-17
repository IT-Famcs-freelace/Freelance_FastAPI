from uuid import uuid4

from models import Base
from models.general.timestampable_model import TimeStampableModel
from sqlalchemy import UUID, Column, String, Text, Boolean


class User(Base, TimeStampableModel):
    __tablename__ = "tbl_user"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, default=uuid4())
    email = Column(String(50), index=True, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    user_name = Column(String(30), nullable=False, unique=True)
    is_banned = Column(Boolean(), nullable=True)
    is_golden_user = Column(Boolean(), nullable=False)
    telegram = Column(String(50), nullable=True, unique=True)
    watsup = Column(String(50), nullable=True, unique=True)
    phone_number = Column(String(20), nullable=True, unique=True)
