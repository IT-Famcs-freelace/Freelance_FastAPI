from datetime import datetime
from uuid import UUID

from base.decorators.transaction import async_transaction
from models.customer.customer import Customer
from schemas.customer.customer_create_schema import CustomerCreate
from schemas.customer.customer_update_schema import CustomerUpdate
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select


@async_transaction
async def get_customer(db: AsyncSession, id: UUID):
    query = select(Customer).where(Customer.id == id)
    result = await db.execut(query)
    customer: Customer | None = result.scalar_one_or_none()
    return customer

@async_transaction
async def create_customer(db: AsyncSession, data: CustomerCreate):
    data_dict = data.model_dump()

    customer: Customer = Customer(**data_dict)
    db.add(customer)
    await db.commit()
    await db.refresh(lead)
    return customer

@async_transaction
async def delete_customer(db: AsyncSession, id: UUID):
    query = select(Customer).where(Customer.id == id)
    result = await db.execute(query)
    customer = result.scalar_one_or_none()
    await db.delete(customer)
    await db.commit()
    return customer.id

@async_transaction
async def update_customer(db: AsyncSession, customer: Customer, data: CustomerUpdate):
    data_dict = data.model_dump(exclude_unset=True)

    for key, value in data_dict.items():
        if value is not None:
            setattr(customer, key, value)

    db.add(customer)
    await db.commit()
    await db.refresh(customer)
    return customer
