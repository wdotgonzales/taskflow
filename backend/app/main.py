from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import SQLModel

from .database import engine

from . import models

from .routers.projects import router as project_router

# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs ON STARTUP
    print("Connecting to PostgreSQL and creating tables...")
    SQLModel.metadata.create_all(engine)
    yield
    # This runs ON SHUTDOWN
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(project_router)

@app.get("/health")
async def health():
    return {"status":"ok"}


