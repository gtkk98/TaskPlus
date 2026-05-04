from fastapi import FastAPI

# Initialize the FastAPI
app = FastAPI()

# Create a route 
@app.get("/")
def read_root():
    return {"message": "Welcome to the TaskPulse API! The brain is online."}