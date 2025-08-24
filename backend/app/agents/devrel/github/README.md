# GitHub Integration for Devr.AI

This directory contains the GitHub integration components for the Devr.AI backend.

## Architecture

The GitHub integration uses a **Model Context Protocol (MCP) server** approach:

### MCP Server Architecture
- **File**: `services/github_mcp_server.py`
- **How it works**: Runs as a separate FastAPI server that provides GitHub repository information
- **Benefits**: Modular, can be used by other applications, follows MCP standards
- **Usage**: Requires running the MCP server separately

### MCP Client
- **File**: `services/github_mcp_client.py`
- **Class**: `GitHubMCPClient`
- **How it works**: Communicates with the MCP server via HTTP to get repository information
- **Benefits**: Clean separation of concerns, server can be restarted independently

## Components

### Core Files

- **`github_mcp_service.py`**: Core GitHub API service using the GitHub REST API
- **`github_mcp_client.py`**: Client for both direct and MCP server communication
- **`tools/repository_query.py`**: Tool that handles repository queries from user requests
- **`github_toolkit.py`**: Main entry point that routes queries to appropriate tools

### How It Works

1. **User Query**: User asks about a repository (e.g., "Tell me about AOSSIE-Org/Devr.AI")
2. **Intent Classification**: The GitHub toolkit classifies the intent as "repo_support"
3. **Tool Execution**: Routes to `handle_repo_query` function
4. **Repository Parsing**: Extracts owner/repo from the query using regex
5. **GitHub API Call**: Uses the GitHub service to fetch repository data
6. **Response**: Returns formatted repository information

## Setup

### Environment Variables

Make sure you have the following environment variable set:
```bash
GITHUB_TOKEN=your_github_personal_access_token
```

### Starting the MCP Server

1. **Start the GitHub MCP server**:
```bash
cd backend
python start_github_mcp_server.py
```

The server will run on `http://localhost:8001`

2. **Verify the server is running**:
```bash
curl http://localhost:8001/health
```

### Testing

Run the test script to verify the integration:
```bash
cd backend
python test_github_integration.py
```

Or test the specific tool:
```bash
cd backend
python -m app.agents.devrel.github.test_repo_query
```

## Example Usage

When a user asks: "Please fetch AOSSIE-Org/Devr.AI repository details"

The system will:
1. Parse "AOSSIE-Org" as owner and "Devr.AI" as repository
2. Call GitHub API to get repository information
3. Return structured data including:
   - Repository name and description
   - Star count, fork count, open issues
   - Repository URL

## Integration with Devr Bot

The GitHub integration is automatically available through the Devr bot when users ask about GitHub repositories. The bot will:

1. Recognize GitHub-related queries
2. Route them to the appropriate GitHub tools
3. Return formatted responses with repository information
4. Not use Google API for repository queries (as requested)

## Error Handling

The integration includes comprehensive error handling:
- Invalid repository format
- GitHub API errors
- Missing authentication tokens
- Network connectivity issues

All errors are gracefully handled and return user-friendly error messages.
