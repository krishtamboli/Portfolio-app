import streamlit as st
import pandas as pd
import re

# 1. Premium Page Setup
st.set_page_config(page_title="Krish Tamboli | Portfolio", page_icon="⚡", layout="wide")

# 2. Advanced Minimalist CSS Injection (Obsidian-Dark Theme)
st.markdown("""
    <style>
    /* Global Background and Text Overrides */
    .main {
        background-color: #0A0F1D !important;
        color: #E2E8F0 !important;
    }
    header, footer, .stDeployButton { display: none !important; }
    
    /* Elegant Minimalist Card Design */
    .premium-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 24px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    /* Custom Styling for Project Metric Highlights */
    .metric-value {
        font-size: 32px;
        font-weight: 700;
        color: #38BDF8;
        font-family: monospace;
    }
    .metric-label {
        font-size: 13px;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Clean Minimalist Custom Badges for Skills */
    .tech-badge {
        background-color: #1F2937;
        color: #38BDF8;
        border: 1px solid #374151;
        padding: 4px 12px;
        border-radius: 4px;
        display: inline-block;
        margin: 4px;
        font-size: 13px;
        font-family: monospace;
    }
    
    /* Custom divider line */
    .minimal-line {
        border-bottom: 1px solid #1F2937;
        margin: 25px 0;
    }
    
    /* Custom style for raw logs code block */
    code { color: #F43F5E !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation & Contact Aligned with Minimal Theme
with st.sidebar:
    st.markdown("### KRISH TAMBOLI [cite: 1]")
    st.caption("Data Systems & Analytics Specialist")
    st.markdown("<div class='minimal-line'></div>", unsafe_allow_html=True)
    
    st.markdown("🌐 **Location:** Frankfurt, Germany [cite: 2]")
    st.markdown("✉️ [krishtamboli10@gmail.com](mailto:krishtamboli10@gmail.com) [cite: 2]")
    st.markdown("📞 +49 15510685501 [cite: 2]")
    st.markdown("<div class='minimal-line'></div>", unsafe_allow_html=True)
    
    st.markdown("🔗 **Networks**")
    st.markdown("[LinkedIn Profile](https://linkedin.com) [cite: 2]")
    st.markdown("[GitHub Repositories](https://github.com/krishtamboli)")
    st.markdown("<div class='minimal-line'></div>", unsafe_allow_html=True)
    
    st.caption("💼 Current Status:")
    st.write("Open to Working Student & Data Operations roles within Germany.")

# 4. Hero Presentation Layout
st.markdown("<br>", unsafe_allow_html=True)
h_col1, h_col2, h_col3 = st.columns([3, 1, 1])

with h_col1:
    st.markdown("<h1 style='color: #FFFFFF; font-size: 42px; font-weight: 800; letter-spacing: -1px;'>Systems Engineering & Data Health</h1>", unsafe_allow_html=True)
    st.markdown(
        "I am a Master's student in **High Integrity Systems** specializing in data detective work[cite: 4]. "
        "While standard workflows focus on simple visualization, I specialize in deep-diving raw backend datasets [cite: 5] "
        "to isolate hidden structural anomalies, clean chaotic records, and eliminate system processing bottlenecks[cite: 5]."
    )

with h_col2:
    st.markdown('<div class="premium-card"><span class="metric-label">Overhead Cut</span><br><span class="metric-value">-40%</span></div>', unsafe_allow_html=True)

with h_col3:
    st.markdown('<div class="premium-card"><span class="metric-label">Reliability Lift</span><br><span class="metric-value">+15%</span></div>', unsafe_allow_html=True)

st.markdown("<div class='minimal-line'></div>", unsafe_allow_html=True)

# 5. Modular Workspace Tabs
tab1, tab2, tab3 = st.tabs(["⚡ Live Data Cleaning Pipeline", "🛠️ Verified Tech Stack", "💼 Experience & Credentials"])

with tab1:
    st.markdown("<h3 style='color: #FFFFFF;'>Live Processing Pipeline Optimization</h3>", unsafe_allow_html=True)
    st.write(
        "Instead of just describing data cleaning conceptually, this module executes live Python string parsing "
        "and type validation over an incoming corrupt production transaction stream log."
    )
    
    # The Raw Data Input
    st.markdown("#### 1. The Incoming Corrupt Log Stream")
    st.write("This raw, unstructured text block represents unvalidated application payloads entering the ecosystem:")
    
    raw_log_data = [
        "TXN_ID:10024|REG:Frankfurt|VAL:1250EUR|STATUS:VALID",
        "TXN_ID:10025|REG:Berlin|VAL:4300_ERR_NaN|STATUS:CORRUPT",
        "TXN_ID:10026|REG:Munich|VAL:1500EUR|STATUS:VALID",
        "TXN_ID:NULL_ID|REG:Hamburg|VAL:950EUR|STATUS:MISSING_ID",
        "TXN_ID:10028|REG:Frankfurt|VAL:6100EUR|STATUS:VALID"
    ]
    st.code("\n".join(raw_log_data), language="text")

    st.markdown("<div class='minimal-line'></div>", unsafe_allow_html=True)

    # The Interactive Pipeline Trigger
    st.markdown("#### 2. Execute Data Cleaning Pipeline Logic")
    st.write("Toggle the execution block to inject the cleaning engine script using Python Pandas and regular expressions (Regex).")
    
    run_pipeline = st.checkbox("🚀 Click to Run Cleaning & Optimization Script")
    
    if run_pipeline:
        parsed_records = []
        
        for line in raw_log_data:
            # Step A: String splitting and key-value mapping
            parts = dict(item.split(":") for item in line.split("|"))
            
            # Step B: Data Cleaning Logic (Regex extraction of numerical values, handling anomalies)
            raw_val = parts["VAL"]
            clean_val = re.sub(r"[^\d]", "", raw_val) # Strip out "EUR", "_ERR_NaN", etc.
            
            # Type casting with fallback routing
            if clean_val == "":
                numeric_val = 0
                anomaly_note = "Missing Value Coerced to 0"
            else:
                numeric_val = int(clean_val)
                anomaly_note = "Clean Operational Record"
                
            # Handling structural record identifiers
            if parts["TXN_ID"] == "NULL_ID":
                parts["TXN_ID"] = "00000" # Imputing dummy key for system continuity
                anomaly_note = "Structural Malformation: Null Key Imputed"
            
            parsed_records.append({
                "Transaction ID": parts["TXN_ID"],
                "Region": parts["REG"],
                "Revenue (Numeric)": numeric_val,
                "Pipeline Flag": anomaly_note
            })
            
        # Convert to Pandas DataFrame live
        df_cleaned = pd.DataFrame(parsed_records)
        
        st.success("✅ Script Executed Successfully. Output Structured Ledger Layout:")
        st.dataframe(df_cleaned, use_container_width=True)
        
        # Display the real data cleaning script inside the portfolio
        st.markdown("#### 🛠️ Code Behind This Cleaning Module")
        st.write("This is the exact logical architecture running inside the sandbox to construct the structured frame:")
        st.code("""
# Real engineering logic running live above:
parsed_records = []
for line in raw_log_data:
    parts = dict(item.split(":") for item in line.split("|"))
    
    # Strip alphabetical noise/errors from currency metrics using regex
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
        st.info("Pipeline Idle. Check the checkbox above to execute the data transformation script live.")

with tab2:
    st.markdown("<h3 style='color: #FFFFFF;'>Technical Capability Spectrum</h3>", unsafe_allow_html=True)
    
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.markdown("<h5 style='color: #38BDF8;'>Data Diagnostics</h5>", unsafe_allow_html=True)
        skills_d = ["Data Analysis", "Pattern Identification", "Structural Anomaly Detection", "Process Optimization", "User Behavior Tracking"] [cite: 9, 10]
        for s in skills_d:
            st.markdown(f'<span class="tech-badge">{s}</span>', unsafe_allow_html=True)
            
    with sc2:
        st.markdown("<h5 style='color: #38BDF8;'>Engineering Core</h5>", unsafe_allow_html=True)
        skills_e = ["SQL", "Python (Pandas/NumPy)", "Power Automate", "ETL Pipeline Design", "VBA / Macros"] [cite: 11, 12]
        for s in skills_e:
            st.markdown(f'<span class="tech-badge">{s}</span>', unsafe_allow_html=True)
            
    with sc3:
        st.markdown("<h5 style='color: #38BDF8;'>Reporting & Ops</h5>", unsafe_allow_html=True)
        skills_r = ["Power BI", "Tableau", "Advanced MS Excel", "JIRA Tracking", "Agile Methodologies"] [cite: 11, 12, 13]
        for s in skills_r:
            st.markdown(f'<span class="tech-badge">{s}</span>', unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 style='color: #FFFFFF;'>Chronological Record</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <span style="float: right; color: #9CA3AF; font-size:14px; font-family: monospace;">June 2022 – Aug 2024</span>
        <h4 style="margin: 0; color: #38BDF8;">Software Specialist (Data Analytics)</h4>
        <strong style="color: #9CA3AF;">eClinicalWorks | Mumbai</strong>
        <p style="font-size:14px; color: #E2E8F0; margin-top:10px;">
        • Conducted deep-dive SQL investigations into over 200 customer master records to isolate and resolve validation errors, improving master database reliability by 15% and ensuring clear data tracking for downstream transactional reports.<br> [cite: 17]
        • Built automated stakeholder alert workflows using Power Automate that flagged performance deviations and triggered targeted notifications in real time, cutting monitoring overhead by 40% across all active reporting pipelines.<br> [cite: 18]
        • Designed interactive Power BI dashboards to track operational KPIs while utilizing Jira to document and coordinate high-priority data exceptions, creating unified technical workflows that improved data visibility for cross-functional teams.<br> [cite: 19]
        • Coordinated cross-functional workflows across business, product, and IT teams in an agile environment, standardising reporting definitions, translating business requirements into technical solutions, and supporting 5 departments at the business-IT interface. [cite: 20]
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_ed1, col_ed2 = st.columns(2)
    with col_ed1:
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: #38BDF8; margin-top:0;">Academic Record</h4>
            <p style="margin:0; font-weight:600;">MSc in Computer Science (High Integrity Systems)</p> [cite: 33]
            <p style="color:#9CA3AF; font-size:14px; margin:0;">Frankfurt University of Applied Sciences | Germany</p> [cite: 33]
            <br>
            <p style="margin:0; font-weight:600;">BSc in Computer Science</p> [cite: 34]
            <p style="color:#9CA3AF; font-size:14px; margin:0;">Mumbai University | India</p> [cite: 34]
        </div>
        """, unsafe_allow_html=True)
    with col_ed2:
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: #38BDF8; margin-top:0;">Verified Credentials</h4>
            <p style="margin:0; font-size:14px;">✔️ Java Programming — IIT Bombay (Spoken Tutorial)</p> [cite: 30]
            <p style="margin:5px 0; font-size:14px;">✔️ MongoDB Developer — Vidyalankar School of IT</p> [cite: 31]
            <p style="margin:0; font-size:14px;">✔️ HTML, CSS & JavaScript — Vidyalankar School of IT</p> [cite: 30]
            <br>
            <p style="margin:0; font-size:14px; color:#9CA3AF;">🗣️ Languages: English (Fluent C1) | German (Actively Learning A2)</p> [cite: 36]
        </div>
        """, unsafe_allow_html=True)
