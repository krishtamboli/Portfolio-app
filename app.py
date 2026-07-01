import streamlit as st
import pandas as pd

# 1. High-Performance Page Configuration
st.set_page_config(page_title="Krish Tamboli | Data Portfolio", page_icon="⚡", layout="wide")

# 2. Premium UI Hover-Float CSS Engine Injection
st.markdown("""
    <style>
    /* Global Clean Canvas */
    .main {
        background-color: #0A0F1D !important;
        color: #E2E8F0 !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    header, footer, .stDeployButton { display: none !important; }
    
    /* Typography Gradient Scales */
    .hero-name {
        font-size: 60px;
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
    
    /* Elegant Narrative Sections */
    .story-section {
        padding: 35px 0px;
        border-bottom: 1px solid #1F2937;
    }
    .block-title {
        color: #FFFFFF;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 20px;
        border-left: 4px solid #38BDF8;
        padding-left: 12px;
    }
    
    /* THE GLIDING/HOVER CARD INTERFACE SETUP */
    .interactive-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 30px;
        border-radius: 12px;
        margin-top: 15px;
        margin-bottom: 15px;
        transition: all 0.3s ease-in-out;
    }
    /* This exact block causes the container to glide up and glow when the cursor passes over it */
    .interactive-card:hover {
        transform: translateY(-6px);
        border-color: #38BDF8;
        box-shadow: 0 12px 24px rgba(56, 189, 248, 0.06);
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

    /* Embedded Inline Metric Badges */
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

    /* Modern Minimalist Tech Badges */
    .skill-badge {
        background: #1F2937;
        color: #38BDF8;
        border: 1px solid #2D3748;
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 13px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .skill-badge:hover {
        background: #38BDF8;
        color: #0A0F1D;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Permanent Left-Hand Sidebar Navigation
with st.sidebar:
    st.markdown("<h3 style='color: white; margin-bottom:0;'>Krish Tamboli</h3>", unsafe_allow_html=True)
    st.caption("Data Science & Engineering")
    st.markdown("---")
    st.markdown("📍 Frankfurt, Germany")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")
    st.markdown("[LinkedIn Profile](https://linkedin.com) | [GitHub Repositories](https://github.com/krishtamboli)")

# 4. Re-engineered Linear Storyboard
st.markdown("<br>", unsafe_allow_html=True)

# --- NARRATIVE NODE 1: PROFILE HOOK ---
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='hero-name'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-tagline'>Data Science & Data Engineering</div>", unsafe_allow_html=True)
st.markdown(
    "I am a Master's student in **High Integrity Systems** specializing in the structural health of raw data assets. "
    "Instead of just managing static visualization charts, I focus on building resilient extraction architectures, "
    "auditing datasets, and eliminating pipeline execution lags to supply enterprise reporting environments with accurate data."
)
st.markdown("</div>", unsafe_allow_html=True)


# --- NARRATIVE NODE 2: INDUSTRY HISTORY ---
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>1. Professional History & Proven Impact</div>", unsafe_allow_html=True)
st.markdown("My enterprise background is centered on resolving validation gaps and automating performance monitoring matrix workflows.")

# Gliding Experience Card
st.markdown("""
<div class="interactive-card">
    <span style="float: right;" class="meta-text">June 2022 – Aug 2024</span>
    <div class="job-title">Software Specialist (Data Analytics)</div>
    <div style="color: #9CA3AF; font-size: 15px; margin-bottom: 15px;">eClinicalWorks | Mumbai</div>
    <p style="font-size:15px; color: #E2E8F0; line-height: 1.7; margin-bottom:0;">
    • Conducted deep-dive investigations into over <span class="metric-badge">200+ Logs</span> of master records to isolate system validation errors, lifting data record reliability by <span class="metric-badge">+15%</span>.<br>
    • Created automated stakeholder alert matrices using Power Automate to flag pipeline deviations, cutting operational monitoring overhead by <span class="metric-badge-red">-40%</span>.<br>
    • Designed interactive Power BI dashboards to map operational metrics while using Jira to systematically track data exceptions across cross-functional team interfaces.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# --- NARRATIVE NODE 3: CLOUD INFRASTRUCTURE ---
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>2. Distributed Data Engineering Architectures</div>", unsafe_allow_html=True)
st.markdown("To process modern big data streams smoothly at scale, I design cloud data ingestion components that prevent ingestion bottlenecks.")

# Gliding Project Card
st.markdown("""
<div class="interactive-card">
    <div class="job-title">Apache Kafka ➔ Databricks Medallion Engine</div>
    <p style="font-size: 15px; color: #E2E8F0; line-height: 1.7; margin-top: 12px; margin-bottom: 15px;">
    Engineered a cloud ingestion pipeline designed to capture and parse high-volume message payloads from Apache Kafka cluster topics straight into a Databricks environment. 
    By deploying automated Python and PySpark streaming tasks, the architecture ensures real-time stream execution, prevents partition lag under stress testing cycles, and organizes event data into structured database tables smoothly.
    </p>
    <span style="color: #38BDF8; font-family: monospace; font-size: 13px;">🧰 Stack: Apache Kafka, PySpark, Databricks Delta Lake, Cloud Data Engineering, SQL</span>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# --- NARRATIVE NODE 4: TECHNICAL TOOLKIT ---
st.markdown("<div class='story-section'>", unsafe_allow_html=True)
st.markdown("<div class='block-title'>3. Core Spectrum & Academic Credentials</div>", unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("**Technical Capabilities**")
    skills_list = [
        "SQL", "Python (Pandas/NumPy)", "Apache Kafka", "PySpark", "Databricks",
        "Power BI", "Tableau", "Power Automate", "ETL Architecture", "Data Analysis"
    ]
    for skill in skills_list:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

with col_right:
    st.markdown("**Academic Profile**")
    st.markdown("""
    <div class="interactive-card" style="padding: 20px; margin-top:0;">
        <p style='font-size:14px; margin-bottom:6px;'>🎓 <b>MSc in Computer Science</b><br>
        <span style='color:#9CA3AF; font-size:13px; font-family:monospace;'>High Integrity Systems | Frankfurt UAS</span></p>
        <p style='font-size:14px; margin-bottom:0;'>🎓 <b>BSc in Computer Science</b><br>
        <span style='color:#9CA3AF; font-size:13px; font-family:monospace;'>Mumbai University | India</span></p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
