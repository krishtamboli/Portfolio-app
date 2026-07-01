import streamlit as st
import pandas as pd
import re

# 1. Clean Page Initialization (Using native settings)
st.set_page_config(
    page_title="Krish Tamboli | Portfolio", 
    page_icon="⚡", 
    layout="wide"
)

# 2. Sidebar Layout
with st.sidebar:
    st.markdown("### KRISH TAMBOLI")
    st.caption("Data Systems & Analytics Specialist")
    st.markdown("---")
    st.markdown("🌐 **Location:** Frankfurt, Germany")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")
    st.markdown("🔗 **Professional Networks**")
    st.markdown("[LinkedIn Profile](https://linkedin.com)")
    st.markdown("[GitHub Repositories](https://github.com/krishtamboli)")
    st.markdown("---")
    st.caption("💼 Current Status:")
    st.write("Open to Working Student & Data Operations roles within Germany.")

# 3. Main Header & Core Overview
st.title("Systems Engineering & Data Health")
st.markdown(
    "I am a Master's student in **High Integrity Systems** specializing in data detective work. "
    "While standard workflows focus on simple visualization, I specialize in deep-diving raw backend datasets "
    "to isolate hidden structural anomalies, clean chaotic records, and eliminate system processing bottlenecks."
)

# Highlight Metrics using native components
st.markdown("---")
m_col1, m_col2 = st.columns(2)
with m_col1:
    st.metric(label="Monitoring Overhead Reduction", value="-40%")
with m_col2:
    st.metric(label="Core Database Reliability Lift", value="+15%")
st.markdown("---")

# 4. Modular Presentation Tabs
tab1, tab2, tab3 = st.tabs(["⚡ Live Data Cleaning Pipeline", "🛠️ Technical Capability Spectrum", "💼 Experience & Credentials"])

with tab1:
    st.subheader("Live Processing Pipeline Optimization")
    st.write(
        "Instead of just describing data cleaning conceptually, this module executes live Python string parsing "
        "and type validation over an incoming corrupt production transaction stream log."
    )
    
    # Raw log demonstration
    st.markdown("#### 1. The Incoming Corrupt Log Stream")
    raw_log_data = [
        "TXN_ID:10024|REG:Frankfurt|VAL:1250EUR|STATUS:VALID",
        "TXN_ID:10025|REG:Berlin|VAL:4300_ERR_NaN|STATUS:CORRUPT",
        "TXN_ID:10026|REG:Munich|VAL:1500EUR|STATUS:VALID",
        "TXN_ID:NULL_ID|REG:Hamburg|VAL:950EUR|STATUS:MISSING_ID",
        "TXN_ID:10028|REG:Frankfurt|VAL:6100EUR|STATUS:VALID"
    ]
    st.text("\n".join(raw_log_data))

    st.markdown("---")

    # Interactive Execution
    st.markdown("#### 2. Execute Data Cleaning Pipeline Logic")
    run_pipeline = st.checkbox("🚀 Click to Run Cleaning & Optimization Script")
    
    if run_pipeline:
        parsed_records = []
        
        for line in raw_log_data:
            # Step A: Safe split logic
            parts = dict(item.split(":") for item in line.split("|"))
            
            # Step B: Clean string values using regular expressions
            raw_val = parts["VAL"]
            clean_val = re.sub(r"[^\d]", "", raw_val)
            
            # Cast types with strict fallback defaults
            if clean_val == "":
                numeric_val = 0
                anomaly_note = "Missing Value Coerced to 0"
            else:
                numeric_val = int(clean_val)
                anomaly_note = "Clean Operational Record"
                
            # Handle broken structural IDs
            if parts["TXN_ID"] == "NULL_ID":
                parts["TXN_ID"] = "00000"
                anomaly_note = "Structural Malformation: Null Key Imputed"
            
            parsed_records.append({
                "Transaction ID": parts["TXN_ID"],
                "Region": parts["REG"],
                "Revenue (Numeric)": numeric_val,
                "Pipeline Flag": anomaly_note
            })
            
        df_cleaned = pd.DataFrame(parsed_records)
        
        st.success("✅ Script Executed Successfully. Output Structured Ledger Layout:")
        st.dataframe(df_cleaned, use_container_width=True)
        
        # Display backend code transparently
        st.markdown("#### 🛠️ Production Code Behind This Module")
        st.code("""
# Backend transformation steps running live above:
parsed_records = []
for line in raw_log_data:
    parts = dict(item.split(":") for item in line.split("|"))
    
    # Strip alphabetical noise from metrics using regex
    clean_val = re.sub(r"[^\d]", "", parts["VAL"])
    numeric_val = int(clean_val) if clean_val != "" else 0
    
    # Impute missing primary database keys
    if parts["TXN_ID"] == "NULL_ID":
        parts["TXN_ID"] = "00000"
        
    parsed_records.append({
        "Transaction ID": parts["TXN_ID"],
        "Region": parts["REG"],
        "Revenue (Numeric)": numeric_val
    })
df_cleaned = pd.DataFrame(parsed_records)
        """, language="python")
    else:
        st.info("Pipeline Idle. Check the box above to run the data transformation script live.")

with tab2:
    st.subheader("Technical Toolkit")
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.markdown("**Data Diagnostics**")
        st.write("- Data Analysis\n- Pattern Identification\n- Structural Anomaly Detection\n- Process Optimization")
    with sc2:
        st.markdown("**Engineering Core**")
        st.write("- SQL\n- Python (Pandas/NumPy)\n- Power Automate\n- ETL Pipeline Design")
    with sc3:
        st.markdown("**Reporting & Operations**")
        st.write("- Power BI\n- Tableau\n- Advanced MS Excel\n- JIRA Tracking")

with tab3:
    st.subheader("Professional Timeline")
    
    with st.container():
        st.markdown("#### **Software Specialist (Data Analytics)**")
        st.caption("eClinicalWorks | June 2022 – Aug 2024")
        st.write(
            "- Conducted deep-dive SQL investigations into over 200 customer master records to isolate and resolve validation errors, improving master database reliability by 15% and ensuring clear data tracking for downstream transactional reports.\n"
            "- Built automated stakeholder alert workflows using Power Automate that flagged performance deviations and triggered targeted notifications in real time, cutting monitoring overhead by 40% across all active reporting pipelines.\n"
            "- Designed interactive Power BI dashboards to track operational KPIs while utilizing Jira to document and coordinate high-priority data exceptions, creating unified technical workflows that improved data visibility for cross-functional teams.\n"
            "- Coordinated cross-functional workflows across business, product, and IT teams in an agile environment, standardising reporting definitions, translating business requirements into technical solutions, and supporting 5 departments at the business-IT interface."
        )
    
    st.markdown("---")
    
    col_ed1, col_ed2 = st.columns(2)
    with col_ed1:
        st.markdown("#### **Academic Record**")
        st.write("**MSc in Computer Science (High Integrity Systems)**")
        st.caption("Frankfurt University of Applied Sciences | Germany")
        st.write("**BSc in Computer Science**")
        st.caption("Mumbai University | India")
    with col_ed2:
        st.markdown("#### **Technical Credentials**")
        st.write("- ✔️ Java Programming — IIT Bombay")
        st.write("- ✔️ MongoDB Developer — Vidyalankar School of IT")
        st.write("- ✔️ HTML, CSS & JavaScript — Vidyalankar School of IT")
        st.caption("🗣️ Languages: English (Fluent C1) | German (Actively Learning A2)")
