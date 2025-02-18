from typing import Annotated
from uuid import UUID

from constants.urls import Urls
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from routers.customer.customer_importer import CustomerImporter
from routers.customer.customer_service import CustomerService
from routers.reponse_schemas.Customer_responses import (
    generate_template_responses,
    customer_count_by_status_responses,
    customer_create_responses,
    customer_delete_responses,
    customer_detail_responses,
    customer_import_responses,
    customer_list_responses,
    customer_patch_responses,
)
from schemas.general.paginated_response import PaginatedResponse
from schemas.customer.customer_create_schema import CustomerCreate
from schemas.customer.customer_get_schema import CustomerGet
from schemas.customer.customer_update_schema import CustomerUpdate

customer_router = APIRouter()

@customer_router.get(Urls.delete_customer, response_model = CustomerGet,responses=customer_detail_responses)
async def customer_detail(
    id: Annotated[UUID, Path()],
    service: CustomerService = Depends(CustomerService)
) -> CustomerGet:
    return await service.detail(id)

@customer_router.post(Urls.create_customer, response_model=CustomerGet, responses=customer_create_responses)
async def customer_create(
    data: Annotated[CustomerCreate, Path()],
    service: CustomerService = Depends(CustomerService)
) -> CustomerGet:
    return await service.create(data)

@customer_router.delete(Urls.delete_customer, responses=customer_delete_responses)
async def customer_delete(
    id: UUID,
    service: CustomerService = Depends(CustomerService)
):
    try:
        result = await service.delete(id)
        if not result:
            raise HTTPException(status_code=400, detail={"message": "Invalid input data"})
        return {"detail": {"message": "Customer deleted successfully"}}
    except Exception as e:
        raise HTTPException(status_code=400, detail={"message": str(e)})

@customer_router.update(Urls.update_customer, response_model=CustomerGet, responses=customer_patch_responses)
async def customer_update(
    id: Annotated[UUID, Path()],
    data: Annotated[CustomerUpdate, Path()],
    service: CustomerService = Depends(CustomerService)
):
    return await service.update(id, data)