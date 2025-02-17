from uuid import uuid4

from models import Base
from models.general.timestampable_model import TimeStampableModel
from sqlalchemy import UUID, Column, String, Text, Numeric, Integer, DateTime


class Order(Base, TimeStampableModel):
    __tablename__ = "tbl_order"

    id = Column(UUID, primary_key=True, nullable=False, unique=True, default=uuid4())
    author = Column(UUID, nullable=False)
    performer = Column(UUID)
    title = Column(String(50), nullable=False, unique=False)
    description = Column(Text(), nullable=False)
    payment_method = Column(Text(), nullable=False)
    price = Column(Integer())
    created_at = Column(DateTime(), nullable=False)
    acepted_at = Colunm(DateTime())
    deadline = Column(DateTime())
