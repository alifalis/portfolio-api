from pydantic import BaseModel

class profile(BaseModel):
    name: str
    surname: str
    email: str
    contact_number: str
    linkedin: str
    github: str

class ProfileResponse(BaseModel):
    status: str
    data: profile


