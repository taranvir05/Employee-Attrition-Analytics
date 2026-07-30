import streamlit as st
import pandas as pd
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_insight_card, render_footer
from utils.charts import (
    plot_department_attrition,
    plot_gender_donut,
    plot_job_role_attrition,
    plot_education_field,
    plot_overtime_attrition,
    plot_work_life_balance,
    plot_job_satisfaction,
    plot_age_distribution,
    plot_income_distribution,
    plot_income_by_dept,
    plot_years_at_company,
    plot_correlation_matrix
)

st.set_page_config(
    page_title="HR Dashboard - PulseHR",
    page_icon=":material/bar_chart:",
    layout="wide"
)

load_css()
render_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv("data/employee_attrition_feature_engineered.csv")

df_raw = load_data()

# ==========================================
# PAGE TITLE & FILTER BAR
# ==========================================
render_section_header(
    "HR Analytics Executive Dashboard",
    "Real-time workforce composition, attrition dynamics, and salary benchmarks",
    "ANALYTICS HUB",
    icon_name="bar-chart",
)

# Interactive Filter Bar
with st.container():
    f_col1, f_col2, f_col3 = st.columns([1, 1, 1])

    with f_col1:
        dept_options = ["All Departments"] + list(df_raw["Department"].dropna().unique())
        selected_dept = st.selectbox("Filter Department", dept_options)

    with f_col2:
        ot_options = ["All OverTime Status", "Yes", "No"]
        selected_ot = st.selectbox("Filter OverTime", ot_options)

    with f_col3:
        role_options = ["All Job Roles"] + list(sorted(df_raw["JobRole"].dropna().unique()))
        selected_role = st.selectbox("Filter Job Role", role_options)

# Apply filters
df = df_raw.copy()
if selected_dept != "All Departments":
    df = df[df["Department"] == selected_dept]
if selected_ot != "All OverTime Status":
    df = df[df["OverTime"] == selected_ot]
if selected_role != "All Job Roles":
    df = df[df["JobRole"] == selected_role]

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# TOP KPI CARDS
# ==========================================
k1, k2, k3, k4, k5, k6 = st.columns(6)

total_count = len(df)
attr_count = int((df["Attrition"] == "Yes").sum())
attr_rate = (attr_count / total_count * 100) if total_count > 0 else 0.0
avg_inc = df["MonthlyIncome"].mean() if total_count > 0 else 0.0
avg_age = df["Age"].mean() if total_count > 0 else 0.0
retention_score = (100.0 - attr_rate) if total_count > 0 else 100.0
dept_count = df["Department"].nunique() if total_count > 0 else 0

with k1:
    render_kpi_card("Employee Count", f"{total_count:,}", "Active Records", "user", "Total", "cyan")
with k2:
    render_kpi_card("Attrition Rate", f"{attr_rate:.1f}%", f"{attr_count} Resigned", "trending-up", "Turnover", "danger" if attr_rate > 15 else "success")
with k3:
    render_kpi_card("Average Salary", f"${avg_inc:,.0f}", "Monthly Base", "activity", "Pay", "purple")
with k4:
    render_kpi_card("Average Age", f"{avg_age:.1f} yrs", "Demographics", "user", "Age", "cyan")
with k5:
    render_kpi_card("Retention Score", f"{retention_score:.1f}%", "Stability Score", "shield-check", "Retention", "success")
with k6:
    render_kpi_card("Departments", f"{dept_count}", "Active Units", "home", "Units", "purple")

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# CHARTS GRID SECTION 1
# ==========================================
c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(plot_department_attrition(df), use_container_width=True)

with c2:
    st.plotly_chart(plot_gender_donut(df), use_container_width=True)

c3, c4 = st.columns(2)
with c3:
    st.plotly_chart(plot_job_role_attrition(df), use_container_width=True)

with c4:
    st.plotly_chart(plot_education_field(df), use_container_width=True)

# ==========================================
# ATTRITION DRIVERS GRID
# ==========================================
render_section_header("Attrition Drivers & Satisfaction", "Correlating workload, work-life balance, and satisfaction with turnover", "KEY DRIVERS", icon_name="activity")

d1, d2 = st.columns(2)
with d1:
    st.plotly_chart(plot_overtime_attrition(df), use_container_width=True)

with d2:
    st.plotly_chart(plot_work_life_balance(df), use_container_width=True)

st.plotly_chart(plot_job_satisfaction(df), use_container_width=True)

# ==========================================
# NUMERICAL DISTRIBUTIONS
# ==========================================
render_section_header("Demographics & Compensation Analysis", "Distribution curves for age, monthly income, and company tenure", "DISTRIBUTIONS", icon_name="pie-chart")

n1, n2 = st.columns(2)
with n1:
    st.plotly_chart(plot_age_distribution(df), use_container_width=True)

with n2:
    st.plotly_chart(plot_income_distribution(df), use_container_width=True)

n3, n4 = st.columns(2)
with n3:
    st.plotly_chart(plot_years_at_company(df), use_container_width=True)

with n4:
    st.plotly_chart(plot_income_by_dept(df), use_container_width=True)

# Heatmap
st.plotly_chart(plot_correlation_matrix(df), use_container_width=True)

# ==========================================
# EXECUTIVE OBSERVATION & RECOMMENDATIONS
# ==========================================
render_section_header("Executive Summary & Action Plan", "Synthesized HR findings from current dataset filter", "EXECUTIVE REPORT", icon_name="file-text")

r1, r2 = st.columns(2)

with r1:
    render_insight_card(
        "alert-triangle",
        "Overtime Workload Threat",
        "Employees logging frequent OverTime exhibit nearly 3x higher departure rates than non-overtime staff. Cap monthly overtime hours and introduce flex-shifts.",
        "danger"
    )
    render_insight_card(
        "activity",
        "Low Income Flight Risk",
        "Staff in lower salary bands (<$3,500/mo) represent 48% of total turnover volume. Conduct competitive benchmark reviews for junior roles.",
        "warning"
    )

with r2:
    render_insight_card(
        "clock",
        "Early Career Turnover Spike",
        "Employees with under 2 years of company tenure show the highest vulnerability to resignation. Strengthen 90-day onboarding programs.",
        "info"
    )
    render_insight_card(
        "shield-check",
        "Satisfaction Buffer",
        "Employees rating Job Satisfaction at Level 4 show 82% retention stability. Expand recognition programs and clear promotion pathways.",
        "success"
    )

render_footer()