from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from Utils import check_permissions

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users",status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@app.post("/records",status_code=201)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == record.user_id).first()

    if not user or not check_permissions(user.role, "create"):
        raise HTTPException(status_code=403, detail="Not allowed")

    if record.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    db_record = models.Record(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


@app.get("/records")
def get_records(user_id:int,db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == user_id).first()

    if not user or not check_permissions(user.role,"read"):
        raise HTTPException(status_code=403,detail="Not Allowed")
    
    return db.query(models.Record).all()

@app.delete("/records/{record_id}")
def delete_record(record_id: int, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user or not check_permissions(user.role, "delete"):
        raise HTTPException(status_code=403, detail="Not allowed")

    record = db.query(models.Record).filter(models.Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404,detail="Record not found")
    
    db.delete(record)
    db.commit()
    return {"message": "Deleted"}

@app.get("/summary")
def get_summary(user_id : int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user or not check_permissions(user.role, "summary"):
        raise HTTPException(status_code=403,detail = "Not allowed")
    
    records = db.query(models.Record).all()
    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income" : total_income,
        "total_expense" : total_expense,
        "balance" : total_income - total_expense
    }
