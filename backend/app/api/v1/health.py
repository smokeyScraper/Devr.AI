import logging
from fastapi import APIRouter, HTTPException
from app.database.weaviate.client import get_weaviate_client

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health")
async def health_check():
    """
    General health check endpoint to verify services are running.

    Returns:
        dict: Status of the application and its services
    """
    try:
        async with get_weaviate_client() as client:
            weaviate_ready = await client.is_ready()

        from main import app_instance

        return {
            "status": "healthy",
            "services": {
                "weaviate": "ready" if weaviate_ready else "not_ready",
                "discord_bot": "running" if app_instance.discord_bot and not app_instance.discord_bot.is_closed() else "stopped"
            }
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "error": str(e)
            }
        )


@router.get("/health/weaviate")
async def weaviate_health():
    """Check specifically Weaviate service health."""
    try:
        async with get_weaviate_client() as client:
            is_ready = await client.is_ready()

        return {
            "service": "weaviate",
            "status": "ready" if is_ready else "not_ready"
        }
    except Exception as e:
        logger.error(f"Weaviate health check failed: {e}")
        raise HTTPException(
            status_code=503,
            detail={
                "service": "weaviate",
                "status": "unhealthy",
                "error": str(e)
            }
        )


@router.get("/health/discord")
async def discord_health():
    """Check specifically Discord bot health."""
    try:
        from main import app_instance

        bot_status = "running" if app_instance.discord_bot and not app_instance.discord_bot.is_closed() else "stopped"

        return {
            "service": "discord_bot",
            "status": bot_status
        }
    except Exception as e:
        logger.error(f"Discord bot health check failed: {e}")
        raise HTTPException(
            status_code=503,
            detail={
                "service": "discord_bot",
                "status": "unhealthy",
                "error": str(e)
            }
        )
