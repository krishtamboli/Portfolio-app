import streamlit as st
import pandas as pd
import re

# 1. Page Configuration
st.set_page_config(page_title="Krish Tamboli | Portfolio", page_icon="⚡", layout="wide")

# 2. Advanced CSS Theme Injection
st.markdown("""
    <style>
    .main {
        background-color: #0A0F1D !important;
        color: #E2E8F0 !important;
    }
    header, footer, .stDeployButton { display: none !important; }
    
    .hero-name {
        font-size: 56px;
        font-weight: 800;
        background: linear-gradient(45deg, #38BDF8, #0EA5E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-size: 24px;
        font-weight: 400;
        color: #9CA3AF;
        margin-bottom: 25px;
    }

    .interactive-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        transition: all 0.3s ease-in-out;
    }
    .interactive-card:hover {
        transform: translateY(-5px);
        border-color: #38BDF8;
        box-shadow: 0 10px 20px rgba(56, 189, 248, 0.05);
    }

    .section-title {
        color: #FFFFFF;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
        border-left: 4px solid #38BDF8;
        padding-left: 12px;
    }

    .custom-badge {
        background-color: #1F2937;
        color: #38BDF8;
        border: 1px solid #374151;
        padding: 5px 12px;
        border-radius: 6px;
        display: inline-block;
        margin: 5px;
        font-size: 13px;
        font-family: monospace;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .custom-badge:hover {
        background-color: #38BDF8;
        color: #0A0F1D;
    }

    .job-header {
        font-size: 18px;
        font-weight: 700;
        color: #38BDF8;
        margin: 0;
    }
    .job-meta {
        font-size: 14px;
        color: #9CA3AF;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.markdown("<h2 style='color: white; margin-bottom:0;'>KRISH TAMBOLI</h2>", unsafe_allow_html=True)
    st.caption("Data Science Specialist")
    st.markdown("---")
    st.markdown("🌐 **Location:** Frankfurt, Germany")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")
    st.markdown("🔗 **Networks**")
    st.markdown("[LinkedIn Profile](https://linkedin.com)")
    st.markdown("[GitHub Repositories](https://github.com/krishtamboli)")
    st.markdown("---")
    st.caption("💼 Current Status:")
    st.info("Open to Working Student & Data Operations roles within Germany.")

# 4. Top Hero Segment
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='hero-name'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Data Science & Data Engineering</div>", unsafe_allow_html=True)

st.markdown(
    "I am a Master's student in **High Integrity Systems** who actually enjoys the detective work involved in data. "
    "While standard workflows focus on simple visualization charts, I specialize in deep-diving raw backend datasets "
    "to isolate hidden structural anomalies, clean chaotic production records, and eliminate processing infrastructure bottlenecks."
)

# Metric Summary Rows
st.markdown("<br>", unsafe_allow_html=True)
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.markdown('<div class="interactive-card"><span style="color:#9CA3AF; font-size:12px; font-weight:600; text-transform:uppercase;">Monitoring Overhead</span><br><span style="font-size:36px; font-weight:800; color:#F43F5E;">-40%</span></div>', unsafe_allow_html=True)
with m_col2:
    st.markdown('<div class="interactive-card"><span style="color:#9CA3AF; font-size:12px; font-weight:600; text-transform:uppercase;">Master Record Diagnostics</span><br><span style="font-size:36px; font-weight:800; color:#38BDF8;">200+ Logs</span></div>', unsafe_allow_html=True)
with m_col3:
    st.markdown('<div class="interactive-card"><span style="color:#9CA3AF; font-size:12px; font-weight:600; text-transform:uppercase;">Database Reliability Lift</span><br><span style="font-size:36px; font-weight:800; color:#10B981;">+15%</span></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Core Navigation Tabs
t1, t2, t3 = st.tabs(["⚡ Featured Project & Pipeline", "🛠️ Technical Capability Spectrum", "💼 Experience & Credentials"])

with t1:
    st.markdown("<div class='section-title'>Featured Project: Real-Time Stream Ingestion Engine</div>", unsafe_allow_html=True)
    st.markdown('<div class="interactive-card"><h4 style="color: #38BDF8; margin-top:0;">Kafka ➔ Databricks Medallion Architecture</h4><p style="font-size: 14px; color: #9CA3AF;">Engineered an end-to-end cloud ingestion pipeline designed to ingest, parse, and structure high-volume messaging payloads from Apache Kafka cluster topics into a structured Databricks workspace environment.</p><p style="font-size: 14px; color: #E2E8F0;"><strong>Key Contributions:</strong> Developed automated Python and PySpark streaming data tasks to process unstructured incoming event logs. Resolved partition bottleneck latency under high testing loads. Applied clean Slowly Changing Dimension (SCD Type 2) tracking schemas to ensure transactional data updates retain permanent structural log history without causing database performance lag.</p><p style="font-size: 13px; color: #38BDF8; font-family: monospace;">🧰 Stack: Apache Kafka, PySpark, Databricks Delta Lake, Cloud Data Engineering, SQL</p></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Live Code Simulation: Anomalous Log Investigator</div>", unsafe_allow_html=True)
    st.write("To visually demonstrate how the pipeline handles data malformations live, this module executes real-time string parsing and regex-driven type validation algorithms over an incoming uncleaned transactional infrastructure stream log.")
    
    raw_log_data = [
        "TXN_ID:10024|REG:Frankfurt|VAL:1250EUR|STATUS:VALID",
        "TXN_ID:10025|REG:Berlin|VAL:4300_ERR_NaN|STATUS:CORRUPT",
        "TXN_ID:10026|REG:Munich|VAL:1500EUR|STATUS:VALID",
        "TXN_ID:NULL_ID|REG:Hamburg|VAL:950EUR|STATUS:MISSING_ID",
        "TXN_ID:10028|REG:Frankfurt|VAL:6100EUR|STATUS:VALID"
    ]
    st.text("\n".join(raw_log_data))

    st.markdown("<br>", unsafe_allow_html=True)
    run_p = st.checkbox("🚀 Click to Run Cleaning & Optimization Script")
    
    if run_p:
        parsed_records = []
        for line in raw_log_data:
            parts = dict(item.split(":") for item in line.split("|"))
            raw_val = parts["VAL"]
            clean_val = re.sub(r"[^\d]", "", raw_val)
            
            if clean_val == "":
                numeric_val = 0
                anomaly_note = "Missing Value Coerced to 0"
            else:
                numeric_val = int(clean_val)
                anomaly_note = "Clean Operational Record"
                
            if parts["TXN_ID"] == "NULL_ID":
                parts["TXN_ID"] = "00000"
                anomaly_note = "Structural Malformation: Null Key Imputed"
            
            parsed_records.append({
                "Transaction ID": parts["TXN_ID"],
                "Region": parts["REG"],
                "Revenue (Numeric)": numeric_val,
                "Pipeline Flag": anomaly_note
            })
            
        st.success("✅ Engine Parsing Complete. Structured Output:")
        st.dataframe(pd.DataFrame(parsed_records), use_container_width=True)

with t2:
    st.markdown("<div class='section-title'>Technical Capability Spectrum</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<h4 style='color:white; font-size:16px;'>Data Diagnostics</h4>", unsafe_allow_html=True)
        for s in ["Data Analysis", "Data Visualization", "Pattern Identification", "Structural Anomaly Detection", "Process Optimization", "User Behavior Tracking"]:
            st.markdown(f'<span class="custom-badge">{s}</span>', unsafe_allow_html=True)
    with c2:
        st.markdown("<h4 style='color:white; font-size:16px;'>Engineering Core</h4>", unsafe_allow_html=True)
        for s in ["SQL", "Python (Pandas/NumPy)", "Power Automate", "ETL Pipeline Design", "VBA / Macros"]:
            st.markdown(f'<span class="custom-badge">{s}</span>', unsafe_allow_html=True)
    with c3:
        st.markdown("<h4 style='color:white; font-size:16px;'>Reporting & Analytics</h4>", unsafe_allow_html=True)
        for s in ["Power BI", "Tableau", "Advanced MS Excel", "JIRA Tracking", "Agile Frameworks"]:
            st.markdown(f'<span class="custom-badge">{s}</span>', unsafe_allow_html=True)

with t3:
    st.markdown("<div class='section-title'>Chronological Record</div>", unsafe_allow_html=True)
    st.markdown('<div class="interactive-card"><span style="float: right;" class="job-meta">June 2022 – Aug 2024</span><div class="job-header">Software Specialist (Data Analytics)</div><div style="color: #9CA3AF; font-size: 14px; margin-bottom: 12px;">eClinicalWorks | Mumbai</div><p style="font-size:14px; color: #E2E8F0; line-height: 1.6;">• Conducted deep-dive SQL investigations into over 200 customer master records to isolate and resolve validation errors, improving master database reliability by 15% and ensuring data tracking for downstream transactional reports.<br>• Built automated stakeholder alert workflows using Power Automate that flagged performance deviations and triggered targeted notifications in real time, cutting monitoring overhead by 40% across all active reporting pipelines.<br>• Designed interactive Power BI dashboards to track operational KPIs while utilizing Jira to document and coordinate high-priority data exceptions, creating unified technical workflows that improved data visibility for cross-functional teams.<br>• Coordinated cross-functional workflows across business, product, and IT teams in an agile environment, standardising reporting definitions, translating business requirements into technical solutions, and supporting 5 departments at the business-IT interface.<br></p></div>', unsafe_allow_html=True)
    
    col_ed1, col_ed2 = st.columns(2)
    with col_ed1:
        st.markdown('<div class="interactive-card"><div class="job-header" style="margin-bottom:10px;">Academic Foundations</div><p style="margin:0; font-weight:600; font-size:15px;">MSc in Computer Science (High Integrity Systems)</p><p style="color:#9CA3AF; font-size:13px; margin:0; font-family: monospace;">Frankfurt University of Applied Sciences | Germany</p><br><p style="margin:0; font-weight:600; font-size:15px;">BSc in Computer Science</p><p style="color:#9CA3AF; font-size:13px; margin:0; font-family: monospace;">Mumbai University | India</p></div>', unsafe_allow_html=True)
    with col_ed2:
        st.markdown('<div class="interactive-card"><div class="job-header" style="margin-bottom:10px;">Technical Credentials</div><p style="margin:0; font-size:14px; color:#E2E8F0;">✔️ Java Programming — IIT Bombay (Spoken Tutorial)</p><p style="margin:6px 0; font-size:14px; color:#E2E8F0;">✔️ MongoDB Developer — Vidyalankar School of IT</p><p style="margin:0; font-size:14px; color:#E2E8F0;">✔️ HTML, CSS & JavaScript — Vidyalankar School of IT</p><br><p style="margin:0; font-size:13px; color:#9CA3AF; font-family: monospace;">🗣️ Languages: English (Fluent C1) | German (A2)</p></div>', unsafe_allow_html=True)
