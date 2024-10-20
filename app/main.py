from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import crud, models, schemas, utils

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Daily Expenses Sharing App"}


@app.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/expenses/")
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    if expense.split_type == "equal":
        split = utils.split_equal(expense.amount, expense.participants)
    elif expense.split_type == "exact":
        split = utils.split_exact(expense.amounts)
    elif expense.split_type == "percentage":
        split = utils.split_percentage(expense.amount, expense.percentages)
    
    new_expense = crud.create_expense(db, expense, user_id=1)
    return {"message": "Expense added successfully"}

@app.get("/users/{user_id}/expenses/")
def get_user_expenses(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_expenses(db, user_id)

@app.get("/expenses/overall/")
def get_overall_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db)
