from db import Base
from sqlalchemy import Column, String, Integer, Date


class Certificate(Base):
    __tablename__ = 'certificate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    course = Column(String(255), nullable=False)
    finished_date = Column(Date, nullable=False)
    series = Column(String(255), nullable=False)
