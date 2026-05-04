from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import model
from database import engine, get_db

model.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI
app = FastAPI()

# Create a route 
@app.get("/")
def read_root():
    return {"message": "Welcome to the TaskPulse API! The brain is online."}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"message": "Database session successfully created!"}