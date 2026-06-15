from pydantic import BaseModel

class Education(BaseModel):
    degree: str
    institution: str
    start_year: int
    end_year: int
    description: str

class EducationResponse(BaseModel):
    status: str
    data: list[Education]
    