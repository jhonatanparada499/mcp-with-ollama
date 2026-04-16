# server.py
from fastmcp import FastMCP
import telnetlib
import time

mcp = FastMCP("My First MCP Server")


@mcp.tool()
def get_running_config() -> str:
    """Gets the running configuration file of a frr device router via telnet"""
    HOST = "127.0.0.1"
    PORT = 2323

    tn = telnetlib.Telnet(HOST, PORT, timeout=5)

    time.sleep(1)

    # command to show running config
    tn.write(b"show running-config\n")
    time.sleep(2)

    output = tn.read_very_eager().decode("utf-8")

    tn.write(b"exit\n")
    tn.close()

    return output


if __name__ == "__main__":
    # Start the server
    mcp.run(
        transport="streamable-http",
        stateless_http=True,
        host="0.0.0.0",
        port=9090,
        path="/mcp",
    )
