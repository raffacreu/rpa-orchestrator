from sqlalchemy.orm import Session
from app.models.automation import Automation
from app.schemas.automation import AutomationCreate

def create_automation(db: Session, automation: AutomationCreate):
    db_automation = Automation(
        name=automation.name,
        steps_json=automation.steps_json
    )
    db.add(db_automation)
    db.commit()
    db.refresh(db_automation)
    return db_automation