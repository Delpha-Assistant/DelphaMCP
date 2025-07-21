# Delpha Data Quality MCP Server

Email data quality assessment for MCP-compatible tools like Cursor. Validate emails, get quality scores, and receive suggestions.

## Quick Setup

### 1. Install the Package
```bash
pip install delpha-mcp
```

### 2. Configure Cursor (or other MCP tool)

Go to Cursor Settings → MCP and add this configuration:

```json
{
  "Delpha": {
    "command": "python3",
    "args": ["-m", "delpha_mcp"],
    "env": {
      "DELPHA_CLIENT_ID": "your_client_id_here",
      "DELPHA_CLIENT_SECRET": "your_client_secret_here"
    }
  }
}
```

**Replace:**
- `your_client_id_here` and `your_client_secret_here` with your Delpha credentials

### 3. Restart Cursor

That's it! 🚀 The Delpha tools are now available in your MCP environment.

## Available Tools

- **`submitEmailAssessment`**: Submit an email for quality assessment
- **`getEmailAssessmentStatus`**: Get assessment results by job ID




## Get Credentials

Contact Delpha to get your OAuth 2.0 client credentials for API access.
