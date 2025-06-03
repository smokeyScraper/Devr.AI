import logging
from typing import List, Dict, Any
from tavily import TavilyClient
from app.core.config import settings

logger = logging.getLogger(__name__)

class TavilySearchTool:
    """Tavily web search integration"""

    def __init__(self):
        self.client = TavilyClient(api_key=settings.tavily_api_key) if settings.tavily_api_key else None

    async def search(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """Perform web search using Tavily"""
        try:
            if not self.client:
                logger.warning("Tavily API key not configured")
                return []

            response = self.client.search(
                query=query,
                search_depth="basic",
                max_results=max_results
            )

            results = []
            for result in response.get("results", []):
                results.append({
                    "title": result.get("title", ""),
                    "content": result.get("content", ""),
                    "url": result.get("url", ""),
                    "score": result.get("score", 0)
                })

            logger.info(f"Search for '{query}' returned {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Error performing search: {str(e)}")
            return []
