from fastapi import FastAPI
from .api import users_router
from .database import engine
from .models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Alembic Tutorial API", version="1.0.0")

# Include routers
app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Alembic base!"}
