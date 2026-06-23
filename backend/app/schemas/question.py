from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class QuestionCreate(BaseModel):
    text: str

class QuestionResponse(BaseModel):
    id: str
    text: str
    topic: str
    created_at: datetime

    class Config:
        from_attributes = True

class QuestionSearchResponse(BaseModel):
    id: str
    text: str
    topic: str
    score: float

    class Config:
        from_attributes = True
