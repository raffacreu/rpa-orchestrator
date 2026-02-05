from fastapi import FastAPI
from app.api.automations import router

app = FastAPI(title="RPA Orchestrator")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "RPA Orchestrator API"}