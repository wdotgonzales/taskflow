from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

class ProjectCreate(BaseModel):
    name: str
    description: str = ''
    
class ProjectRead(BaseModel):
    id: int
    name: str
    description: str

# -------------------------------- Temporary --------------------------------
fake_db = [
    {"id": 1, "name": "Website Redesign", "description": "Revamp landing page"},
    {"id": 2, "name": "Mobile App", "description": "iOS and Android client app"},
    {"id": 3, "name": "Database Migration", "description": "Move from MySQL to PostgreSQL"},
    {"id": 4, "name": "API Authentication", "description": "Implement OAuth2 login flow"},
    {"id": 5, "name": "CI/CD Pipeline", "description": "Set up GitHub Actions for auto-deploy"},
    {"id": 6, "name": "User Analytics", "description": "Integrate Mixpanel tracking"},
    {"id": 7, "name": "Payment Gateway", "description": "Integrate Stripe checkout"},
    {"id": 8, "name": "Email Notifications", "description": "Send transactional emails via SendGrid"},
    {"id": 9, "name": "Admin Dashboard", "description": "Build internal metrics reporting tool"},
    {"id": 10, "name": "Security Audit", "description": "Perform vulnerability scanning and penetration test"}
]

def lookup_get_project_by_id(item_id, db=fake_db):
    return next((item for item in db if item["id"] == item_id), None)

def filter_by_name_keyword(keyword, db=fake_db):
    keyword_lower = keyword.lower()
    return [item for item in db if keyword_lower in item["name"].lower()]
# -------------------------------- End of Temporary --------------------------------

    
router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/", status_code=201)
def create_project(project: ProjectCreate) -> ProjectRead:
    new_id = len(fake_db) + 1
    project_data = {"id": new_id, **project.model_dump()}
    fake_db.append(project_data)
    return lookup_get_project_by_id(project_data['id'])

@router.get("/")
def get_projects(q: str = '') -> list[ProjectRead]:
    if q:
        return filter_by_name_keyword(q)
    
    return fake_db

def get_project_or_404(project_id: int) -> ProjectRead:
    project = lookup_get_project_by_id(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"  
        )
    return project

@router.get("/{project_id}")
def get_project_by_id(project: Annotated[dict, Depends(get_project_or_404)]):
    return project

    
    

