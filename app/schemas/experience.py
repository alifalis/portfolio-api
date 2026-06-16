from pydantic import BaseModel

class Experience(BaseModel):
    title: str
    company: str
    start_year: int
    end_year: int
    description: str

class ExperienceResponse(BaseModel):
    status: str
    data: list[Experience]