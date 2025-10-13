import logging
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List
from app.database.supabase.client import get_supabase_client
from app.models.integration import (
    IntegrationCreateRequest,
    IntegrationUpdateRequest,
    IntegrationResponse,
    IntegrationStatusResponse
)

logger = logging.getLogger(__name__)


class IntegrationService:
    """Service for registering organizations (stores org info only)."""

    def __init__(self):
        self.supabase = get_supabase_client()

    async def create_integration(
        self,
        user_id: UUID,
        request: IntegrationCreateRequest
    ) -> IntegrationResponse:
        """Register a new organization."""
        try:
            # Check if integration already exists
            existing = await self.supabase.table("organization_integrations")\
                .select("*")\
                .eq("user_id", str(user_id))\
                .eq("platform", request.platform)\
                .execute()

            if existing.data:
                raise ValueError(f"Integration for {request.platform} already exists")

            # Create integration record (just org metadata)
            integration_data = {
                "id": str(uuid4()),
                "user_id": str(user_id),
                "platform": request.platform,
                "organization_name": request.organization_name,
                "is_active": True,
                "config": request.config or {},
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }

            # Store organization link if provided
            if request.organization_link:
                integration_data["config"]["organization_link"] = request.organization_link

            result = await self.supabase.table("organization_integrations")\
                .insert(integration_data)\
                .execute()

            if not result.data:
                raise Exception("Failed to create integration")

            logger.info(f"Registered organization: {request.organization_name} ({request.platform})")

            return IntegrationResponse(**result.data[0])

        except Exception as e:
            logger.error(f"Error creating integration: {str(e)}")
            raise

    async def get_integrations(self, user_id: UUID) -> List[IntegrationResponse]:
        """Get all integrations for a user."""
        try:
            result = await self.supabase.table("organization_integrations")\
                .select("*")\
                .eq("user_id", str(user_id))\
                .execute()

            return [IntegrationResponse(**item) for item in result.data]

        except Exception as e:
            logger.error(f"Error getting integrations: {str(e)}")
            raise

    async def get_integration(self, user_id: UUID, integration_id: UUID) -> Optional[IntegrationResponse]:
        """Get a specific integration."""
        try:
            result = await self.supabase.table("organization_integrations")\
                .select("*")\
                .eq("id", str(integration_id))\
                .eq("user_id", str(user_id))\
                .execute()

            if not result.data:
                return None

            return IntegrationResponse(**result.data[0])

        except Exception as e:
            logger.error(f"Error getting integration: {str(e)}")
            raise

    async def get_integration_by_platform(
        self,
        user_id: UUID,
        platform: str
    ) -> Optional[IntegrationResponse]:
        """Get an integration by platform."""
        try:
            result = await self.supabase.table("organization_integrations")\
                .select("*")\
                .eq("user_id", str(user_id))\
                .eq("platform", platform)\
                .execute()

            if not result.data:
                return None

            return IntegrationResponse(**result.data[0])

        except Exception as e:
            logger.error(f"Error getting integration by platform: {str(e)}")
            raise

    async def update_integration(
        self,
        user_id: UUID,
        integration_id: UUID,
        request: IntegrationUpdateRequest
    ) -> IntegrationResponse:
        """Update an existing integration."""
        try:
            update_data = {"updated_at": datetime.now().isoformat()}

            if request.organization_name is not None:
                update_data["organization_name"] = request.organization_name

            if request.is_active is not None:
                update_data["is_active"] = request.is_active

            if request.config is not None:
                update_data["config"] = request.config

            if request.organization_link is not None:
                if "config" not in update_data:
                    # Get existing config first
                    existing = await self.get_integration(user_id, integration_id)
                    update_data["config"] = existing.config or {}
                update_data["config"]["organization_link"] = request.organization_link

            result = await self.supabase.table("organization_integrations")\
                .update(update_data)\
                .eq("id", str(integration_id))\
                .eq("user_id", str(user_id))\
                .execute()

            if not result.data:
                raise Exception("Integration not found or update failed")

            logger.info(f"Updated integration {integration_id}")

            return IntegrationResponse(**result.data[0])

        except Exception as e:
            logger.error(f"Error updating integration: {str(e)}")
            raise

    async def delete_integration(self, user_id: UUID, integration_id: UUID) -> bool:
        """Delete an integration."""
        try:
            await self.supabase.table("organization_integrations")\
                .delete()\
                .eq("id", str(integration_id))\
                .eq("user_id", str(user_id))\
                .execute()

            logger.info(f"Deleted integration {integration_id}")

            return True

        except Exception as e:
            logger.error(f"Error deleting integration: {str(e)}")
            raise

    async def get_integration_status(
        self,
        user_id: UUID,
        platform: str
    ) -> IntegrationStatusResponse:
        """Get the status of an integration for a specific platform."""
        try:
            integration = await self.get_integration_by_platform(user_id, platform)

            if not integration:
                return IntegrationStatusResponse(
                    platform=platform,
                    is_connected=False
                )

            return IntegrationStatusResponse(
                platform=platform,
                is_connected=integration.is_active,
                organization_name=integration.organization_name,
                last_updated=integration.updated_at
            )

        except Exception as e:
            logger.error(f"Error getting integration status: {str(e)}")
            raise

    async def get_all_integrations_for_platform(self, platform: str) -> List[IntegrationResponse]:
        """Get all registered organizations for a platform (useful for bot to know which orgs to serve)."""
        try:
            result = await self.supabase.table("organization_integrations")\
                .select("*")\
                .eq("platform", platform)\
                .eq("is_active", True)\
                .execute()

            return [IntegrationResponse(**item) for item in result.data]

        except Exception as e:
            logger.error(f"Error getting all integrations for platform: {str(e)}")
            raise


# Singleton instance
integration_service = IntegrationService()
