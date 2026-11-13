# PulseRCM AI: Hospital Revenue Cycle & Financial Intelligence Engine

An enterprise-grade hospital Revenue Cycle Management (RCM) and financial analytics application designed to track gross billing, insurance claim denials, accounts receivable (A/R) aging, and revenue leakage across clinical departments.

##  Live Demo
[Access PulseRCM AI Live App](https://your-streamlit-app-url.streamlit.app) *(Update after deployment)*

##  Business Problem & Objective
Hospital finance departments struggle with siloed billing data, insurance claim denials (e.g., coding errors, missing pre-authorizations), and delayed cash collections. **PulseRCM AI** bridges this gap by offering an interactive natural language query interface that translates executive financial questions into multi-variable SQL analytics instantly.

## Technical Architecture
1. **Database Layer:** Relational SQLite database (`hospital_finance_rcm.db`) structured around patient billing, CPT procedure codes, insurance payers, and claim statuses.
2. **Backend Engine:** Python & Pandas backend mapping natural language intents to secure database queries.
3. **Presentation Layer:** Interactive **Streamlit** dashboard displaying executive KPI cards, dynamic data tables, and financial aggregations.

##  Key Metrics Tracked
* Gross Revenue Billed vs. Net Cash Collected
* Claim Denial Volume & Loss Risk Analysis
* Accounts Receivable (A/R) Aging Benchmarks (>30 Days)
* Department-Level Collection Conversion Rates

## Tech Stack
* **Language:** Python
* **Database:** SQLite
* **App Framework:** Streamlit
* **Data Processing:** Pandas