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

* [🌟 Overview](#-overview)
* [🎬 Demo](#-demo)
* [🚀 Quickstart](#-quickstart)
* [🗝️ Getting Client Credentials](#️-getting-client-credentials)
* [🛠️ Tools](#️-tools)
* [📞 Support](#-support)

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

See Delpha MCP in action—validate and enrich data directly from your AI assistant.

<p align="center">
  <img src="https://github.com/Delpha-Assistant/DelphaMCP/blob/release/v0.1.12/assets/demo.gif?raw=true" width="800" alt="Delpha MCP Demo">
</p>

---

## 🚀 Quickstart

1. **Install the package**

   ```bash
   pip install delpha-mcp
   ```

2. **Configure**
   Add this to your MCP settings (replace env values with your credentials):

   ```json
   {
     "mcpServers": {
       "Delpha": {
         "command": "python",
         "args": ["-m", "delpha_mcp"],
         "env": {
           "DELPHA_CLIENT_ID": "your_client_id_here",
           "DELPHA_CLIENT_SECRET": "your_client_secret_here"
         }
       }
     }
   }
   ```

3. **Restart your app** — Delpha tools are now available.

---

## 🗝️ Getting Client Credentials

Delpha MCP uses OAuth2. Please contact **[support.api@delpha.io](mailto:support.api@delpha.io)** to request your client ID and secret.

---

## 🛠️ Tools

Delpha MCP exposes a set of intelligent tools to assess and improve the quality of your data. Each tool is designed to address specific data quality challenges, providing actionable insights and suggestions for improvement.



---

### Email

**MCP Tool Names**

* `findAndValidateEmail`
* `getEmailResult`

**What it does**
Keep email data deliverable and up-to-date by discovering missing addresses and validating existing ones.

**How we assess**

* **Completeness:** Find and populate missing addresses.
* **Validity:** Check syntax and deliverability signals.
* **Accuracy:** Ensure the email fits the intended person/entity context.
* **Consistency:** Align inputs with normalized output.

**Extras**

* Classification (e.g., professional vs. personal) to support compliant outreach.
* AI recommendations with confidence scores when a better email is likely.

---

### Address

**MCP Tool Names**

* `findAndValidateAddress`
* `getAddressResult`

**What it does**
Standardize, validate, and complete postal addresses to improve delivery, analytics, and territory planning.

**How we assess**

* **Completeness:** Fill missing elements (street no., street, city, postal code, country).
* **Validity:** Conformity to country-specific postal rules and canonical formats.
* **Accuracy:** Normalize structure and resolve ambiguities.
* **Consistency:** Compare input vs. normalized output.

**Extras**

* Returns a normalized, well-structured address.
* AI recommendations with confidence scores when multiple plausible addresses exist.

---

### Website

**MCP Tool Names**

* `findAndValidateWebsite`
* `getWebsiteResult`

**What it does**
Normalize and canonicalize company websites (domain, scheme, redirects) and suggest likely sites when the input is missing or off.

**How we assess**

* **Completeness:** Populate missing websites/root domains.
* **Validity:** Confirm proper URL formatting and safe normalization (scheme, subdomain, trailing slash, redirects).
* **Accuracy:** Check that the URL matches the intended entity.
* **Consistency:** Compare input vs. normalized/canonical URL.

**Extras**

* Returns the normalized (and redirected if applicable) URL.
* AI recommendations with confidence scores.

---

### LinkedIn

**MCP Tool Names**

* `findAndValidateLinkedin`
* `getLinkedinResult`

**What it does**
Normalize LinkedIn profile/company URLs and, when needed, suggest the most relevant pages using context like name, company, and website.

**How we assess**

* **Completeness:** Detect presence/absence of a LinkedIn URL.
* **Validity:** Validate **format** (e.g., `/in/` for people, company page patterns); not a live profile/existence check.
* **Accuracy:** Check that the URL aligns with provided context (first/last name, company name, website).
* **Consistency:** Compare input vs. normalized URL.

**Extras**

* Recommendations include URL, confidence, and helpful metadata (e.g., profile/page name, title/description, location, rank) to speed selection.

---

### Phone

**MCP Tool Names**

* `findAndValidatePhone`
* `getPhoneResult`

**What it does**
Normalize phone numbers to international standards and check basic plausibility.

**How we assess**

* **Completeness:** Is a value present.
* **Validity:** Does the number conform to country/region rules and basic plausibility checks (e.g., non-blacklisted patterns).
* **Consistency:** Compare input vs. normalized E.164 output.

**Notes**

* No accuracy score or side-field recommendations.
* If no country is provided, inference follows a configured country preference order.

---

### Name

**MCP Tool Names**

* `findAndValidateName`
* `getNameResult`

**What it does**
Normalize person names and detect common data-entry issues to keep contact data clean.

**How we assess**

* **Completeness:** Separate scoring for **FirstName** and **LastName**.
* **Validity:** Check both parts against reference databases.
* **Consistency:** Compare input vs. normalized casing, hyphenation, etc.
* **Misspelled:** Flag likely typos and propose close alternatives.
* **Reversed:** Detect when first and last names appear swapped.

**Extras**

* Suggestions include corrected spelling, swapped order when appropriate, or simply the normalized version when everything looks good.
* No accuracy score for names.

---

### Legal ID

**MCP Tool Names**

* `findAndValidateLegalID`
* `getLegalIDResult`

**What it does**
Validate, normalize, and enrich company legal identifiers across supported countries and ID types.

**How we assess**

* **Completeness:** Determine ID type from provided country or input; populate when possible.
* **Validity:** Normalize to canonical representation and verify against supported country rules and reference datasets.
* **Accuracy:** Check that the ID corresponds to the intended entity using side fields (e.g., company name, address, website).
* **Consistency:** Compare input vs. normalized value.

**Extras**

* Returns enriched context for matched entities (e.g., company name, website, address, industry) and ranked recommendations when input and side fields point to multiple candidates.

> The list of supported countries and ID types is maintained in Delpha’s documentation; implementations should rely on what’s enabled in your environment.

---

### Email Insights

**MCP Tool Name**

* `getEmailInsights`

**What it does**
Extract structured signals from email bodies to update/contact records faster.

**Examples of extracted fields**

* Name, phone(s), title, company, department, address
* Social links
* Out-of-office window
* Confidence score

---

### LinkedIn Import (People & Companies)

**MCP Tool Names**

* `submitLinkedinImport`
* `getLinkedinImportResult`

**What it does**
High-throughput importer for LinkedIn / Sales Navigator searches and lists. Submit a source URL and receive normalized profiles or companies at scale.

**Flow**

1. Start a job with `submitLinkedinImport`.
2. We handle throttling and retries.
3. Poll with `getLinkedinImportResult` for the final dataset URL.

> Refer to the OpenAPI schemas for the exact input fields and outputs supported in your environment.

---

## 📞 Support

If you encounter any issues or have questions, please reach out to the Delpha team at **[support.api@delpha.io](mailto:support.api@delpha.io)** or open an issue in the repository.
