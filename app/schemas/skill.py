from pydantic import BaseModel

class Skill(BaseModel):
    name: str
    description: str


class SkillResponse(BaseModel):
    status: str
    data: list[Skill]