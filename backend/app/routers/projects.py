from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
from ..schemas import ProjectRead, ProjectCreate
from sqlmodel import select
from ..database import SessionDep
from ..models import Projects
    
router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/", status_code=201)
def create_project(session: SessionDep, project: ProjectCreate) -> ProjectRead:
    db_project = Projects.model_validate(project, update={"owner_id": 1}) # owner_id is temporary for now
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project

@router.get("/")
def get_projects(session: SessionDep, q: str = '') -> list[ProjectRead]:
    statement = select(Projects)
    
    if q:
        statement = statement.where(Projects.name.ilike(f"%{q}%"))
    
    return session.exec(statement).all()

def get_project_or_404(project_id: int, session: SessionDep):
    project = session.get(Projects, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"  
        )
    return project

@router.get("/{project_id}")
def get_project_by_id(project: Annotated[dict, Depends(get_project_or_404)]) -> ProjectRead:
    return project

    
    

