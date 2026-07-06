import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Chaital | Data Portfolio", page_icon="⚡", layout="wide")

# 2. CSS Engine
st.markdown("""
    <style>
    .main { background-color: #0A0F1D !important; color: #E2E8F0 !important; font-family: sans-serif; }
    .hero-name { font-size: 50px; font-weight: 800; color: #38BDF8; }
    .interactive-card { background: #111827; border: 1px solid #1F2937; padding: 25px; border-radius: 12px; margin-bottom: 15px; }
    .skill-badge { background: #1F2937; color: #38BDF8; border: 1px solid #2D3748; padding: 5px 12px; border-radius: 20px; display: inline-block; margin: 4px; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("### Chaital")
    st.caption("Data Analyst & Specialist")
    st.markdown("---")
    st.markdown("📍 Germany")
    st.markdown("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com/krishtamboli)")

# 4. Main Content
st.markdown("<div class='hero-name'>Chaital</div>", unsafe_allow_html=True)
st.markdown("Master's student in High Integrity Systems and Biotechnology, specializing in Data Analytics and Business Intelligence.")

# Tabs Setup
tab1, tab2 = st.tabs(["💼 Professional Experience", "🚀 Portfolio Projects"])

with tab1:
    st.subheader("Industry Experience")
    st.markdown("""
    <div class="interactive-card">
        <div style="color: #38BDF8; font-weight: bold;">Software Specialist (Data Analytics) | eClinicalWorks</div>
        <p style="margin-top: 10px;">
        • <b>Data Engineering:</b> Streamlined data ingestion workflows, ensuring high-integrity data flow from source systems into analytical environments.<br>
        • <b>Data Analysis:</b> Investigated system logs and master records to identify data quality bottlenecks, improving overall reporting reliability by 15%.<br>
        • <b>Automation:</b> Developed automated monitoring workflows to track pipeline health, significantly reducing manual overhead.<br>
        • <b>Visualization:</b> Designed and deployed interactive dashboards to translate complex operational metrics into actionable business insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("Featured Projects")
    
    # FIFA Project
    st.markdown("""
    <div class="interactive-card">
        <div style="color: #38BDF8; font-weight: bold; font-size: 18px;">FIFA World Cup Data Analysis Dashboard</div>
        <p style="margin-top: 10px;">
        Focused on transforming historical FIFA World Cup datasets into an interactive Power BI dashboard. 
        The goal was to practice data modeling and develop a user-friendly interface for granular analysis.<br><br>
        <b>Key Features:</b><br>
        • <b>Tournament Overview:</b> Visualized historical match results, scoring trends, and performance metrics.<br>
        • <b>Interactive Filtering:</b> Built functionality to slice data by tournament stage, team, and match outcomes.<br>
        • <b>Data Modeling:</b> Applied DAX and star schema techniques to structure tournament data for efficient visualization.<br>
        <br>
        🔗 <a href="https://github.com/krishtamboli/FIFA-WorldCup-Analytics" style="color: #38BDF8;">View Project on GitHub</a>
        </p>
        <div style="margin-top: 10px;">
            <span class="skill-badge">Microsoft Power BI</span>
            <span class="skill-badge">DAX</span>
            <span class="skill-badge">Excel</span>
            <span class="skill-badge">Tableau</span>
            <span class="skill-badge">Data Modeling</span>
            <span class="skill-badge">Data Visualization</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Technical Toolkit")
    skills = ["Power BI", "Tableau", "DAX", "Excel", "SQL", "Data Modeling", "ETL Architecture", "Data Cleaning"]
    for skill in skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
