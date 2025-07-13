from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ClientBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "active"

class ProjectCreate(ProjectBase):
    client_id: int

class Project(ProjectBase):
    id: int
    client_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    invoice_number: str
    amount: float
    status: str = "pending"
    due_date: Optional[date] = None

class InvoiceCreate(InvoiceBase):
    client_id: int
    project_id: Optional[int] = None

class Invoice(InvoiceBase):
    id: int
    client_id: int
    project_id: Optional[int] = None
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True