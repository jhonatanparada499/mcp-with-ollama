# mcp_server.py
from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("My First MCP Server")


# Define Tool 1: Add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


# Define Tool 2: Greet someone
@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Welcome!"


if __name__ == "__main__":
    # Start the server
    mcp.run(transport="sse", port=8080)
