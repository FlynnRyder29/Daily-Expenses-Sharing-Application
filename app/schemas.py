from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Dict

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    mobile_number: str = Field(..., pattern="^\d{10}$")  

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    split_type: str
    participants: List[int]
    percentages: Optional[Dict[int, float]] = None
    amounts: Optional[Dict[int, float]] = None
