from pydantic import BaseModel
from app.schemas.project import Project


class Education(BaseModel):
    degree: str
    institution: str
    start_year: int
    end_year: int | None = None
    description: str
    projects: list[Project]

class EducationResponse(BaseModel):
    status: str
    data: list[Education]