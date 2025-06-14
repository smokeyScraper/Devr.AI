from app.db.supabase.supabase_client import supabase_client
import os
def login_with_oauth(provider: str):
    try:
        result = supabase_client.auth.sign_in_with_oauth({
            "provider": provider,
            "options": {
                "redirect_to": os.getenv("SUPABASE_REDIRECT_URL", "http://localhost:3000/home")
            }
        })
        return {"url": result.url}
    except Exception as e:
        raise Exception(f"OAuth login failed for {provider}: {str(e)}")


def login_with_github():
    return login_with_oauth("github")

def login_with_discord():
    return login_with_oauth("discord")

def logout(access_token: str):
    try:
        supabase_client.auth.set_session(access_token, refresh_token="")
        supabase_client.auth.sign_out()
        return {"message": "User logged out successfully"}
    except Exception as e:
        raise Exception(f"Logout failed: {str(e)}")
