from typing import Annotated
from uuid import UUID

from constants.urls import Urls
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from routers.freelancer.freelancer_importer import FreelancerImporter
from routers.freelancer.freelancer_service import FreelancerService
from routers.reponse_schemas.Freelancer_responses import (
    generate_template_responses,
    freelancer_count_by_status_responses,
    freelancer_create_responses,
    freelancer_delete_responses,
    freelancer_detail_responses,
    freelancer_import_responses,
    freelancer_list_responses,
    freelancer_patch_responses,
)
from schemas.general.paginated_response import PaginatedResponse
from schemas.freelancer.freelancer_create_schema import FreelancerCreate
from schemas.freelancer.freelancer_get_schema import FreelancerGet
from schemas.freelancer.freelancer_update_schema import FreelancerUpdate

freelancer_router = APIRouter()

@freelancer_router.get(Urls.delete_freelancer, response_model = FreelancerGet,responses=freelancer_detail_responses)
async def freelancer_detail(
    id: Annotated[UUID, Path()],
    service: FreelancerService = Depends(FreelancerService)
) -> FreelancerGet:
    return await service.detail(id)

@freelancer_router.post(Urls.create_freelancer, response_model=FreelancerGet, responses=freelancer_create_responses)
async def freelancer_create(
    data: Annotated[FreelancerCreate, Path()],
    service: FreelancerService = Depends(FreelancerService)
) -> FreelancerGet:
    return await service.create(data)

@freelancer_router.delete(Urls.delete_freelancer, responses=freelancer_delete_responses)
async def freelancer_delete(
    id: UUID,
    service: FreelancerService = Depends(FreelancerService)
):
    try:
        result = await service.delete(id)
        if not result:
            raise HTTPException(status_code=400, detail={"message": "Invalid input data"})
        return {"detail": {"message": "Freelancer deleted successfully"}}
    except Exception as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

@freelancer_router.update(Urls.update_freelancer, response_model=FreelancerGet, responses=freelancer_patch_responses)
async def freelancer_update(
    id: Annotated[UUID, Path()],
    data: Annotated[FreelancerUpdate, Path()],
    service: FreelancerService = Depends(FreelancerService)
):
    return await service.update(id, data)