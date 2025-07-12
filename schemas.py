from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    identifier: str
    name: str
    gender: str
    birth_date: date

class PatientCreate(PatientBase):
    fhir_id: str

class PatientOut(BaseModel):
    id: int
    fhir_id: str
    identifier: str
    name: str
    gender: str
    birth_date: date

    class Config:
        from_attributes = True