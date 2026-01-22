from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import uuid4
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    role: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
