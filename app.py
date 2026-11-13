import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="PulseRCM AI - Hospital Financial Intelligence", layout="wide")

st.title("🏥 PulseRCM AI: Hospital Financial & Billing Intelligence")
st.markdown("Query hospital billing records, claim denials, and payer collection metrics using natural language.")

# Database Connection & Query Parsing Helper
def run_financial_query(user_query):
    conn = sqlite3.connect('hospital_finance_rcm.db')
    q = user_query.lower()
    
    # Financial Query Parsing Logic (Simulated Text-to-SQL Agent)
    if "denied" in q or "denial" in q:
        sql = "SELECT billing_id, department, payer_name, gross_charge, denial_code, claim_status FROM patient_billing WHERE claim_status = 'DENIED'"
    elif "days in ar" in q or "pending" in q or "aging" in q:
        sql = "SELECT billing_id, department, payer_name, gross_charge, days_in_ar, claim_status FROM patient_billing WHERE days_in_ar > 30 ORDER BY days_in_ar DESC"
    elif "radiology" in q:
        sql = "SELECT billing_id, cpt_code, payer_name, gross_charge, paid_amount, claim_status FROM patient_billing WHERE department = 'Radiology'"
    elif "collection" in q or "summary" in q or "total" in q:
        sql = "SELECT department, COUNT(billing_id) as total_claims, SUM(gross_charge) as total_gross_billed, SUM(paid_amount) as total_cash_collected, ROUND(AVG(days_in_ar),1) as avg_days_in_ar FROM patient_billing GROUP BY department"
    else:
        sql = "SELECT * FROM patient_billing"
        
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return sql, df

# Executive KPI Summary Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Gross Revenue Billed", "$20,950.00")
col2.metric("Net Cash Collected", "$8,950.00", delta="42.7% Collection Rate")
col3.metric("Denied Claim Volume", "$2,550.00", delta="-12.1% Loss Risk", delta_color="inverse")
col4.metric("Avg Days in A/R", "35.8 Days", delta="+5.2 Days", delta_color="inverse")

st.divider()

# Natural Language Search Interface
user_input = st.text_input("Ask a financial question (e.g., 'Show all denied claims', 'Which claims have high days in AR?', 'Give department summary'):")

if st.button("Run Financial Intelligence Query"):
    if user_input:
        with st.spinner("Analyzing financial database schema..."):
            sql_executed, result_df = run_financial_query(user_input)
            
            st.subheader("Executed SQL Command")
            st.code(sql_executed, language="sql")
            
            st.subheader("Query Results")
            st.dataframe(result_df, use_container_width=True)
            
            if "gross_charge" in result_df.columns:
                total_val = result_df["gross_charge"].sum()
                st.info(f"💡 Total Gross Charge value for this selection: **${total_val:,.2f}**")
            elif "total_gross_billed" in result_df.columns:
                total_val = result_df["total_gross_billed"].sum()
                st.info(f"💡 Total Gross Billed across departments: **${total_val:,.2f}**")