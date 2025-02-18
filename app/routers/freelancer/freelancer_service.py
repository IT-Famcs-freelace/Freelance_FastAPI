from json import dumps
from typing import Callable
from uuid import UUID

from base.mixins.paginated_list_mixin import PaginatedListMixin
from crud.general.filter_query_by_search_fields import filter_query_by_search_fields
from crud.general.get_model_query import get_model_query
from crud.freelancer.freelancer import (
    get_freelancer,
    create_freelancer,
    delete_freelancer,
    update_freelancer,
)
from dependencies import async_get_db
from fastapi import Depends
from models.freelancer.freelancer import Freelancer
from schemas.freelacner.freelancer_create_schema import FreelancerCreate
from schemas.freelacner.freelancer_get_schema import FreelancerGet
from schemas.freelacner.freelancer_update_schema import FreelancerUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.selectable import Select


class FreelancerService(
    PaginatedListMixin,
):

    model: DeclarativeMeta = Freelancer
    schema: FreelancerGet = FreelancerGet
    fileds_to_search: list[str] = ["first_name", "second_name", "resume", "sector"]
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


    async def detail(self, id: UUID) -> FreelancerGet:

        freelancer: Freelancer | None = await get_freelancer(self.db, id=id)
        return FreelancerGet.model_validate(freelancer)


    async def create(self, data: FreelancerCreate) -> FreelancerGet:

        freelancer: Freelancer = await create_lead(self.db, data)
        return FreelancerGet.model_validate(freelancer)

    async def patch(self, id: UUID, data: FreelancerUpdate) -> FreelancerGet:

        freelancer: Freelancer | None = await get_freelancer(self.db, id=id)
        updated_freelancer: Freelancer = await update_freelancer(self.db, freelancer, data)
        return FreelancerGet.model_validate(update_freelancer)

    async def delete(self, id: UUID):
        freelancer = await get_freelancer(self.db, id=id)
        raise_exception_if_lead_is_none(freelancer)
        return await delete_freelancer(self.db, id)


