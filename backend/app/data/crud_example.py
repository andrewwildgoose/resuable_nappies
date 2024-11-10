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
    return supabase.auth.sign_up({
            'email': email,
            'password': password,
        })

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
    return supabase.auth.sign_out()

def sp_get_user():
    print(supabase.auth.get_user())
    return supabase.auth.get_user()

def sp_start_subscription(user):
    user_id = user.user.id
    print(user_id)
    return supabase.from_("Subscriptions").insert([{"user_id": user_id, "active": "TRUE"}]).execute()