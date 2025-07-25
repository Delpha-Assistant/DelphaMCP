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

### Email Validator and Email Finder

**Available MCP Tool Names:**
- `submitEmailQuality`: Submit an email address for validation and enrichment, and receive a job ID for tracking progress.
- `getEmailQualityStatus`: Retrieve the result and status of a previously submitted email validation/enrichment job.

**Goal:**

In today’s data-driven landscape, having accurate and complete email data directly impacts your organization’s efficiency, deliverability, and outreach success. Delpha’s Email Finder and Email Validator solutions ensure your email database remains robust, accurate, and up-to-date by systematically discovering missing emails and verifying email addresses.

Delpha evaluates email data across four critical dimensions:
- **Completeness:** Uses advanced Email Finder technology to locate and populate missing email addresses.
- **Validity:** Employs a powerful Email Validator to confirm emails adhere to standard formatting rules and are deliverable.
- **Accuracy:** Ensures that discovered emails match the intended individuals correctly.
- **Consistency:** Verifies alignment between emails and related data points such as domains, company websites, etc.

Additionally, Delpha:
- Classifies emails as personal or professional, supporting GDPR compliance and improving deliverability.
- Offers AI-generated recommendations for correcting or completing emails, accompanied by confidence scores to guide effective decision-making.

Delpha’s integrated Email Finder and Email Validator provide a comprehensive health check and intelligent enrichment, delivering actionable insights that enhance communication success, regulatory compliance, and overall data integrity.

**How it works:**
- Submit an email address (optionally with first name, last name, and website) for validation and enrichment using the `submitEmailQuality` tool.
- Track the job and retrieve a detailed report, including scores for accuracy, completeness, consistency, and validity, as well as actionable suggestions for improvement, using the `getEmailQualityStatus` tool.

> More tools (address, social, website, deduplication, etc.) will be added soon as Delpha expands its data quality platform.

---


## 📞 Support
if you encounter any issues or have questions, please reach out to the Delpha support team or open an issue in the repository.
