from sqlalchemy import Column, String, Date, Integer
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    fhir_id = Column(String, unique=True, nullable=True)
    identifier = Column(String, unique=True, index=True)
    name = Column(String)
    gender = Column(String)
    birth_date = Column(Date)