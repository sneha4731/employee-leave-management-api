from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "employee"


class LeaveCreate(BaseModel):
    leave_type: str
    start_date: date
    end_date: date
    reason: str
