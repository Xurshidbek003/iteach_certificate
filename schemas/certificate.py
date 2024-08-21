from pydantic import BaseModel
from db import SessionLocal
import datetime

db = SessionLocal()


class CreateCertificate(BaseModel):
    full_name: str
    course: str
    finished_date: datetime.date

