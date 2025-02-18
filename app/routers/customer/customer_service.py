from json import dumps
from typing import Callable
from uuid import UUID

from base.mixins.paginated_list_mixin import PaginatedListMixin
from crud.general.filter_query_by_search_fields import filter_query_by_search_fields
from crud.general.get_model_query import get_model_query
from crud.customer.customer import (
    get_customer,
    create_customer,
    delete_customer,
    update_customer,
)
from dependencies import async_get_db
from fastapi import Depends
from models.customer.customer import Customer
from schemas.customer.customer_create_schema import CustomerCreate
from schemas.customer.customer_get_schema import CustomerGet
from schemas.customer.customer_update_schema import CustomerUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.selectable import Select


class CustomerService(
    PaginatedListMixin,
):

    model: DeclarativeMeta = Customer
    schema: CustomerGet = CustomerGet
    fileds_to_search: list[str] = ["first_name", "second_name"]
    not_found_exception_func: Callable = raise_exception_if_lead_is_none

    def _get_query(self, *args, **kwargs) -> Select:

        teamplate: str = kwargs.get("template", "")

        query: Select = get_model_query(self.model)
        if template:
            query: Select = filter_query_by_search_fields(
                query, self.model, self.fileds_to_search, template
            )
        return query

    def _not_found_exception_func(self, lead: Lead | None):
        raise_exception_if_lead_is_none(lead)

    def __init__(self, db: AsyncSession = Depends(async_get_db)):
        self.db: AsyncSession = db


    async def detail(self, id: UUID) -> CustomerGet:

        customer: Customer | None = await get_customer(self.db, id=id)
        return CustomerGet.model_validate(customer)


    async def create(self, data: CustomerCreate) -> CustomerGet:

        customer: Customer = await create_lead(self.db, data)
        return CustomerGet.model_validate(customer)

    async def patch(self, id: UUID, data: CustomerUpdate) -> CustomerGet:

        customer: Customer | None = await get_customer(self.db, id=id)
        updated_customer: Customer = await update_customer(self.db, customer, data)
        return CustomerGet.model_validate(update_customer)

    async def delete(self, id: UUID):
        customer = await get_customer(self.db, id=id)
        raise_exception_if_lead_is_none(customer)
        return await delete_customer(self.db, id)


