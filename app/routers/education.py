from fastapi import APIRouter
from app.services.education_service import get_education, add_education
from app.schemas.education import Education


router = APIRouter(
    prefix="/education",
    tags=["Education"]
)


@router.get("/", response_model=list[Education])
def read_education():
    return get_education()

@router.post("/", response_model=Education)
def create_education(education: Education):
   return add_education(education.model_dump())

