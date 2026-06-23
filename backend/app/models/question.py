from sqlalchemy import Column, String, DateTime, JSON
import uuid
from datetime import datetime
from app.db.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String, index=True)
    text = Column(String)
    embedding = Column(JSON)  # SQLite can store JSON strings via SQLAlchemy JSON type
    topic = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
