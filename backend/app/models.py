from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True) 
    hashed_password: str
    projects: list["Projects"] = Relationship(back_populates="owner")
    
class Projects(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str = ''
    owner_id: int | None = Field(default=None, foreign_key="users.id")
    owner: Users | None = Relationship(back_populates="projects")
    tasks: list["Tasks"] = Relationship(back_populates="project")
    
class Tasks(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    due_date: date | None = None
    status: str = Field(default="todo")
    project_id: int | None = Field(default=None, foreign_key="projects.id")
    project: Projects | None = Relationship(back_populates="tasks")
    
