import streamlit as st
import pandas as pd
import re

# 1. High-Performance Page Inception
st.set_page_config(page_title="Krish Tamboli | Data Portfolio", page_icon="⚡", layout="wide")

# Custom UI Breathe Space Styles
st.markdown("""
    <style>
    header, footer, .stDeployButton { display: none !important; }
    .main { background-color: #0A0F1D !important; }
    
    /* Clean Text Readability Containers */
    .hero-title {
        font-size: 58px;
        font-weight: 800;
        background: linear-gradient(45deg, #38BDF8, #0EA5E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px;
        margin-bottom: 0px;
    }
    .hero-tagline {
        font-size: 24px;
        color: #9CA3AF;
        margin-bottom: 35px;
    }
    .section-block {
        padding: 35px 0px;
        border-bottom: 1px solid #1F2937;
    }
    .block-title {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
    }
    .experience-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 25px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .highlight-number {
        color: #38BDF8;
        font-weight: 700;
        font-family: monospace;
        background: rgba(56, 189, 248, 0.1);
        padding: 2px 6px;
        border-radius: 4px;
    }
    .highlight-reduction {
        color: #F43F5E;
        font-weight: 700;
        font-family: monospace;
        background: rgba(244, 63, 94, 0.1);
        padding: 2px 6px;
        border-radius: 4px;
    }
    .skill-badge {
        background: #1F2937;
        color: #38BDF8;
        padding: 5px 12px;
        border-radius: 15px;
        display: inline-block;
        margin: 4px;
        font-size: 13px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Left-Hand Access Sidebar
with st.sidebar:
    st.markdown("<h3 style='color: white; margin-bottom:0;'>Krish Tamboli</h3>", unsafe_allow_html=True)
    st.caption("Data Science & Engineering")
    st.markdown("---")
    st.markdown("📍 Frankfurt, Germany")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")
    st.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/krishtamboli)")

# 3. The Linear Vertical Storyboard
st.markdown("<br>", unsafe_allow_html=True)

# --- PHASE 1: THE INTRODUCTION ---
st.markdown("<div class='section-block'>", unsafe_allow_html=True)
st.markdown("<div class='hero-title'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-tagline'>Master's Student in High Integrity Systems</div>", unsafe_allow_html=True)
st.markdown(
    "I specialize in the structural health of data assets. Instead of just managing static visualization charts, "
    "I focus on designing clean extraction flows, auditing backend datasets, and eliminating pipeline execution lags "
    "to supply enterprise reporting environments with accurate data."
)
st.markdown("</div>", unsafe_allow_html=True)

# --- PHASE 2: PROFESSIONAL HISTORY ---
st.markdown("<div class='section-block'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>1. Industry Track Record</div>", unsafe_allow_html=True)
st.markdown(
    "My engineering foundation is built on handling live database diagnostics and automation workflows at an enterprise scale, "
    "ensuring data consistency across business-IT interfaces."
)

st.markdown("""
<div class="experience-card">
    <span style="float: right; color: #9CA3AF; font-size: 13px; font-family: monospace;">2022 – 2024</span>
    <div style="font-size: 18px; font-weight: 700; color: #38BDF8;">Software Specialist (Data Analytics)</div>
    <div style="color: #9CA3AF; font-size: 14px; margin-bottom: 12px;">eClinicalWorks | Mumbai</div>
    <p style="font-size:14px; color: #E2E8F0; line-height: 1.6; margin-bottom:0;">
    • Conducted deep-dive investigations into over <span class="highlight-number">200+ Database Logs</span> to isolate and resolve system validation errors, lifting core record reliability by <span class="highlight-number">+15%</span>.<br>
    • Created automated stakeholder notification routines using Power Automate, reducing operational monitoring overhead by <span class="highlight-reduction">-40%</span>.<br>
    • Designed interactive Power BI dashboards to map operational KPIs while using Jira to systematically document and track data exceptions.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- PHASE 3: SCALED EXPERIMENTS ---
st.markdown("<div class='section-block'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>2. Distributed Cloud Architectures</div>", unsafe_allow_html=True)
st.markdown(
    "To handle high-volume data streams without system lag, I engineer distributed ingestion components "
    "designed to collect, parse, and organize messaging payloads smoothly."
)

st.markdown("""
<div class="experience-card">
    <div style="font-size: 18px; font-weight: 700; color: #38BDF8; margin-bottom: 8px;">Apache Kafka ➔ Databricks Medallion Engine</div>
    <p style="font-size: 14px; color: #E2E8F0; line-height: 1.6; margin-bottom: 12px;">
    Engineered a cloud data pipeline designed to ingest and parse unstructured messaging payloads from active Kafka cluster topics straight into a Databricks environment. 
    By setting up automated PySpark streaming tasks, the system effectively resolves bottleneck latencies under testing loads, processing event data into clean, structured layers while maintaining full update histories.
    </p>
    <span style="color: #38BDF8; font-family: monospace; font-size: 12px;">🧰 Stack: Apache Kafka, PySpark, Databricks Delta Lake, Cloud Data Engineering, SQL</span>
</div>
""", unsafe_allow_html=True)

# Live Processing Element
st.markdown("<br>", unsafe_allow_html=True)
st.write("⚙️ **Interactive Feature: Run Python Parsing Logic Live**")
st.caption("Toggle the filter switch below to view how a Python engine ruleset parses out system anomalies instantly.")

raw_log_inputs = [
    "TXN_ID:10024|REG:Frankfurt|VAL:1250EUR|STATUS:VALID",
    "TXN_ID:10025|REG:Berlin|VAL:4300_ERR_NaN|STATUS:CORRUPT",
    "TXN_ID:10026|REG:Munich|VAL:1500EUR|STATUS:VALID",
    "TXN_ID:NULL_ID|REG:Hamburg|VAL:950EUR|STATUS:MISSING_ID"
]

if st.checkbox("🚀 Deploy Script Engine & Process Log Stream"):
    parsed_output = []
    for line in raw_log_inputs:
        parts = dict(item.split(":") for item in line.split("|"))
        clean_val = re.sub(r"[^\d]", "", parts["VAL"])
        num_val = int(clean_val) if clean_val != "" else 0
        if parts["TXN_ID"] == "NULL_ID":
            parts["TXN_ID"] = "00000"
        parsed_output.append({
            "Transaction ID": parts["TXN_ID"],
            "Region": parts["REG"],
            "Revenue (Numeric)": num_val,
            "Engine Processing Flag": "Pristine Record" if num_val > 0 else "Imputed Malformation"
        })
    st.dataframe(pd.DataFrame(parsed_output), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- PHASE 4: THE TOOLKIT ---
st.markdown("<div class='section-block'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>3. Technical Spectrum & Credentials</div>", unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("**Core Skill Alignment**")
    skills_array = [
        "SQL", "Python (Pandas/NumPy)", "Apache Kafka", "PySpark", "Databricks",
        "Power BI", "Tableau", "Power Automate", "ETL Architecture", "Data Analysis"
    ]
    for skill in skills_array:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

with col_right:
    st.markdown("**Academic Timeline**")
    st.markdown(
        "<p style='font-size:14px; margin-bottom:6px;'>🎓 <b>MSc in Computer Science</b><br>"
        "<span style='color:#9CA3AF; font-size:13px; font-family:monospace;'>High Integrity Systems | Frankfurt UAS</span></p>"
        "<p style='font-size:14px;'>🎓 <b>BSc in Computer Science</b><br>"
        "<span style='color:#9CA3AF; font-size:13px; font-family:monospace;'>Mumbai University | India</span></p>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
