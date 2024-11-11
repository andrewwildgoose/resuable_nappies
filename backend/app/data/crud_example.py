from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client

url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')
JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
supabase: Client = create_client(url, key)

def sp_get_test():
    return supabase.from_("Test").select("*").execute()

def sp_add_test_value(value: str):
    return supabase.from_("Test").insert([{"value": value}]).execute()

def sp_signup(email: str, password: str):
    sign_up_response = supabase.auth.sign_up({
            'email': email,
            'password': password,
        })
    return sign_up_response


def sp_signin(email: str, password: str):
    try:
        session = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })

        return session  # Contains the JWT token
    except Exception as e:
        raise Exception(f"Sign-in failed: {str(e)}")

def sp_logout():
    log_out_response = supabase.auth.sign_out()
    return log_out_response

def sp_get_user():
    user = supabase.auth.get_user()
    return user

def sp_start_subscription(user):
    user_id: str = user.user.id
    data = [{"user_id": user_id, "active": "TRUE"}]
    response = (supabase.table("Subscriptions").insert(data).execute())
    return response