import streamlit as st

# 1. High-Performance Page Configuration
st.set_page_config(page_title="Krish Tamboli | Data Portfolio", page_icon="⚡", layout="wide")

# 2. Premium UI Hover-Float CSS Engine
st.markdown("""
    <style>
    .main { background-color: #0A0F1D !important; color: #E2E8F0 !important; font-family: 'Inter', sans-serif; }
    header, footer, .stDeployButton { display: none !important; }
    .hero-name { font-size: 60px; font-weight: 800; background: linear-gradient(45deg, #38BDF8, #0EA5E9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .interactive-card { background: #111827; border: 1px solid #1F2937; padding: 30px; border-radius: 12px; margin-bottom: 15px; transition: all 0.3s; }
    .interactive-card:hover { transform: translateY(-6px); border-color: #38BDF8; }
    .job-title { font-size: 20px; font-weight: 700; color: #38BDF8; }
    .skill-badge { background: #1F2937; color: #38BDF8; border: 1px solid #2D3748; padding: 6px 14px; border-radius: 20px; display: inline-block; margin: 5px; font-size: 13px; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("### Krish Tamboli")
    st.markdown("📍 Frankfurt, Germany | ✉️ krishtamboli10@gmail.com")
    st.markdown("---")

# 4. Main Profile Hook
st.markdown("<div class='hero-name'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("### Data Science & Data Engineering")
st.write("""
I am a Data Professional specializing in the structural integrity of data assets. I focus on building 
resilient extraction architectures, auditing datasets, and automating pipeline workflows to supply 
enterprise-grade reporting environments with accurate, high-quality data.
""")

# 5. Interactive Tabs
tab1, tab2 = st.tabs(["💼 Professional Experience & Education", "🚀 Portfolio Projects"])

with tab1:
    st.subheader("Professional History")
    st.markdown("""
    <div class="interactive-card">
        <div class="job-title">Software Specialist (Data Analytics) | eClinicalWorks</div>
        <p>• Engineered robust data pipelines to ensure seamless ETL flows from raw source systems to analytical databases.<br>
           • Executed complex data audits on master record sets to eliminate discrepancies, improving reporting reliability by 15%.<br>
           • Built automated performance monitoring matrices to flag pipeline deviations, reducing operational latency by 40%.<br>
           • Developed interactive business intelligence dashboards to translate high-volume operational metrics into actionable insights for stakeholders.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Academic Credentials")
    st.markdown("""
    <div class="interactive-card">
        • <b>MSc in Computer Science (High Integrity Systems)</b> | Frankfurt UAS, Germany<br>
        • <b>BSc in Computer Science</b> | Mumbai University, India
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("Data Projects")
    
    # FIFA Project
    st.markdown("""
    <div class="interactive-card">
        <div class="job-title">FIFA World Cup Data Analysis Dashboard</div>
        <p>Transformed historical FIFA World Cup datasets into an interactive Power BI dashboard for granular analysis of tournament trends.</p>
        <p><b>Features:</b> Tournament Overview, Interactive Slicers by Stage/Team, and optimized Data Modeling using DAX.<br>
        🔗 <a href="https://github.com/krishtamboli/FIFA-WorldCup-Analytics" style="color: #38BDF8;">GitHub Repository</a></p>
        <span class="skill-badge">Power BI</span><span class="skill-badge">DAX</span><span class="skill-badge">Excel</span><span class="skill-badge">Tableau</span><span class="skill-badge">Data Modeling</span>
    </div>
    """, unsafe_allow_html=True)

    # Kafka Project
    st.markdown("""
    <div class="interactive-card">
        <div class="job-title">Apache Kafka ➔ Databricks Medallion Engine</div>
        <p>Designed a cloud ingestion pipeline to capture and parse high-volume message payloads into Databricks.</p>
        <span class="skill-badge">Apache Kafka</span><span class="skill-badge">PySpark</span><span class="skill-badge">Databricks</span><span class="skill-badge">SQL</span>
    </div>
    """, unsafe_allow_html=True)
