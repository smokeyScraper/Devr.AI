"""
API package for the Devr.AI backend.

This package contains all API-related components:
- router: Main API router with all endpoints
- v1: Version 1 API endpoints
"""

from .router import api_router

__all__ = ["api_router"]
