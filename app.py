import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Professional Theme Injection
st.set_page_config(page_title="Krish Tamboli | Portfolio", page_icon="📊", layout="wide")

# Custom UI CSS Styling for a Premium Dark Accent look
st.markdown("""
    <style>
    .main .block-container { padding-top: 1.5rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 28px; }
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: 600; padding: 12px 20px; }
    
    /* Premium UI Card Design for Experience & Projects */
    .metric-card {
        background-color: rgba(28, 131, 225, 0.05);
        border: 1px solid rgba(28, 131, 225, 0.15);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        margin-bottom: 15px;
    }
    .skill-badge {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        margin: 4px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Navigation & Global Info
with st.sidebar:
    st.title("Krish Tamboli")
    st.caption("Data Science Specialist & System Analytics Graduate")
    st.markdown("---")
    
    st.markdown("### 📬 Contact Details")
    st.markdown("📍 Frankfurt, Germany")
    st.markdown("📞 +49 15510685501")
    st.markdown("✉️ [krishtamboli10@gmail.com](mailto:krishtamboli10@gmail.com)")
    st.markdown("💼 [LinkedIn Profile](https://linkedin.com)")
    st.markdown("💻 [GitHub Profile](https://github.com/krishtamboli)")
    st.markdown("---")
    
    # Elegant Availability Status
    st.info("💡 **Availability:** Open to Working Student & Data Operations roles within Germany.")

# 3. Hero Layout (Split view: Profile text on left, verified metrics on right)
hero_col1, hero_col2 = st.columns([2.5, 1], gap="large")

with hero_col1:
    st.title("Turning Raw Backend Infrastructure into Actionable Business Intelligence 🚀")
    st.markdown(
        "I am a Master's student in **High Integrity Systems** who actually enjoys the detective work involved in data. "
        "Most people stop after getting simple graphs, but I prefer doing deep dives into raw backend datasets to isolate hidden patterns, "
        "find processing anomalies, and investigate system bottlenecks."
    )

with hero_col2:
    # High impact numeric highlights directly from your real achievements
    st.metric(label="Monitoring Overhead Cut", value="-40%")
    st.metric(label="Database Reliability Lift", value="+15%")

st.markdown("---")

# 4. Interactive Navigation Workspace
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Commercial Analytics Sandbox", 
    "🛠️ Technical Ecosystem", 
    "💼 Professional Journey",
    "📜 Certifications & Background"
])

with tab1:
    st.subheader("Featured Project Workspace")
    
    # Multi-column strategic layout for your case study
    col_dash, col_alert = st.columns(2, gap="medium")
    
    with col_dash:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Case Study 1: Commercial Performance Analytics Dashboard</h3>
            <p>Automated complex commercial data workflows using Python and SQL to systematically extract and clean raw transactional inputs.</p>
            <p><strong>Impact:</strong> Unified scattered historical metrics to track organizational KPIs, regional growth vectors, and YoY product performance.</p>
            <p><small>🧰 Tools: Power BI, MS Excel, Power Query, Python</small></p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_alert:
        st.markdown("""
        <div class="metric-card">
            <h3>🔔 Case Study 2: Automated KPI Reporting & Stakeholder Alerts</h3>
            <p>Integrated transactional SQL stored procedures directly with cloud-native Power Automate configurations.</p>
            <p><strong>Impact:</strong> Eliminated manual data validation bottlenecks by triggering real-time email notifications the moment critical performance thresholds are breached.</p>
            <p><small>🧰 Tools: SQL, Power Automate, Power BI</small></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🎛️ Live Interactive Ledger Sandbox")
    st.caption("Interact with the dashboard logic below to observe how the filter query cleans up downstream transactional logs.")
    
    # Mock dataset representing structural ledger data
    mock_ledger = pd.DataFrame({
        "transaction_id": [10024, 10025, 10026, 10027, 10028],
        "region": ["Frankfurt", "Berlin", "Munich", "Hamburg", "Frankfurt"],
        "revenue_val": [1250, 4300, 1500, 950, 6100],
        "anomaly_flag": [False, False, True, False, False],
        "log_time": ["12:00", "12:05", "12:10", "12:15", "12:20"]
    })
    
    filter_choice = st.radio(
        "Apply Data Security Filter View:", 
        ["Show All System Logs", "Clean Operational Records Only", "Isolated Anomalies Only (System Exceptions)"], 
        horizontal=True
    )
    
    if filter_choice == "Clean Operational Records Only":
        display_df = mock_ledger[mock_ledger["anomaly_flag"] == False]
    elif filter_choice == "Isolated Anomalies Only (System Exceptions)":
        display_df = mock_ledger[mock_ledger["anomaly_flag"] == True]
    else:
        display_df = mock_ledger
        
    st.dataframe(display_df, use_container_width=True)
    
    # Plotly Chart reflecting user choices live
    fig = px.line(display_df, x="log_time", y="revenue_val", markers=True, title="Real-Time System Log Valuation Stream")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Validated Engineering Stack")
    st.caption("Categorized structural specializations compiled from active production environments.")
    
    sk_col1, sk_col2, sk_col3 = st.columns(3)
    with sk_col1:
        st.markdown("#### ⚙️ Functional Expertise")
        skills_f = ["Data Analysis", "Data Visualization", "Pattern Identification", "Structural Anomaly Detection", "Process Optimization", "KPI Dashboards", "User Behavior Tracking"]
        for s in skills_f:
            st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)
            
    with sk_col2:
        st.markdown("#### 💻 Technical Infrastructure")
        skills_t = ["SQL", "Python (Pandas/NumPy)", "Power BI", "Power Automate", "MS Excel (Advanced)", "Tableau", "VBA / Macros"]
        for s in skills_t:
            st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)
            
    with sk_col3:
        st.markdown("#### 🤝 Methodologies & Tools")
        skills_s = ["Analytical Thinking", "Cross-functional Collaboration", "JIRA Ticket Tracking", "Agile Methodologies", "Documentation"]
        for s in skills_s:
            st.markdown(f'<span class="skill-badge">{s}</span>', unsafe_allow_html=True)

