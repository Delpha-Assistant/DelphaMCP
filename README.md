<p align="center">
  <a href="https://delpha.io/">
    <img src="https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_b0b39d78ea2a6c1417ea68f2a9dcfeae/delpha.png" width="220" alt="Delpha Logo">
  </a>
</p>

<h1 align="center">Delpha Data Quality MCP</h1>
<h3 align="center">Data Quality Assessment for AI Agents & Apps</h3>

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/delpha-mcp?label=PyPI)](https://pypi.org/project/delpha-mcp/)
</div>

---

## 🌟 Overview

Delpha is an AI-driven data quality solution that uses intelligent AI Agents to ensure accurate, unique, and reliable customer data. Delpha's specialized AI Agents automate data cleansing and enrichment, helping businesses enhance operational efficiency and drive stronger revenue performance.

- **Reduce Data Maintenance Costs:** Delpha minimizes the need for manual data cleanup, reducing labor costs and overhead associated with constant data maintenance.
- **Improve Sales Productivity:** By automating data quality tasks, Delpha frees up significant portions of sales teams' schedules, allowing them to focus on selling rather than data entry and correction.
- **Shorten Data Migration:** Delpha accelerates the process of unifying CRM datasets, enabling sales reps to confidently approach newly acquired customers and drive incremental revenue sooner.
- **Deduplication with AI:** Delpha’s advanced AI accurately scores potential duplicates by analyzing multiple fields and detecting subtle variations, offering both automatic and manual merging options.

---

## 🚀 Quickstart (with Cursor)

1. **Install the package:**
   ```bash
   pip install delpha-mcp
   ```
2. **Configure Cursor:**
   - Go to `Settings → MCP` and add:
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
   - Replace with your Delpha credentials.
3. **Restart Cursor** — Delpha tools are now available!

---

## 🗝️ Getting Client Credentials

To use Delpha MCP, you need OAuth2 client credentials. Please contact the Delpha team at [support.api@delpha.io](mailto:support.api@delpha.io) to request your client ID and secret.

---

## 🛠️ Tools

Delpha MCP exposes a set of intelligent tools to assess and improve the quality of your data. Each tool is designed to address specific data quality challenges, providing actionable insights and suggestions for improvement.

### Email Quality

**Available MCP Tool Names:**
- `submitEmailQuality`: Submit an email address for quality evaluation and receive a job ID for tracking progress.
- `getEmailQualityStatus`: Retrieve the result and status of a previously submitted email quality job.

**Goal:**
Evaluate and enhance the quality of email addresses in your database, ensuring your contact information is accurate, complete, and actionable.

**Capabilities:**
- Analyzes email addresses across four key data quality dimensions:
  - **Completeness:** Verifies that the email field is populated.
  - **Validity:** Checks if the email follows standard format rules.
  - **Accuracy:** Assesses whether the email accurately matches the intended contact.
  - **Consistency:** Ensures the email is aligned with other data points (e.g., domain, website, etc.).
- Classifies each email as personal or professional—supporting GDPR compliance and improving deliverability.
- Suggests corrected emails when issues are found, complete with a confidence score to guide decision-making.
- Provides a comprehensive health check of your email data—delivering actionable insights to boost communication success, compliance, and data integrity.

**How it works:**
- Submit an email address (optionally with first name, last name, and website) for quality evaluation using the `submitEmailQuality` tool.
- Track the job and retrieve a detailed quality report, including scores for accuracy, completeness, consistency, and validity, as well as actionable suggestions for improvement, using the `getEmailQualityStatus` tool.

> More tools (address, social, website, deduplication, etc.) will be added soon as Delpha expands its data quality platform.

---


## 📞 Support
if you encounter any issues or have questions, please reach out to the Delpha support team or open an issue in the repository.
