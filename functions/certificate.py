from utils.db_operations import save_in_db
from models.certificate import Certificate


def get_certificate(db, user):
    if user.role == 'admin':
        return db.query(Certificate).all()


def get_next_serial_number(db):
    last_certificate = db.query(Certificate).order_by(Certificate.id.desc()).first()
    if last_certificate:
        last_serial_number = last_certificate.series
        number_part = int(last_serial_number[2:]) + 1
        new_serial_number = f"AB{number_part:05d}"
    else:
        new_serial_number = "AB00001"
    return new_serial_number


def create_certificate(form, db, user):
    if user.role == 'admin':
        new_serial_number = get_next_serial_number(db)  # Seriya raqamini olish
        new_item_db = Certificate(
            full_name=form.full_name,
            course=form.course,
            finished_date=form.finished_date,
            series=new_serial_number  # Yangi seriya raqamini qo'shish
        )
        save_in_db(db, new_item_db)
        return new_item_db


def delete_certificate(db, user):
    if user.role == "admin":
        db.query(Certificate).filter(Certificate.id == user.id).delete()
        db.commit()
