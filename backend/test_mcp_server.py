#!/usr/bin/env python3
"""
Test script to verify the GitHub MCP server can be imported and configured
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_mcp_server_import():
    """Test that the MCP server can be imported"""
    try:
        print("Testing MCP server import...")
        
        # Test importing the MCP server
        from app.agents.devrel.github.services.github_mcp_server import app
        print("✓ MCP server import successful")
        
        # Test that the app has the expected endpoints
        routes = [route.path for route in app.routes]
        expected_routes = ["/health", "/mcp", "/repo_info"]
        
        for route in expected_routes:
            if route in routes:
                print(f"✓ Route {route} found")
            else:
                print(f"✗ Route {route} not found")
                return False
        
        print("\nAll MCP server tests passed!")
        print("You can now start the server with: python start_github_mcp_server.py")
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
    success = test_mcp_server_import()
    sys.exit(0 if success else 1)
