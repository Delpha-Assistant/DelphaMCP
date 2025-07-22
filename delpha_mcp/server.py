"""
Delpha MCP Server entrypoint.
"""

import logging

import httpx
from fastmcp import FastMCP

from .client import DelphaOAuthClient
from .config import config

logger = logging.getLogger("delpha_mcp.server")


def run_server() -> None:
    """
    Create and run the MCP server using OpenAPI integration.
    """
    logger.info("🚀 Creating Delpha Data Quality MCP Server from OpenAPI...")
    try:
        # Load the OpenAPI specification from a URL
        logger.info(f"💡 Fetching OpenAPI spec from {config.openapi_url}")
        response = httpx.get(config.openapi_url)
        response.raise_for_status()
        openapi_spec = response.json()

        # Create the OAuth-enabled HTTP client
        client = DelphaOAuthClient()

        # Create MCP server from OpenAPI spec
        server = FastMCP.from_openapi(
            openapi_spec=openapi_spec,
            client=client,
            name="delpha-data-quality",
        )

        # Run the server
        logger.info("🚀 Starting MCP server...")
        server.run(transport="stdio")

    except ValueError as e:
        logger.error(f"❌ Configuration error: {e}")
        exit(1)
    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        exit(1)
