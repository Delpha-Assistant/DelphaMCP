#!/usr/bin/env python3
"""
Delpha Data Quality MCP Server using FastMCP OpenAPI integration

This server uses FastMCP's built-in OpenAPI integration to automatically generate
tools from the OpenAPI specification, following best practices.
"""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP
from authlib.integrations.httpx_client import AsyncOAuth2Client

# Load environment variables
load_dotenv()

class DelphaOAuthClient:
    """
    HTTP client for Delpha API with OAuth 2.0 support.
    
    This implements the interface expected by FastMCP's OpenAPI integration.
    """
    
    def __init__(self):
        self.base_url = "https://ao67qf61qk.execute-api.eu-west-1.amazonaws.com/prod"
        self.token_url = "https://secure-dev.delpha.io/oauth2/token"
        self.scope = "api/access"
        self.client_id = os.getenv("DELPHA_CLIENT_ID", "")
        self.client_secret = os.getenv("DELPHA_CLIENT_SECRET", "")
        
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "❌ OAuth credentials required! "
                "Set DELPHA_CLIENT_ID and DELPHA_CLIENT_SECRET environment variables."
            )
        
        # Create async OAuth2 client using Authlib
        self.client = AsyncOAuth2Client(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope
        )
        self.access_token = None
    
    async def _get_access_token(self) -> str:
        """Get OAuth 2.0 access token using client credentials flow."""
        try:
            print(" 🔐 Getting OAuth 2.0 access token...")
            
            # Get token using Authlib OAuth2Client
            token = await self.client.fetch_token(
                self.token_url,
                grant_type="client_credentials"
            )
            
            self.access_token = token.get("access_token")
            
            if not self.access_token:
                raise RuntimeError("No access token in response")
            
            print(" ✅ Access token obtained successfully")
            return self.access_token
                
        except Exception as e:
            print(f" ❌ Error getting access token: {e}")
            raise RuntimeError(f"Failed to authenticate with Delpha API: {e}")
    
    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """
        Make an authenticated request to the Delpha API.
        
        This method implements the interface expected by FastMCP's OpenAPI integration.
        It automatically handles OAuth token management.
        """
        # Combine base URL with the relative URL from OpenAPI
        if url.startswith('/'):
            full_url = f"{self.base_url}{url}"
        else:
            full_url = url
            
        print(f" 🔍 Making {method} request to: {full_url}")
        
        # Get authentication headers
        headers = kwargs.get("headers", {})
        headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        
        # Get OAuth token (will raise exception if it fails)
        token = await self._get_access_token()
        headers["Authorization"] = f"Bearer {token}"
        
        kwargs["headers"] = headers
        
        # Make the request using the async OAuth2 client
        try:
            print(f" 📤 Request payload: {kwargs.get('json', 'No JSON payload')}")
            response = await self.client.request(method, full_url, **kwargs)
            print(f" 📥 Response status: {response.status_code}")
            return response
        except Exception as e:
            print(f" ❌ Request failed: {e}")
            raise
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

def main():
    """Create and run the MCP server using OpenAPI integration."""
    print(" 🚀 Creating Delpha Data Quality MCP Server from OpenAPI...")
    
    try:
        # Load the OpenAPI specification
        script_dir = Path(__file__).parent
        openapi_path = script_dir / "openapi.json"
        
        with open(openapi_path, "r") as f:
            openapi_spec = json.load(f)
        
        # Create the OAuth-enabled HTTP client
        client = DelphaOAuthClient()
        
        # Create MCP server from OpenAPI spec
        server = FastMCP.from_openapi(
            openapi_spec=openapi_spec,
            client=client,
            name="delpha-data-quality"
        )
        
        # Print configuration info
        print(f" 📡 API Base URL: {client.base_url}")
        print(f"   - Client ID: {client.client_id[:8]}...")
        print(f"   - Token URL: {client.token_url}")
        
        # Run the server
        print(" 🚀 Starting MCP server...")
        server.run(transport="stdio")
        
    except ValueError as e:
        print(f" ❌ Configuration error: {e}")
        exit(1)
    except Exception as e:
        print(f" ❌ Failed to start server: {e}")
        exit(1)

if __name__ == "__main__":
    main() 
