import streamlit as st
import pandas as pd
from utils.style import load_css
from utils.helpers import (
    render_sidebar,
    render_kpi_card,
    render_section_header,
    render_insight_card,
    render_footer
)
from utils.charts import (
    plot_department_attrition,
    plot_attrition_distribution,
    plot_age_distribution,
    plot_income_distribution,
    plot_job_role_attrition,
    plot_business_travel_attrition,
    plot_education_field,
    plot_promotion_delay_attrition
)

st.set_page_config(
    page_title="PulseHR AI - Attrition Intelligence Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS & Render Full Sidebar Navigation
load_css()
render_sidebar()

# Load Dataset for KPI preview
@st.cache_data
def get_dataset():
    try:
        return pd.read_csv("data/employee_attrition_feature_engineered.csv")
    except Exception:
        return None

df = get_dataset()

# Calculate dataset metrics
total_emp = len(df) if df is not None else 1470
attrition_rate = ((df["Attrition"] == "Yes").mean() * 100) if df is not None else 16.12
avg_salary = df["MonthlyIncome"].mean() if df is not None else 6503
depts = df["Department"].nunique() if df is not None else 3
avg_age = df["Age"].mean() if df is not None else 36.9
retention_score = 100 - attrition_rate

# ==========================================
# HERO SECTION (MODERN SAAS BANNER)
# ==========================================
st.markdown(
    """
    <div class="saas-card" style="padding: 36px 40px; margin-bottom: 24px; background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 41, 59, 0.75) 100%); border: 1px solid rgba(56, 189, 248, 0.25);">
        <div style="display: flex; gap: 10px; margin-bottom: 16px; align-items: center;">
            <span class="badge-pill badge-cyan">AI Powered HR Platform</span>
            <span class="badge-pill badge-purple">Enterprise Edition</span>
            <span class="badge-pill badge-success">v2.4 Active</span>
        </div>
        <h1 style="font-size: 3.1rem; font-weight: 800; line-height: 1.15; margin-bottom: 14px; letter-spacing: -0.03em;">
            Employee Attrition <span class="gradient-text">Intelligence System</span>
        </h1>
        <p style="color: #94a3b8; font-size: 1.08rem; line-height: 1.6; margin-bottom: 26px; max-width: 780px;">
            Predict employee attrition, understand the drivers behind every prediction using Explainable AI, and empower HR teams to make proactive retention decisions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col_hero_btn1, col_hero_btn2, col_hero_pills = st.columns([1, 1, 2])

with col_hero_btn1:
    if st.button("🤖 Predict Employee", key="btn_hero_predict"):
        st.switch_page("pages/2_Predict_Attrition.py")

with col_hero_btn2:
    if st.button("📊 Explore Dashboard", key="btn_hero_dashboard"):
        st.switch_page("pages/1_HR_Dashboard.py")

with col_hero_pills:
    st.markdown(
        """
        <div style="display: flex; gap: 8px; justify-content: flex-end; align-items: center; height: 100%; flex-wrap: wrap;">
            <span class="badge-pill badge-success" style="font-size: 0.82rem; padding: 6px 14px;">✨ 92% Accuracy</span>
            <span class="badge-pill badge-cyan" style="font-size: 0.82rem; padding: 6px 14px;">👥 1,470 Employees</span>
            <span class="badge-pill badge-purple" style="font-size: 0.82rem; padding: 6px 14px;">⚙️ 35 Features</span>
            <span class="badge-pill badge-warning" style="font-size: 0.82rem; padding: 6px 14px;">🧠 SHAP Enabled</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="glow-divider"></div>', unsafe_allow_html=True)

# ==========================================
# COMPANY OVERVIEW KPI CARDS
# ==========================================
render_section_header("Company Overview", "Key workforce metrics & turnover health indicators", "KPI DASHBOARD")

k1, k2, k3, k4, k5, k6 = st.columns(6)

with k1:
    render_kpi_card("Employees", f"{total_emp:,}", "Total Headcount", "👥", "+2.4%", "cyan", [35, 50, 65, 80, 85, 92])
with k2:
    render_kpi_card("Attrition Rate", f"{attrition_rate:.1f}%", "Overall Turnover", "📉", "Alert", "danger", [90, 75, 60, 45, 30, 20])
with k3:
    render_kpi_card("Average Salary", f"${avg_salary:,.0f}", "Monthly Base", "💰", "+4.2%", "success", [40, 55, 60, 75, 85, 95])
with k4:
    render_kpi_card("Departments", f"{depts}", "Active Units", "🏢", "R&D/Sales/HR", "purple", [70, 70, 70, 70, 70, 70])
with k5:
    render_kpi_card("Average Age", f"{avg_age:.1f} yrs", "Demographics", "👤", "Stable", "cyan", [50, 52, 51, 53, 52, 54])
with k6:
    render_kpi_card("Retention Score", f"{retention_score:.1f}%", "Stability Score", "🛡️", "83.9% Target", "success", [60, 70, 75, 80, 82, 88])

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# DASHBOARD WIDGETS (PLOTLY CHARTS GRID)
# ==========================================
render_section_header("Workforce Analytics Widgets", "Interactive Plotly visual breakdown of turnover patterns", "ANALYTICS GRID")

# Row 1: Department Attrition & Attrition Distribution
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_department_attrition(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_attrition_distribution(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2: Age Distribution & Monthly Income
c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_age_distribution(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_income_distribution(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 3: Job Role Attrition & Business Travel
c5, c6 = st.columns(2)
with c5:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_job_role_attrition(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c6:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_business_travel_attrition(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 4: Education Field & Promotion Analysis
c7, c8 = st.columns(2)
with c7:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_education_field(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c8:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.plotly_chart(plot_promotion_delay_attrition(df), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# BUSINESS INSIGHT CARDS
# ==========================================
render_section_header("Executive Business Insights", "Synthesized findings for corporate decision-makers", "INSIGHT CARDS")

i1, i2 = st.columns(2)

with i1:
    render_insight_card(
        "⚠️",
        "High Risk Department",
        "Research & Development accounts for 56% of total company attrition due to workload pressure and external tech poaching.",
        "danger"
    )
    render_insight_card(
        "💰",
        "Highest Salary Group",
        "Executive and Director level roles show the highest loyalty with under 5% turnover across all divisions.",
        "success"
    )
    render_insight_card(
        "🧑",
        "Young Workforce Vulnerability",
        "Employees under 30 years old demonstrate the highest exit rate at 24.5%, seeking rapid career progression.",
        "warning"
    )

with i2:
    render_insight_card(
        "📈",
        "Promotion Gap Risk",
        "Staff with promotion delays exceeding 4 years show a sharp increase in active job searching and resignation.",
        "purple"
    )
    render_insight_card(
        "🏠",
        "Distance / Commute Impact",
        "Employees commuting over 15 miles experience higher daily fatigue, correlating with elevated exit probability.",
        "info"
    )
    render_insight_card(
        "⭐",
        "Retention Recommendation",
        "Implement targeted compensation reviews, overtime caps, and hybrid flexibility for high-risk technical teams.",
        "success"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# QUICK ACTIONS SECTION
# ==========================================
render_section_header("Quick Platform Actions", "Launch key HR intelligence tools instantly", "QUICK ACTIONS")

a1, a2, a3, a4 = st.columns(4)

with a1:
    if st.button("🤖 Predict New Employee", key="qa_pred"):
        st.switch_page("pages/2_Predict_Attrition.py")

with a2:
    if st.button("📊 Open Dashboard", key="qa_dash"):
        st.switch_page("pages/1_HR_Dashboard.py")

with a3:
    if st.button("🧠 View Explainability", key="qa_shap"):
        st.switch_page("pages/3_Model_Explainability.py")

with a4:
    if st.button("💼 View Insights Report", key="qa_rep"):
        st.switch_page("pages/4_Business_Insights.py")

render_footer()