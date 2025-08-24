from ..services.github_mcp_client import GitHubMCPClient
import re

OWNER_REPO_RE = re.compile(r"([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")

async def handle_repo_query(user_query: str) -> dict:
    m = OWNER_REPO_RE.search(user_query)
    if not m:
        return {"status": "error", "message": "Usage: include owner/repo in query."}

    owner, repo = m.group(1), m.group(2)
    
    # Use the GitHub MCP client to communicate with the MCP server
    async with GitHubMCPClient() as client:
        if not await client.is_server_available():
            return {
                "status": "error", 
                "message": "GitHub MCP server not available. Please ensure the MCP server is running."
            }
        
        result = await client.get_repo_info(owner, repo)
        
        if "error" in result:
            return {
                "status": "error", 
                "owner": owner, 
                "repo": repo, 
                "message": result["error"]
            }
        
        return {
            "status": "success", 
            "owner": owner, 
            "repo": repo, 
            "data": result
        }
