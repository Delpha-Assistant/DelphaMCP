"""
Delpha Data Quality MCP Server Entrypoint
"""

import logging

from .server import run_server


def main():
    """
    Entrypoint for running the Delpha MCP server.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    run_server()


if __name__ == "__main__":
    main()
