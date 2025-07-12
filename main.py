from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fhir/patients/", response_model=schemas.PatientOut)
def create_fhir_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    try:
        db_patient = models.Patient(
            fhir_id=patient.fhir_id,
            identifier=patient.identifier,
            name=patient.name,
            gender=patient.gender,
            birth_date=patient.birth_date
        )
        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)
        return db_patient
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"FHIR parsing error: {str(e)}")

@app.get("/patients/", response_model=list[schemas.PatientOut])
def get_all_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()

@app.get("/patients/{patient_id}", response_model=schemas.PatientOut)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient    

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient.fhir_id = updated_patient.fhir_id
    patient.identifier = updated_patient.identifier
    patient.name = updated_patient.name
    patient.gender = updated_patient.gender
    patient.birth_date = updated_patient.birth_date

    db.commit()
    db.refresh(patient)
    return {"message": "Patient updated successfully", "patient": schemas.PatientOut.from_orm(patient)}    

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted successfully"}    