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

Delpha MCP brings advanced data quality assessment to any MCP-compatible tool, such as Cursor. Instantly validate, score, and improve the quality of your data—emails, addresses, social profiles, websites, and more—all via a secure, OAuth2-protected API.

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

## ✨ Features
- Data validation and quality scoring (email, address, social, website, ...)
- Actionable suggestions for data improvement
- Seamless integration with MCP tools (e.g., Cursor)

---


## 📞 Support
if you encounter any issues or have questions, please reach out to the Delpha support team or open an issue in the repository.
