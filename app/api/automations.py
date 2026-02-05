from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.automation import AutomationCreate, AutomationResponse
from app.services.automation_service import create_automation
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/automations", response_model=AutomationResponse)
def create_automation_route(automation: AutomationCreate, db: Session = Depends(get_db)):
    return create_automation(db, automation)