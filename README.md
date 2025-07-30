<p align="center">
  <a href="https://delpha.io/">
    <img src="https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_b0b39d78ea2a6c1417ea68f2a9dcfeae/delpha.png" width="220" alt="Delpha Logo">
  </a>
</p>

<h1 align="center">Delpha Data Quality MCP</h1>
<h3 align="center"><a href="https://delpha.io" style="color: inherit; text-decoration: none;">Intelligent AI Agents to ensure accurate, unique, and reliable customer data</a></h3>

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/delpha-mcp?label=PyPI)](https://pypi.org/project/delpha-mcp/)
</div>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [🎬 Demo](#-demo)
- [🚀 Quickstart](#-quickstart)
- [🗝️ Getting Client Credentials](#️-getting-client-credentials)
- [🛠️ Tools](#️-tools)
- [📞 Support](#-support)

---

## 🌟 Overview

Delpha is an AI-driven data quality solution that uses intelligent AI Agents to ensure accurate, unique, and reliable customer data. Delpha's specialized AI Agents automate data cleansing and enrichment, helping businesses enhance operational efficiency and drive stronger revenue performance.

- **Reduce Data Maintenance Costs:** Delpha minimizes the need for manual data cleanup, reducing labor costs and overhead associated with constant data maintenance.
- **Improve Sales Productivity:** By automating data quality tasks, Delpha frees up significant portions of sales teams' schedules, allowing them to focus on selling rather than data entry and correction.
- **Shorten Data Migration:** Delpha accelerates the process of unifying CRM datasets, enabling sales reps to confidently approach newly acquired customers and drive incremental revenue sooner.
- **Deduplication with AI:** Delpha's advanced AI accurately scores potential duplicates by analyzing multiple fields and detecting subtle variations, offering both automatic and manual merging options.

<p align="center">
  <img src="https://github.com/Delpha-Assistant/DelphaMCP/blob/release/v0.1.12/assets/MCP.png?raw=true" width="600" alt="Delpha MCP Integration">
</p>

---

## 🎬 Demo

See Delpha MCP in action! Watch how easy it is to validate and enrich email data directly from your AI assistant.

<p align="center">
  <img src="https://github.com/Delpha-Assistant/DelphaMCP/blob/release/v0.1.12/assets/demo.gif?raw=true" width="800" alt="Delpha MCP Demo">
</p>

---

## 🚀 Quickstart

1. **Install the package:**
   ```bash
   pip install delpha-mcp
   ```

2. **Configure:**
   - Go to `Settings → MCP` and add:
   ```json
   {
     "mcpServers": {
       "Delpha": {
         "command": "python",
         "args": [
           "-m",
           "delpha_mcp"
         ],
         "env": {
           "DELPHA_CLIENT_ID": "your_client_id_here",
           "DELPHA_CLIENT_SECRET": "your_client_secret_here"
         }
       }
     }
   }
   ```
   - Replace with your Delpha credentials.

3. **Restart your app** — Delpha tools are now available!

---

## 🗝️ Getting Client Credentials

To use Delpha MCP, you need OAuth2 client credentials. Please contact the Delpha team at [support.api@delpha.io](mailto:support.api@delpha.io) to request your client ID and secret.

---

## 🛠️ Tools

Delpha MCP exposes a set of intelligent tools to assess and improve the quality of your data. Each tool is designed to address specific data quality challenges, providing actionable insights and suggestions for improvement.

### Email

**Available MCP Tool Names:**
- `findAndValidateEmail`: Submit an email address for validation and enrichment, and receive a job ID for tracking progress.
- `getEmailResult`: Retrieve the result and status of a previously submitted email validation/enrichment job.

**Goal:**

In today’s data-driven landscape, having accurate and complete email data directly impacts your organization’s efficiency, deliverability, and outreach success. Delpha’s **Email Finder** and **Email Validator** solutions ensure your email database remains robust, accurate, and up-to-date by systematically discovering missing emails and verifying email addresses.

Delpha evaluates email data across four critical dimensions:

- **Completeness**: Uses advanced Email Finder technology to locate and populate missing email addresses.
- **Validity**: Employs a powerful Email Validator to confirm emails adhere to standard formatting rules and are deliverable.
- **Accuracy**: Ensures that discovered emails match the intended individuals correctly.
- **Consistency**: Verifies alignment between emails and related data points such as domains, company websites, etc..

Additionally:

- **Email Validator classifies emails** as personal or professional, supporting GDPR compliance and improving deliverability.
- **Email Finder** offers **AI-generated email recommendation** for correcting or completing emails, accompanied by **confidence scores** to guide effective decision-making.

Delpha’s integrated **Email Finder** and **Email Validator** provide a comprehensive health check and intelligent enrichment, delivering actionable insights that enhance communication success, regulatory compliance, and overall data integrity.

### Email Insights

**Available MCP Tool Name:**
- `getEmailInsights`: Extract key insights from email content including name, phone number, title, company, and out-of-office status.

**Goal:**

Email communications contain a wealth of valuable information beyond just the email address itself. Delpha's Email Insight solution systematically analyzes email bodies to identify and extract critical contact information, professional details, and contextual insights that can transform how you understand and interact with your contacts.

Delpha's Email Insight solution extracts and enriches information such as:

- **Name**: Automatically identifies and extracts the sender's name from email communications.
- **Phone Number**: Detects and normalizes phone numbers to facilitate direct contact.
- **Title**: Extracts the sender's professional title, providing context for better engagement.
- **Company**: Identifies the sender's organization to enhance CRM accuracy and business insights.
- **Out-of-Office Status**: Determines if the sender is currently out of office, enabling timely and informed responses.

Delpha's Email Insight delivers precise, structured insights, enhancing data quality, enabling smarter interactions, and driving informed business decisions.

> More tools (address, social, website, deduplication, etc.) will be added soon as Delpha expands its data quality platform.

---


## 📞 Support
if you encounter any issues or have questions, please reach out to the Delpha support team or open an issue in the repository.
