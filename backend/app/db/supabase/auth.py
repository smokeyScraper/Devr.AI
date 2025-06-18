import asyncio
from app.db.supabase.supabase_client import supabase_client


async def login_with_oauth(provider: str):
    try:
        result = await asyncio.to_thread(
            supabase_client.auth.sign_in_with_oauth,
            {"provider": provider}
        )
        return {"url": result.url}
    except Exception as e:
        raise Exception(f"OAuth login failed for {provider}") from e

async def login_with_github():
    return await login_with_oauth("github")

async def login_with_discord():
    return await login_with_oauth("discord")

async def login_with_slack():
    return await login_with_oauth("slack")

async def logout(access_token: str):
    try:
        supabase_client.auth.set_session(access_token, refresh_token="")
        supabase_client.auth.sign_out()
        return {"message": "User logged out successfully"}
    except Exception as e:
        raise Exception(f"Logout failed: {str(e)}")
