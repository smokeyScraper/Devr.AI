#!/usr/bin/env python3
"""
Test script to verify GitHub MCP integration is working correctly

Make sure the GitHub MCP server is running on http://localhost:8001
"""

import asyncio
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def test_github_integration():
    """Test the GitHub integration"""
    try:
        print("Testing GitHub integration...")
        
        # Test the repository query tool
        from app.agents.devrel.github.tools.repository_query import handle_repo_query
        print("✓ Repository query tool import successful")
        
        # Test with AOSSIE-Org/Devr.AI repository
        print("\nTesting repository query for AOSSIE-Org/Devr.AI...")
        result = await handle_repo_query("Please fetch AOSSIE-Org/Devr.AI repository details.")
        
        print(f"Result: {result}")
        
        if result["status"] == "success":
            print("✓ Repository query successful!")
            print(f"Repository: {result['owner']}/{result['repo']}")
            if "data" in result and result["data"]:
                data = result["data"]
                # --- Core Info ---
                print(f"URL: {data.get('html_url', 'N/A')}")
                print(f"Description: {data.get('description', 'N/A')}")

                # --- Stats ---
                print(f"Stars: {data.get('stars', 'N/A')}")
                print(f"Forks: {data.get('forks', 'N/A')}")
                print(f"Watchers: {data.get('watchers', 'N/A')}")
                print(f"Open Issues: {data.get('open_issues', 'N/A')}")

                # --- NEW: Details ---
                print(f"Language: {data.get('language', 'N/A')}")
                # Join the list of topics into a comma-separated string for clean printing
                topics = ", ".join(data.get('topics', []))
                print(f"Topics: {topics if topics else 'N/A'}")
                print(f"License: {data.get('license', 'N/A')}")
                print(f"Default Branch: {data.get('default_branch', 'N/A')}")

                # --- NEW: Timestamps ---
                print(f"Created At: {data.get('created_at', 'N/A')}")
                print(f"Last Updated At: {data.get('updated_at', 'N/A')}")
                print(f"Last Pushed At: {data.get('pushed_at', 'N/A')}")
        else:
            print(f"✗ Repository query failed: {result.get('message', 'Unknown error')}")
            return False
        
        print("\nAll tests passed! GitHub MCP integration is working correctly.")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_github_integration())
    sys.exit(0 if success else 1)
