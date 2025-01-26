from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import Base, SessionLocal, engine
from models import User, HealthMetric, UserRole
from datetime import datetime
from schemas import UserCreate, UserResponse, HealthMetricCreate, HealthMetricResponse

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User CRUD operations
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        week_of_pregnancy =user.week_of_pregnancy,
        doctor_name=user.doctor_name,
        doctor_phone=user.doctor_phone,  
      
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


@app.get("/users/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

from predict import predict_risk
# Health metrics CRUD operations
@app.post("/health-metrics/", response_model=HealthMetricResponse)
def create_health_metric(metric: HealthMetricCreate, db: Session = Depends(get_db)):
    # Verify user exists
    user = db.query(User).filter(User.id == metric.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Predict the risk level
    risk_level = predict_risk(
        blood_pressure=metric.blood_pressure,
        weight=metric.weight,
        fetal_heart_rate=metric.fetal_heart_rate,
        systolic_bp=metric.systolic_bp,
        diastolic_bp=metric.diastolic_bp
    ) or "low"  # Fallback to "low" if `predict_risk` returns None

    # Create the HealthMetric object
    db_metric = HealthMetric(
        user_id=metric.user_id,
        blood_pressure=int(metric.blood_pressure),
        weight=metric.weight,
        fetal_heart_rate=metric.fetal_heart_rate,
        age=metric.age,
        systolic_bp=metric.systolic_bp,
        diastolic_bp=metric.diastolic_bp,
        blood_sugar=metric.blood_sugar,
        body_temp=metric.body_temp,
        heart_rate=metric.heart_rate,
        gestational_age=metric.gestational_age,
        kick_count=metric.kick_count,
        contraction_frequency=metric.contraction_frequency,
        fluid_intake=metric.fluid_intake,
        risk_level=risk_level  # Add the predicted risk level here
    )
    
    # Commit to the database
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    
    return db_metric



@app.get("/health-metrics/{user_id}", response_model=List[HealthMetricResponse])
def get_user_health_metrics(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    metrics = db.query(HealthMetric).filter(HealthMetric.user_id == user_id).all()
    return metrics
