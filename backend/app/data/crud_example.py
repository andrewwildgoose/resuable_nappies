from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client

url: str = os.environ.get('SUPABASE_URL')
key: str = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(url, key)

def get_test():
    return supabase.from_("Test").select("*").execute()

def add_test_value(value: str):
    return supabase.from_("Test").insert([{"value": value}]).execute()

def signup(email: str, password: str):
    return supabase.auth.sign_up(email, password)