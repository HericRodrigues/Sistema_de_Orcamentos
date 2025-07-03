from fastapi import FastAPI
from app.routes import user
from app.database import create_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(user.router)