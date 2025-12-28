# app/main.py
from fastapi import FastAPI

app = FastAPI(title="FastAPI Sample")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

