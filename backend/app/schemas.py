from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str = ''
    
class ProjectRead(BaseModel):
    id: int
    name: str
    description: str