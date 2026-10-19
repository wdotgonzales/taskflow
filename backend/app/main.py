from fastapi import FastAPI
from contextlib import asynccontextmanager

from .routers.projects import router as project_router
from .routers.auth import router as auth_router
from .routers.users import router as user_router

# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # This runs ON SHUTDOWN
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(project_router)
app.include_router(auth_router)
app.include_router(user_router)

@app.get("/health")
async def health():
    return {"status":"ok"}


