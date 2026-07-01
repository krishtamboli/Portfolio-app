import streamlit as st
import pandas as pd
import re

# 1. Page Configuration & Clean CSS Typography
st.set_page_config(page_title="Krish Tamboli | Data Portfolio", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* Global Clean Slate */
    .main {
        background-color: #0A0F1D !important;
        color: #E2E8F0 !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    header, footer, .stDeployButton { display: none !important; }
    
    /* Storytelling Typography Scales */
    .hero-name {
        font-size: 64px;
        font-weight: 800;
        background: linear-gradient(45deg, #38BDF8, #0EA5E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        font-size: 26px;
        font-weight: 400;
        color: #9CA3AF;
        margin-bottom: 30px;
    }
    
    /* Clean Narrative Sections (High Readability Spacing) */
    .story-section {
        padding: 40px 0px;
        border-bottom: 1px solid #1F2937;
    }
    .story-heading {
        color: #FFFFFF;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 20px;
    }
    
    /* Minimalist Content Cards */
    .narrative-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 30px;
        border-radius: 12px;
        margin-top: 15px;
        transition: transform 0.2s ease;
    }
    .narrative-card:hover {
        border-color: #38BDF8;
    }
    
    .job-title {
        font-size: 20px;
        font-weight: 700;
        color: #38BDF8;
    }
    .meta-text {
        font-size: 14px;
        color: #9CA3AF;
        font-family: monospace;
    }

    /* Embedded Highlight Badges for Numbers */
    .metric-badge {
        background: rgba(56, 189, 248, 0.1);
        color: #38BDF8;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-family: monospace;
    }
    .metric-badge-red {
        background: rgba(244, 63, 94, 0.1);
        color: #F43F5E;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 700;
        font-family: monospace;
    }

    /* Skill Tags */
    .skill-tag {
        background-color: #1F2937;
        color: #38BDF8;
        border: 1px solid #374151;
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        margin: 6px;
        font-size: 13px;
        font-weight: 600;
    }
    </style>filter
""", unsafe_allow_html=True)

# 2. Sidebar Quick-Info
with st.sidebar:
    st.markdown("<h3 style='color: white; margin-bottom:0;'>Krish Tamboli</h3>", unsafe_allow_html=True)
    st.caption("Frankfurt, Germany")
    st.markdown("---")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")
    st.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/krishtamboli)")
    st.markdown("---")
    st.info("Seeking Data Science & Engineering opportunities.")

# --- THE NARRATIVE SCROLL ---

# SECTION 1: THE HERO HOOK
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='hero-name'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Data Science & Data Engineering</div>", unsafe_allow_html=True)

st.markdown(
    "##### The Core Focus\n"
    "I am a Master's student in **High Integrity Systems** specializing in making raw, chaotic data production streams reliable. "
    "Instead of just building basic visual charts, I focus on the structural integrity of data: designing extraction pipelines, optimizing backend datasets, "
    "and eliminating processing bottlenecks to deliver pristine information to enterprise reporting environments."
)
st.markdown("</div>", unsafe_allow_html=True)


# SECTION 2: CHRONOLOGICAL RECORD & PERFORMANCE METRICS
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='story-heading'>1. Professional History & Proven Impact Metrics</div>", unsafe_allow_html=True)

st.markdown(
    "My engineering foundation is built on handling live database diagnostics and data automation workflows at an enterprise scale, "
    "ensuring system reliability across cross-functional team interfaces."
)

st.markdown("""
<div class="narrative-card">
    <span style="float: right;" class="meta-text">June 2022 – Aug 2024</span>
    <div class="job-title">Software Specialist (Data Analytics)</div>
    <div style="color: #9CA3AF; font-size: 15px; margin-bottom: 15px;">eClinicalWorks | Mumbai</div>
    <p style="font-size:15px; color: #E2E8F0; line-height: 1.8; margin-bottom:0;">
    • Conducted deep-dive SQL investigations into over <span class="metric-badge">200+ Logs</span> of customer master records to isolate validation errors, lifting core database reliability by <span class="metric-badge">+15%</span>.<br>
    • Built automated stakeholder alert workflows using Power Automate to flag pipeline deviations, cutting operational monitoring overhead by <span class="metric-badge-red">-40%</span>.<br>
    • Designed interactive Power BI dashboards to track operational KPIs while utilizing Jira to document data exceptions across agile business-IT interfaces.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# SECTION 3: THE FEATURED ENGINE
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='story-heading'>2. Scaled Projects: Real-Time Stream Ingestion Engine</div>", unsafe_allow_html=True)

st.markdown(
    "To address processing latency and structural tracking issues at scale, I engineer distributed cloud infrastructure components "
    "designed to ingest and clean high-volume message workloads smoothly."
)

st.markdown("""
<div class="narrative-card">
    <div class="job-title" style="color: #38BDF8;">Apache Kafka ➔ Databricks Medallion Pipeline</div>
    <p style="font-size: 15px; color: #E2E8F0; line-height: 1.7; margin-top: 10px;">
    Engineered a cloud data pipeline designed to ingest, parse, and structure high-volume messaging payloads from Kafka cluster topics directly into a Databricks environment. 
    By developing automated PySpark streaming tasks, the architecture successfully resolves partition bottleneck latency under testing loads. 
    It applies robust data schema rules to guarantee transactional updates retain permanent history without causing performance lag.
    </p>
    <p style="font-size: 13px; color: #38BDF8; font-family: monospace; margin-bottom:0;">🧰 Core Architecture Stack: Apache Kafka, PySpark, Databricks Delta Lake, Cloud Data Engineering, SQL</p>
</div>
""", unsafe_allow_html=True)

# Live Simulation Subblock
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("⚙️ **Interactive Simulation: Processing a Live Log Stream**")
st.write("Toggle the pipeline filter below to view how a Python engine ruleset parses out corrupt syntax variations instantly.")

raw_log_data = [
    "TXN_ID:10024|REG:Frankfurt|VAL:1250EUR|STATUS:VALID",
    "TXN_ID:10025|REG:Berlin|VAL:4300_ERR_NaN|STATUS:CORRUPT",
    "TXN_ID:10026|REG:Munich|VAL:1500EUR|STATUS:VALID",
    "TXN_ID:NULL_ID|REG:Hamburg|VAL:950EUR|STATUS:MISSING_ID",
    "TXN_ID:10028|REG:Frankfurt|VAL:6100EUR|STATUS:VALID"
]

run_p = st.checkbox("🚀 Deploy Script Engine & Parse Logs")

if run_p:
    parsed_records = []
    for line in raw_log_data:
        parts = dict(item.split(":") for item in line.split("|"))
        raw_val = parts["VAL"]
        clean_val = re.sub(r"[^\d]", "", raw_val)
        numeric_val = int(clean_val) if clean_val != "" else 0
        if parts["TXN_ID"] == "NULL_ID":
            parts["TXN_ID"] = "00000"
        parsed_records.append({
            "Transaction ID": parts["TXN_ID"],
            "Region": parts["REG"],
            "Revenue (Numeric)": numeric_val,
            "Engine Status Flag": "Cleaned Record" if numeric_val > 0 else "Imputed Malformation"
        })
    st.dataframe(pd.DataFrame(parsed_records), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# SECTION 4: THE TECHNICAL TOOLKIT
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='story-heading'>3. Technical Toolkit & Academic Credentials</div>", unsafe_allow_html=True)

st.markdown("The targeted array of tools, core frameworks, and education details that define my professional profile:")

tc1, tc2 = st.columns([2, 1])

with tc1:
    st.markdown("**Engineering & Analytics Capabilities**")
    skills = [
        "SQL", "Python (Pandas/NumPy)", "Apache Kafka", "PySpark", "Databricks", 
        "Power BI", "Tableau", "Power Automate", "ETL Pipeline Design", 
        "Data Analysis", "Structural Anomaly Detection", "Process Optimization"
    ]
    for s in skills:
        st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

with tc2:
    st.markdown("**Education & Background**")
    st.markdown(
        "<p style='font-size:14px; margin-bottom:4px;'>🎓 <b>MSc in Computer Science</b><br>"
        "<span class='meta-text'>High Integrity Systems<br>Frankfurt UAS | Germany</span></p>"
        "<p style='font-size:14px;'>🎓 <b>BSc in Computer Science</b><br>"
        "<span class='meta-text'>Mumbai University | India</span></p>", 
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
