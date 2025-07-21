# Delpha Data Quality MCP Server

This is a FastMCP server that provides access to the Delpha Data Quality API for email assessment. It follows FastMCP best practices for OAuth 2.0 client credentials flow and automatically generates tools from the OpenAPI specification.

## Features

- **Email Assessment**: Submit emails for data quality assessment
- **Job Tracking**: Monitor assessment progress with job IDs
- **Comprehensive Results**: Get detailed scores across multiple dimensions:
  - Accuracy
  - Validity
  - Completeness
  - Consistency
- **Email Suggestions**: Receive alternative email suggestions
- **Domain Analysis**: Analyze email and website domains

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure OAuth 2.0 Credentials

Since the Delpha API is fully protected, you need OAuth 2.0 credentials. Create a `.env` file:

```bash
cp env.example .env
```

Then edit `.env` and add your OAuth 2.0 credentials:

```
DELPHA_CLIENT_ID=your_actual_client_id_here
DELPHA_CLIENT_SECRET=your_actual_client_secret_here
```

### 3. Run the MCP Server

```bash
python fastmcp_delpha_server.py
```

The server will start and display:
```
 🚀 Creating Delpha Data Quality MCP Server...
 📡 API Base URL: https://ao67qf61qk.execute-api.eu-west-1.amazonaws.com/prod
 🔐 OAuth 2.0 configured: Yes/No
   - Client ID: abc12345...
   - Token URL: https://secure-dev.delpha.io/oauth2/token
 🛠️ Available tools (auto-generated from OpenAPI):
   - submitEmailAssessment
   - getEmailAssessmentStatus
 🚀 Starting MCP server...
```

## Available Tools

The MCP server automatically creates tools from the OpenAPI specification using FastMCP's built-in OpenAPI integration:

### 1. `submitEmailAssessment`

Submit an email for data quality assessment.

**Parameters:**
- `email` (required): The email address to assess
- `first_name` (optional): First name
- `last_name` (optional): Last name
- `website` (optional): Website URL

**Returns:** Job ID and submission status

### 2. `getEmailAssessmentStatus`

Check the status and get results of an assessment job.

**Parameters:**
- `job_id` (required): The job ID from the submission

**Returns:** Assessment results or current status

**Note:** Tool names are automatically generated from the OpenAPI `operationId` fields. The server uses FastMCP's OpenAPI integration to automatically create tools with proper parameter validation and response handling.

## Usage Examples

### Basic Email Assessment

```python
# Submit an email for assessment
result = await submitEmailAssessment(
    email="john.doe@company.com",
    first_name="John",
    last_name="Doe",
    website="https://company.com"
)

# Get the job ID
job_id = result["job_id"]

# Check results
assessment = await getEmailAssessmentStatus(job_id=job_id)
```

**Note:** The tools are automatically created from the OpenAPI specification, so the exact parameter names and return values match the API documentation.

## Response Format

### Email Assessment Result

```json
{
  "label": "No",
  "normalized_value": "test@example.com",
  "provider": "Example Provider",
  "email_domain": "example.com",
  "email_domain_qualification": "nominative@pro",
  "email_status": "Invalid",
  "suggestions": [
    {
      "value": "suggested@email.com",
      "score": 0.85
    }
  ],
  "website_domain": "company.com",
  "website_domain_qualification": "nominative@pro",
  "suggestions_from_website": [
    {
      "value": "john.doe@company.com",
      "score": 0.92
    }
  ],
  "data_type": "email",
  "scores": {
    "accuracy": 0.7,
    "validity": 0,
    "completeness": 1.0,
    "consistency": 0
  }
}
```

## Data Quality Dimensions

The API assesses emails across 6 key dimensions:

1. **Accuracy**: How correct and reliable the data is
2. **Completeness**: How much of the required data is present
3. **Consistency**: How uniform and coherent the data is
4. **Timeliness**: How current and up-to-date the data is
5. **Validity**: How well the data conforms to defined rules
6. **Uniqueness**: How free the data is from duplicates

## Domain Qualifications

- `nominative@pro`: Professional domain, returns invalid for fake emails
- `catchall@pro`: Professional domain, returns valid for fake emails
- `nominative@perso`: Personal domain, returns invalid for fake emails
- `catchall@perso`: Personal domain, returns valid for fake emails
- `Unknown`: Grey listed or temporary server issue

## Error Handling

The server includes comprehensive error handling:

- HTTP errors are caught and returned with appropriate status codes
- Network timeouts are handled gracefully
- Invalid responses are logged with emoji indicators
- All errors include descriptive messages

## Testing with Cursor

To test this MCP server with Cursor:

1. Configure your OAuth 2.0 credentials in `.env`
2. Start the server: `python fastmcp_delpha_server.py`
3. In Cursor, configure the MCP server connection
4. Use the available tools to test email assessment functionality

The server automatically creates tools from your OpenAPI specification using FastMCP's built-in integration, providing proper parameter validation and response handling.

## Authentication

The server supports OAuth 2.0 client credentials flow:

- **Token URL**: `https://secure-dev.delpha.io/oauth2/token`
- **Scope**: `api/access`
- **Grant Type**: `client_credentials`

The server automatically:
- Obtains access tokens when needed
- Refreshes tokens before expiration
- Handles authentication errors gracefully
- Falls back to unauthenticated requests if credentials are not provided

## Logging

The server uses emoji-based logging for easy visual identification:

- 🚀 Server startup
- 🔐 Authentication operations
- 💡 Information messages
- ✅ Success operations
- ❌ Error conditions
- ⚠️ Warnings
- ⏳ Processing status
- 📧 Email-related operations
- 🏷️ Label information

## License

This project is provided as-is for testing and development purposes. # DelphaMCP
