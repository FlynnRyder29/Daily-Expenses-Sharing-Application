import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from app.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

Base.metadata.create_all(bind=engine)

def test_add_equal_expense():
    
    client.post("/users/", json={"name": "John", "email": "john@example.com", "mobile_number": "1234567890"})
    client.post("/users/", json={"name": "Jane", "email": "jane@example.com", "mobile_number": "0987654321"})

    response = client.post(
        "/expenses/",
        json={
            "description": "Dinner",
            "amount": 2000,
            "split_type": "equal",
            "participants": [1, 2]  
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Expense added successfully"

def test_add_percentage_expense():
    client.post("/users/", json={"name": "Alice", "email": "alice@example.com", "mobile_number": "1231231234"})
    client.post("/users/", json={"name": "Bob", "email": "bob@example.com", "mobile_number": "3213214321"})

    
    response = client.post(
        "/expenses/",
        json={
            "description": "Party",
            "amount": 3000,
            "split_type": "percentage",
            "participants": [1, 2],
            "percentages": {1: 60, 2: 40}  
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Expense added successfully"
