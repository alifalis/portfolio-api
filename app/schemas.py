from pydantic import BaseModel, EmailStr


class Project(BaseModel):
    id: int
    name: str
    description: str
    technologies: list[str]


class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str
