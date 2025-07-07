from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel
from app.core.auth import create_access_token, decode_access_token
from app.core.config import MONGO_URI
from passlib.hash import bcrypt
from pymongo import MongoClient
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
client = MongoClient(MONGO_URI)
db = client.skillbridge

class User(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(user: User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    hashed = bcrypt.hash(user.password)
    db.users.insert_one({**user.dict(), "password": hashed})
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(req: LoginRequest):
    user = db.users.find_one({"email": req.email})
    if not user or not bcrypt.verify(req.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": req.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_user_profile(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.users.find_one({"email": payload['sub']}, {"password": 0})
    return user
