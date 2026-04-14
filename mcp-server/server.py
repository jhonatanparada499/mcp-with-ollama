# server.py
from fastmcp import FastMCP
import subprocess

mcp = FastMCP("My First MCP Server")


@mcp.tool()
def get_running_config(container_name: str) -> str:
    """Gets the running config file of a frr in a docker container"""
    try:
        config = subprocess.run(
            ["docker", "exec", container_name, "vtysh", "-c", "show running-config"],
            capture_output=True,
            text=True,
            check=True,
        )
        return config.stdout
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr or str(e)
        return f"Error: {error_msg}"


if __name__ == "__main__":
    # Start the server
    mcp.run(
        transport="streamable-http",
        stateless_http=True,
        host="0.0.0.0",
        port=9090,
        path="/mcp",
    )
