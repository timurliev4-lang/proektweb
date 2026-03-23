from fastapi import FastAPI
from proekt320Kalegin import funk320Kalegin

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Gruppa 640"}

@app.get("/funcKalegin")
def get_funcKalegin(x: int, y: int):
    return {"result": funk320Kalegin(x, y)}