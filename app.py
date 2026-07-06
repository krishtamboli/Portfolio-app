import streamlit as st

# 1. High-Performance Page Configuration
st.set_page_config(page_title="Krish Tamboli | Data Portfolio", page_icon="⚡", layout="wide")

# 2. Premium UI Hover-Float CSS Engine
st.markdown("""
    <style>
    .main { background-color: #0A0F1D !important; color: #E2E8F0 !important; font-family: 'Inter', sans-serif; }
    header, footer, .stDeployButton { display: none !important; }
    .hero-name { font-size: 60px; font-weight: 800; background: linear-gradient(45deg, #38BDF8, #0EA5E9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .contact-info { color: #9CA3AF; font-size: 16px; margin-bottom: 20px; }
    .interactive-card { background: #111827; border: 1px solid #1F2937; padding: 30px; border-radius: 12px; margin-bottom: 15px; transition: all 0.3s; }
    .interactive-card:hover { transform: translateY(-6px); border-color: #38BDF8; }
    .job-title { font-size: 20px; font-weight: 700; color: #38BDF8; }
    .skill-badge { background: #1F2937; color: #38BDF8; border: 1px solid #2D3748; padding: 6px 14px; border-radius: 20px; display: inline-block; margin: 5px; font-size: 13px; transition: all 0.2s ease; cursor: default; }
    .skill-badge:hover { background: #38BDF8; color: #0A0F1D; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("### Krish Tamboli")
    st.markdown("📍 Frankfurt, Germany")
    st.markdown("✉️ krishtamboli10@gmail.com")
    st.markdown("📞 +49 15510685501")
    st.markdown("---")

# 4. Main Profile Hook
st.markdown("<div class='hero-name'>Krish Tamboli</div>", unsafe_allow_html=True)
st.markdown("### Data Science & Data Engineering")
# Personal Contact Details under the name
st.markdown("""
    <div class='contact-info'>
    📍 Frankfurt, Germany &nbsp; | &nbsp; ✉️ krishtamboli10@gmail.com &nbsp; | &nbsp; 📞 +49 15510685501
    </div>
""", unsafe_allow_html=True)

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
        <p>Focused on transforming historical FIFA World Cup datasets into an interactive Power BI dashboard. 
        The goal was to practice data modeling and develop a clean, user-friendly interface for granular analysis.</p>
        <p><b>Key Features:</b> Tournament Overview (visualized trends), Interactive Filtering (slice by stage/team), and Data Modeling (DAX and star schema techniques).</p>
        <p>🔗 <a href="https://github.com/krishtamboli/FIFA-WorldCup-Analytics" style="color: #38BDF8;">GitHub Repository</a></p>
    </div>
    """, unsafe_allow_html=True)
    

    # Kafka Project
    st.markdown("""
    <div class="interactive-card">
        <div class="job-title">Apache Kafka ➔ Databricks Medallion Engine</div>
        <p>Engineered a cloud ingestion pipeline designed to capture and parse high-volume message payloads from Apache Kafka cluster topics straight into a Databricks environment. 
        By deploying automated Python and PySpark streaming tasks, the architecture ensures real-time stream execution, prevents partition lag under stress testing cycles, and organizes event data into structured database tables.</p>
    </div>
    """, unsafe_allow_html=True)
    

    # Technical Skills Section
    st.subheader("Technical Skills")
    skills = ["Power BI", "DAX", "SQL", "Python", "Tableau", "Excel", "Data Modeling", "ETL Architecture", "Data Cleaning", "PySpark", "Apache Kafka"]
    for skill in skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
