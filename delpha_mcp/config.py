"""
Configuration for Delpha MCP client and server.
Centralizes all URLs, scopes, and other constants.
"""

from pydantic import Field
from pydantic_settings import BaseSettings


class MCPConfig(BaseSettings):
    """Configuration for Delpha MCP client and server."""

    delpha_base_url: str = Field(
        "https://api-dev.delpha.io",
        validation_alias="DELPHA_BASE_URL",
        description="Base URL of the Delpha API",
    )
    delpha_token_url: str = Field(
        "https://secure-dev.delpha.io/oauth2/token",
        validation_alias="DELPHA_TOKEN_URL",
        description="URL of the Delpha OAuth2 token endpoint",
    )
    delpha_scope: str = Field(
        "api/access",
        validation_alias="DELPHA_SCOPE",
        description="Scope of the Delpha API",
    )
    openapi_url: str = Field(
        "https://delphadev-static-ressources.s3.eu-west-1.amazonaws.com/openapi.json",
        validation_alias="OPENAPI_URL",
        description="URL of the OpenAPI specification for the Delpha API",
    )
    delpha_client_id: str = Field(
        ..., validation_alias="DELPHA_CLIENT_ID", description="Delpha OAuth2 client ID"
    )
    delpha_client_secret: str = Field(
        ...,
        validation_alias="DELPHA_CLIENT_SECRET",
        description="Delpha OAuth2 client secret",
    )


config = MCPConfig()
