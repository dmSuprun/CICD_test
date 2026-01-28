from fastapi import FastAPI
from app.service import add, is_even

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CI/CD FastAPI is working"}


@app.get("/add")
def add_numbers(a: int, b: int):
    result = add(a, b)
    return {"result": result}


@app.get("/even/{number}")
def check_even(number: int):
    return {"is_even": is_even(number)}