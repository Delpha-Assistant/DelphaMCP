"""
Delpha OAuth2 HTTP client for API access.
"""

import logging

import httpx
from authlib.integrations.httpx_client import AsyncOAuth2Client

from .config import config

logger = logging.getLogger("delpha_mcp.client")


class DelphaOAuthClient:
    """OAuth2 HTTP client for Delpha API, compatible with FastMCP."""

    def __init__(self):
        """Initialize the Delpha OAuth client."""

        self.client = AsyncOAuth2Client(
            client_id=config.delpha_client_id,
            client_secret=config.delpha_client_secret,
            scope=config.delpha_scope,
        )
        self.access_token = None

    async def _get_access_token(self) -> str:
        """
        Obtain an OAuth2 access token using client credentials flow.

        :return: The access token
        """
        try:
            logger.info("🔐 Getting OAuth 2.0 access token...")
            token = await self.client.fetch_token(
                config.delpha_token_url, grant_type="client_credentials"
            )
            self.access_token = token.get("access_token")
            if not self.access_token:
                logger.error("❌ No access token in response")
                raise RuntimeError("No access token in response")
            logger.info("✅ Access token obtained successfully")
            return self.access_token
        except Exception as e:
            logger.error(f"❌ Error getting access token: {e}")
            raise RuntimeError(f"Failed to authenticate with Delpha API: {e}")

    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Make an authenticated request to the Delpha API.

        :param method: The HTTP method to use
        :param url: The URL to request
        :return: The response from the Delpha API
        """
        if url.startswith("/"):
            full_url = f"{config.delpha_base_url}{url}"
        else:
            full_url = url
        logger.info(f"🔍 Making {method} request to: {full_url}")
        headers = kwargs.get("headers", {})
        headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )
        token = await self._get_access_token()
        headers["Authorization"] = f"Bearer {token}"
        kwargs["headers"] = headers
        try:
            logger.debug(f"📤 Request payload: {kwargs.get('json', 'No JSON payload')}")
            response = await self.client.request(method, full_url, **kwargs)
            logger.info(f"📥 Response status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"❌ Request failed: {e}")
            raise

    async def close(self):
        """Close the HTTP client session."""
        await self.client.aclose()
