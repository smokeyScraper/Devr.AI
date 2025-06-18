from app.core.config import settings
from supabase import create_client

SUPABASE_URL = settings.supabase_url
SUPABASE_KEY = settings.supabase_key

supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_supabase_client():
    return supabase_client
