from fastapi import FastAPI, Form, Request, HTTPException, Response, Depends
from fastapi.security import HTTPBearer
from app.data.crud_example import sp_get_test, sp_add_test_value, sp_signup, sp_signin, sp_logout, sp_get_user, sp_start_subscription
import os
from jwt import JWT

app = FastAPI()


from supabase import create_client, Client

url: str = os.environ.get('SUPABASE_URL')
key: str = os.environ.get('SUPABASE_KEY')
JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
supabase: Client = create_client(url, key)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/test")
async def test():
    return sp_get_test()

@app.post("/api/test/new")
async def test(value: str = Form()):
    try:
        sp_add_test_value(value)
        return {"message": "Successfully added value"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/signup")
async def signup(email: str = Form(), password: str = Form()):
    try:
        auth_response = sp_signup(email, password)
        return {"message": f"Successfully signed up: {auth_response}"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/signin")
async def signin(response: Response, email: str = Form(), password: str = Form()):
    try:
        session = sp_signin(email, password)
        access_token = session.session.access_token

        # Set JWT token in a secure HTTP-only cookie
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax"
        )
        return {"success": True, "user": session.user}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.post("/api/logout")
async def logout(response: Response):
    try:
        logout_response = sp_logout()
        # Clear the session cookie by deleting it
        response.delete_cookie("access_token")
        return {"message": f"Successfully logged out: {logout_response}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/user")
async def get_user_info():
    try:
        user_info = sp_get_user()
        return user_info
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@app.post("/api/start_subscription")
async def start_subscription(response: Response):
    try:
        user = sp_get_user()
        subscription_response = sp_start_subscription(user)
        return {"message": f"Successfully subscribed: {subscription_response}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))