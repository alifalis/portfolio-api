from fastapi import APIRouter
from app.services.education_service import get_education
from app.schemas.education import Education


router = APIRouter(
    prefix="/education",
    tags=["Education"]
)


@router.get("/", response_model=list[Education])
def read_education():
    return get_education()