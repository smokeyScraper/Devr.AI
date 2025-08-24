import asyncio
from .tools.repository_query import handle_repo_query

async def main():
    print("Testing GitHub repository query...")
    res = await handle_repo_query("Please fetch AOSSIE-Org/Devr.AI repository details.")
    print(f"Result: {res}")
    
    if res["status"] == "success":
        print("✓ Query successful!")
        data = res["data"]
        print(f"Repository: {res['owner']}/{res['repo']}")
        print(f"Description: {data.get('description', 'N/A')}")
        print(f"Stars: {data.get('stars', 'N/A')}")
        print(f"Forks: {data.get('forks', 'N/A')}")
        print(f"Open Issues: {data.get('open_issues', 'N/A')}")
    else:
        print(f"✗ Query failed: {res.get('message', 'Unknown error')}")

if __name__ == "__main__":
    asyncio.run(main())
