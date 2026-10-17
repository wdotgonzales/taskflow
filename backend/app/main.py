from fastapi import FastAPI

from routers.projects import router as project_router

app = FastAPI()

app.include_router(project_router)

@app.get("/health")
async def health():
    return {"status":"ok"}


