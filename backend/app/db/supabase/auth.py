from app.db.supabase.supabase_client import supabase_client

async def login_with_github():
    result = supabase_client.auth.sign_in_with_oauth({
        "provider": "github",
        "options": {
            "redirect_to": "http://localhost:3000/home"
        }
    })
    return {"url": result.url}

async def login_with_discord():
    result = supabase_client.auth.sign_in_with_oauth({
        "provider": "discord",
        "options": {
            "redirect_to": "http://localhost:3000/home"
        }
    })
    return {"url": result.url}

async def logout(access_token: str):
    supabase_client.auth.set_session(access_token, refresh_token="")
    supabase_client.auth.sign_out()
    return {"message": "User logged out successfully"}
