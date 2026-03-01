from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .database import Base, engine
from .models import User, LeaveRequest
from .schemas import UserCreate, LeaveCreate
from .auth import hash_password, verify_password, create_access_token
from .dependencies import get_db, get_current_user

app = FastAPI(title="Employee Leave Management API")

Base.metadata.create_all(bind=engine)


@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    return {"message": "User created"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401)
    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/apply-leave")
def apply_leave(leave: LeaveCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_leave = LeaveRequest(
        user_id=current_user.id,
        leave_type=leave.leave_type,
        start_date=leave.start_date,
        end_date=leave.end_date,
        reason=leave.reason
    )
    db.add(new_leave)
    db.commit()
    return {"message": "Leave applied"}


@app.get("/my-leaves")
def my_leaves(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(LeaveRequest).filter(LeaveRequest.user_id == current_user.id).all()
