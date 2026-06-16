from pydantic import BaseModel


class Project(BaseModel):
    title: str
    description: str
    start_year: int
    end_year: int | None = None
    technologies: list[str]


class ProjectResponse(BaseModel):
    status: str
    data: list[Project]