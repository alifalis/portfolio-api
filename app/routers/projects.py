from fastapi import APIRouter
from app.services.project_service import get_projects
from app.schemas.project import Project


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/", response_model=list[Project])
def read_projects():
    return get_projects()