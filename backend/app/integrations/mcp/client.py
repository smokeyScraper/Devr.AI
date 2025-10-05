import os
import json
import asyncio
from typing import Any, Dict, Optional

try:
    import aiohttp
except Exception:  # pragma: no cover
    aiohttp = None  # lazy import guard for environments without aiohttp

DEFAULT_TIMEOUT = 15

class MCPClientError(Exception):
    pass

class MCPClient:
    """Minimal async MCP client over HTTP.

    Exposes a simple call(method, params) that posts JSON to the MCP server.
    """

    def __init__(self, server_url: Optional[str] = None, api_key: Optional[str] = None):
        self.server_url = server_url or os.getenv("MCP_SERVER_URL")
        self.api_key = api_key or os.getenv("MCP_API_KEY")

    def available(self) -> bool:
        return bool(self.server_url) and aiohttp is not None

    async def call(self, method: str, params: Dict[str, Any], timeout: int = DEFAULT_TIMEOUT) -> Dict[str, Any]:
        if not self.available():
            raise MCPClientError("MCP not configured or aiohttp missing")

        payload = {"method": method, "params": params}
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.server_url, headers=headers, json=payload, timeout=timeout) as resp:
                    text = await resp.text()
                    if resp.status >= 400:
                        raise MCPClientError(f"MCP HTTP {resp.status}: {text}")
                    try:
                        data = json.loads(text)
                    except json.JSONDecodeError:
                        raise MCPClientError("MCP returned invalid JSON")
                    return data
            except asyncio.TimeoutError as e:
                raise MCPClientError(f"MCP timeout: {str(e)}")

