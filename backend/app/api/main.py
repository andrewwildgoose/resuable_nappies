from fastapi import FastAPI
from app.data.crud_example import get_test

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return get_test()