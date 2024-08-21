from routes.login import get_password_hash
from utils.db_operations import save_in_db
from models.users import Users


def get_users(db, user):
    if user.role == 'admin':
        return db.query(Users).all()


def create_user_f(form, db, user):
    if user.role == 'admin':
        new_item_db = Users(
            name=form.name,
            username=form.username,
            role="admin",
            password=get_password_hash(form.password))
        save_in_db(db, new_item_db)


def update_user_f(form, db, user):
    if user.role == 'admin':
        db.query(Users).filter(Users.id == user.id).update({
            Users.name: form.name,
            Users.username: form.username,
            Users.password: get_password_hash(form.password),
            Users.role: "admin",
        })
        db.commit()


def delete_user_f(db, user):
    if user.role == "admin":
        db.query(Users).filter(Users.id == user.id).delete()
        db.commit()
