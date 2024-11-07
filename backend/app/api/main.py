from fastapi import FastAPI, Form
from app.data.crud_example import get_test, add_test_value, signup


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return get_test()

@app.post("/api/test/new")
async def test(value: str = Form()):
    try:
        add_test_value(value)
        return {"message": "Successfully added value"}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/api/signup")
async def signup(email: str = Form(), password: str = Form()):
    try:
        auth_response: str = signup(email, password)
        return {"message": f"Successfully signed up: {auth_response}"}
    except Exception as e:
        return {"error": str(e)}
