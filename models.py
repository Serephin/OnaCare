from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
from datetime import datetime
from typing import Optional


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    doctor_name=Column(String)
    doctor_phone=Column(String)
    week_of_pregnancy = Column(Integer, nullable=True)
    hospital_name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    emergency_contact_name = Column(String, nullable=True)
    emergency_contact_phone = Column(String, nullable=True)
    metrics = relationship("HealthMetric", back_populates="user")





class HealthMetric(Base):
    __tablename__ = "health_metrics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    blood_pressure = Column(String, nullable=True)
    weight = Column(Float, nullable=True)
    fetal_heart_rate = Column(Integer, nullable=True)
    recorded_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    age = Column(Integer, nullable=True)
    systolic_bp = Column(Integer, nullable=True)
    diastolic_bp = Column(Integer, nullable=True)
    blood_sugar = Column(Float, nullable=True)
    body_temp = Column(Float, nullable=True)
    heart_rate = Column(Integer, nullable=True)
    gestational_age = Column(Integer, nullable=True)
    kick_count = Column(Integer, nullable=True)
    contraction_frequency = Column(Integer, nullable=True)
    fluid_intake = Column(Float, nullable=True)
    risk_level = Column(String, nullable=True)

    user = relationship("User", back_populates="metrics")
