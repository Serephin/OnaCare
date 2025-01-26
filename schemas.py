from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HealthMetricBase(BaseModel):
    age: int
    systolic_bp: Optional[int] = None
    diastolic_bp: Optional[int] = None
    blood_sugar: Optional[float] = None
    body_temp: Optional[float] = None
    heart_rate: Optional[int] = None
    weight: Optional[float] = None
    gestational_age: Optional[int] = None
    fetal_heart_rate: Optional[float] = None
    kick_count: Optional[int] = None
    contraction_frequency: Optional[int] = None
    fluid_intake: Optional[float] = None
    risk_level: Optional[str] = 'Low'

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    doctor_name: str  # Added type annotation
    doctor_phone: str  # Added type annotation
    week_of_pregnancy: int  # Added type annotation
    address: Optional[str] = None
    phone_number: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    phone_number: Optional[str] = None
    doctor_name: str  # Added type annotation
    doctor_phone: str  # Added type annotation
    week_of_pregnancy: int  # Added type annotation
    hospital_name: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True


class HealthMetricCreate(BaseModel):
    user_id: int
    blood_pressure: Optional[str] = None
    weight: Optional[float] = None
    fetal_heart_rate: Optional[int] = None
    # New fields for metrics
    age: Optional[int] = None
    systolic_bp: Optional[int] = None
    diastolic_bp: Optional[int] = None
    blood_sugar: Optional[float] = None
    body_temp: Optional[float] = None
    heart_rate: Optional[int] = None
    gestational_age: Optional[int] = None
    kick_count: Optional[int] = None
    contraction_frequency: Optional[int] = None
    fluid_intake: Optional[float] = None
    risk_level: Optional[str] = 'Low'


class HealthMetricResponse(BaseModel):
    id: int
    user_id: int
    blood_pressure: Optional[str] = None
    weight: Optional[float] = None
    fetal_heart_rate: Optional[int] = None
    recorded_at: datetime
    age: Optional[int] = None
    systolic_bp: Optional[int] = None
    diastolic_bp: Optional[int] = None
    blood_sugar: Optional[float] = None
    body_temp: Optional[float] = None
    heart_rate: Optional[int] = None
    gestational_age: Optional[int] = None
    kick_count: Optional[int] = None
    contraction_frequency: Optional[int] = None
    fluid_intake: Optional[float] = None
    risk_level: Optional[str] = 'Low'

    class Config:
        from_attributes = True
