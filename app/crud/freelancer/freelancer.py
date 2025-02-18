from datetime import datetime
from uuid import UUID

from base.decorators.transaction import async_transaction
from models.freelancer.freelancer import Freelancer
from schemas.freelacner.freelancer_create_schema import FreelancerCreate
from schemas.freelancer.freelancer_update_schema import FreelancerUpdate
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select


@async_transaction
async def get_freelancer(db: AsyncSession, id: UUID):
    query = select(Freelancer).where(Freelancer.id == id)
    result = await db.execut(query)
    freelancer: Freelancer | None = result.scalar_one_or_none()
    return freelancer

@async_transaction
async def create_freelancer(db: AsyncSession, data: FreelancerCreate):
    data_dict = data.model_dump()

    freelancer: Freelancer = Freelancer(**data_dict)
    db.add(freelancer)
    await db.commit()
    await db.refresh(lead)
    return freelancer

@async_transaction
async def delete_freelancer(db: AsyncSession, id: UUID):
    query = select(Freelancer).where(Freelancer.id == id)
    result = await db.execute(query)
    freelancer = result.scalar_one_or_none()
    await db.delete(freelancer)
    await db.commit()
    return freelancer.id

@async_transaction
async def update_freelancer(db: AsyncSession, freelancer: Freelancer, data: FreelancerUpdate):
    data_dict = data.model_dump(exclude_unset=True)

    for key, value in data_dict.items():
        if value is not None:
            setattr(freelancer, key, value)

    db.add(freelancer)
    await db.commit()
    await db.refresh(freelancer)
    return freelancer