with tab3:
    st.subheader("Professional History")
    
    # Structuring eClinicalWorks experience inside a beautiful container
    st.markdown("""
    <div class="metric-card">
        <span style="float: right; color: gray;">June 2022 – Aug 2024</span>
        <h4 style="margin: 0; color: #1C83E1;">Software Specialist (Data Analytics)</h4>
        <strong style="color: gray;">eClinicalWorks | Mumbai</strong>
        <ul style="margin-top: 10px; padding-left: 20px;">
            <li>Conducted deep-dive SQL investigations into over 200 customer master records to isolate and resolve validation errors, improving master database reliability by 15% and ensuring clear data tracking for downstream transactional reports.</li>
            <li>Built automated stakeholder alert workflows using Power Automate that flagged performance deviations and triggered targeted notifications in real time, cutting monitoring overhead by 40% across all active reporting pipelines.</li>
            <li>Designed interactive Power BI dashboards to track operational KPIs while utilizing Jira to document and coordinate high-priority data exceptions, creating unified technical workflows that improved data visibility for cross-functional teams.</li>
            <li>Coordinated cross-functional workflows across business, product, and IT teams in an agile environment, standardising reporting definitions, translating business requirements into technical solutions, and supporting 5 departments at the business-IT interface.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.subheader("Academic Foundations & Verified Certifications")
    
    ed_col1, ed_col2 = st.columns(2)
    with ed_col1:
        st.markdown("#### 🎓 Education")
        st.markdown("**MSc in Computer Science (Focus: High Integrity Systems)**")
        st.caption("Frankfurt University of Applied Sciences | Germany")
        
        st.markdown("**BSc in Computer Science**")
        st.caption("Mumbai University | India")
        
        st.markdown("🗣️ **Languages:** English (Fluent C1) | German (Actively Learning A2)")
        
    with ed_col2:
        st.markdown("#### 📜 Technical Credentials")
        st.write("✔️ **Java Programming** — IIT Bombay (Spoken Tutorial)")
        st.write("✔️ **HTML, CSS & JavaScript** — Vidyalankar School of IT")
        st.write("✔️ **MongoDB** — Vidyalankar School of IT")
