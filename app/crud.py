from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, name=user.name, mobile_number=user.mobile_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    new_expense = models.Expense(description=expense.description, amount=expense.amount, split_type=expense.split_type, user_id=user_id)
    db.add(new_expense)
    db.commit()
    return new_expense

def get_user_expenses(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.user_id == user_id).all()

def get_all_expenses(db: Session):
    return db.query(models.Expense).all()
