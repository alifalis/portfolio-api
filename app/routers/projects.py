from fastapi import APIRouter
from app.schemas import Project

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

projects = [
    Project(
        id=1,
        name="Portfolio API",
        description="API REST réalisée avec FastAPI",
        technologies=["Python", "FastAPI"]
    )
]


@router.get("/", response_model=list[Project])
def get_projects():
    return projects


@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int):
    for project in projects:
        if project.id == project_id:
            return project