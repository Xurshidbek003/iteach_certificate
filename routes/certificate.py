from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.certificate import get_certificate, create_certificate, delete_certificate
from routes.login import get_current_active_user
from schemas.certificate import CreateCertificate
from db import database
from schemas.users import CreateUser

certificate_router = APIRouter(
    prefix="/certificate",
    tags=["Certificate operation"]
)


@certificate_router.get('/get')
def get(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return get_certificate(db, current_user)


@certificate_router.post('/create')
def create_certificates(form: CreateCertificate, db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    created_certificate = create_certificate(form, db, current_user)
    return {
        "message": "Amaliyot muvaffaqiyatli amalga oshirildi",
        "certificate": {
            "full_name": created_certificate.full_name,
            "course": created_certificate.course,
            "finished_date": created_certificate.finished_date,
            "series": created_certificate.series
        }
    }


@certificate_router.delete("/delete")
def delete_certificates(db: Session = Depends(database),
                        current_user: CreateUser = Depends(get_current_active_user)):
    delete_certificate(db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
