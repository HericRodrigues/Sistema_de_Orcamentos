from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, Depends, Query 
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.services import auth
from app.schemas import user as schemas


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=schemas.UserOut)
def register(
    user: schemas.UserCreate, 
     local_kw: str = Query(None),
    db: Session = Depends(database.SessionLocal)):
    return auth.create_user(db, user)
