from pydantic import BaseModel
from datetime import datetime

class AutomationCreate(BaseModel):
    name: str
    steps_json: list

class AutomationResponse(BaseModel):
    id: int
    name: str
    steps_json: list
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True