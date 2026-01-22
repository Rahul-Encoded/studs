from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import uuid4

class User(BaseModel):
    name: str
    email: EmailStr
    role: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
