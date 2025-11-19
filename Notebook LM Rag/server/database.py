import os
from supabase import create_client, Client
from dotenv import load_dotenv


supabase_url = os.getenv("SUPABASE_API_URL")
supabase_service_key = os.getenv("SUPBASE_SERVICE_KEY")

if not supabase_url or not supabase_service_key:
    raise ValueError("SUPABASE_API_URL and SUPBASE_SERVICE_KEY must be set")

supabase: Client = create_client(supabase_url, supabase_service_key)