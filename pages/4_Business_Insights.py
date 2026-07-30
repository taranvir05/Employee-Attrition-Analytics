import streamlit as st
import pandas as pd
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_footer
from utils.charts import (
    plot_department_attrition,
    plot_overtime_attrition,
    plot_job_satisfaction,
    plot_income_vs_attrition_box,
    plot_work_life_balance
)

st.set_page_config(
    page_title="Business Insights - PulseHR",
    page_icon=":material/trending_up:",
    layout="wide"
)

load_css()
render_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv("data/employee_attrition_feature_engineered.csv")

df = load_data()

attrition_rate = (df["Attrition"] == "Yes").mean() * 100
highest_dept = df[df["Attrition"] == "Yes"]["Department"].value_counts().idxmax()
highest_role = df[df["Attrition"] == "Yes"]["JobRole"].value_counts().idxmax()

render_section_header(
    "Executive HR Business Briefing",
    "Data-driven findings, quantified financial & operational impacts, and strategic intervention roadmaps",
    "EXECUTIVE REPORT",
    icon_name="trending-up",
)

highest_dept_attr_count = (df[(df["Department"] == highest_dept) & (df["Attrition"] == "Yes")].shape[0])
total_attr_count = (df["Attrition"] == "Yes").sum()
highest_dept_pct = (highest_dept_attr_count / total_attr_count * 100) if total_attr_count > 0 else 0
highest_role_attr_count = (df[(df["JobRole"] == highest_role) & (df["Attrition"] == "Yes")].shape[0])

# ==========================================
# EXECUTIVE SUMMARY TOP CARDS
# ==========================================
k1, k2, k3 = st.columns(3)

with k1:
    render_kpi_card("Overall Attrition", f"{attrition_rate:.1f}%", "Total Turnover Benchmark", "trending-up", "Turnover", "danger")
with k2:
    render_kpi_card("Highest Risk Dept", f"{highest_dept}", f"Accounts for {highest_dept_pct:.1f}% Turnover", "home", "Action Needed", "warning")
with k3:
    render_kpi_card("Highest Risk Role", f"{highest_role}", f"{highest_role_attr_count} Resignations", "user", "Priority 1", "purple")

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# INSIGHT CARD 1: DEPARTMENT ATTRITION
# ==========================================
total_attr = (df["Attrition"] == "Yes").sum()
rd_attr_pct = (df[(df["Department"] == "Research & Development") & (df["Attrition"] == "Yes")].shape[0] / total_attr) * 100
sales_attr_pct = (df[(df["Department"] == "Sales") & (df["Attrition"] == "Yes")].shape[0] / total_attr) * 100

ot_yes_rate = (df[df["OverTime"] == "Yes"]["Attrition"] == "Yes").mean() * 100
ot_no_rate = (df[df["OverTime"] == "No"]["Attrition"] == "Yes").mean() * 100

med_inc_yes = int(df[df["Attrition"] == "Yes"]["MonthlyIncome"].median())
med_inc_no = int(df[df["Attrition"] == "No"]["MonthlyIncome"].median())

wlb1_rate = (df[df["WorkLifeBalance"] == 1]["Attrition"] == "Yes").mean() * 100

col_chart1, col_text1 = st.columns([1.1, 1])

with col_chart1:
    st.plotly_chart(plot_department_attrition(df), use_container_width=True)

with col_text1:
    st.markdown('<span class="badge-pill badge-danger" style="margin-bottom: 8px;">Insight 01 • Department Dynamics</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 6px 0;">Research & Development and Sales Lead Turnover</h3>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; margin-top: 12px;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #38bdf8; font-weight: 700;">Observation:</span>
                <span style="color: #cbd5e1;"> R&amp;D accounts for {rd_attr_pct:.1f}% of total company resignations, followed by Sales at {sales_attr_pct:.1f}%.</span>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #f87171; font-weight: 700;">Business Impact:</span>
                <span style="color: #cbd5e1;"> Project delays in core engineering initiatives and lost sales client relationships.</span>
            </div>
            <div style="background: rgba(34, 197, 94, 0.12); padding: 12px; border-radius: 10px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <span style="color: #4ade80; font-weight: 700;">Actionable Plan:</span>
                <span style="color: #f1f5f9;"> Deploy department-specific engagement pulses and review workload distribution in technical teams.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# INSIGHT CARD 2: OVERTIME IMPACT
# ==========================================
col_chart2, col_text2 = st.columns([1.1, 1])

with col_chart2:
    st.plotly_chart(plot_overtime_attrition(df), use_container_width=True)

with col_text2:
    st.markdown('<span class="badge-pill badge-warning" style="margin-bottom: 8px;">Insight 02 • Overtime & Burnout</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 6px 0;">Overtime Workers Show Higher Exit Rate</h3>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; margin-top: 12px;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #38bdf8; font-weight: 700;">Observation:</span>
                <span style="color: #cbd5e1;"> {ot_yes_rate:.1f}% of overtime employees leave, compared to just {ot_no_rate:.1f}% among non-overtime staff.</span>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #f87171; font-weight: 700;">Business Impact:</span>
                <span style="color: #cbd5e1;"> Severe employee burnout, lowered productivity, and compounding turnover in remaining team members.</span>
            </div>
            <div style="background: rgba(34, 197, 94, 0.12); padding: 12px; border-radius: 10px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <span style="color: #4ade80; font-weight: 700;">Actionable Plan:</span>
                <span style="color: #f1f5f9;"> Enforce mandatory overtime caps, hire temporary contractors for peak project cycles, and introduce flexible hours.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# INSIGHT CARD 3: MONTHLY INCOME
# ==========================================
col_chart3, col_text3 = st.columns([1.1, 1])

with col_chart3:
    st.plotly_chart(plot_income_vs_attrition_box(df), use_container_width=True)

with col_text3:
    st.markdown('<span class="badge-pill badge-purple" style="margin-bottom: 8px;">Insight 03 • Compensation Disparity</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 6px 0;">Lower Income Salary Bands Drive Resignations</h3>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; margin-top: 12px;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #38bdf8; font-weight: 700;">Observation:</span>
                <span style="color: #cbd5e1;"> Median monthly income for departing employees is ${med_inc_yes:,} vs ${med_inc_no:,} for retained employees.</span>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #f87171; font-weight: 700;">Business Impact:</span>
                <span style="color: #cbd5e1;"> Poaching by market competitors offering compensation bumps.</span>
            </div>
            <div style="background: rgba(34, 197, 94, 0.12); padding: 12px; border-radius: 10px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <span style="color: #4ade80; font-weight: 700;">Actionable Plan:</span>
                <span style="color: #f1f5f9;"> Re-index base pay for mid-level technical roles and introduce retention stock options.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# INSIGHT CARD 4: WORK LIFE BALANCE & SATISFACTION
# ==========================================
col_chart4, col_text4 = st.columns([1.1, 1])

with col_chart4:
    st.plotly_chart(plot_work_life_balance(df), use_container_width=True)

with col_text4:
    st.markdown('<span class="badge-pill badge-cyan" style="margin-bottom: 8px;">Insight 04 • Work-Life Balance</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 6px 0;">Poor Work-Life Rating (Level 1) Triples Risk</h3>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; margin-top: 12px;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #38bdf8; font-weight: 700;">Observation:</span>
                <span style="color: #cbd5e1;"> Staff rating work-life balance at Level 1 suffer a {wlb1_rate:.1f}% departure rate.</span>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 12px; border-radius: 10px;">
                <span style="color: #f87171; font-weight: 700;">Business Impact:</span>
                <span style="color: #cbd5e1;"> Low employer brand ratings on Glassdoor and reduced candidate recruitment conversion.</span>
            </div>
            <div style="background: rgba(34, 197, 94, 0.12); padding: 12px; border-radius: 10px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <span style="color: #4ade80; font-weight: 700;">Actionable Plan:</span>
                <span style="color: #f1f5f9;"> Introduce hybrid work policies, wellness stipends, and quarterly manager feedback scorecards.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# STRATEGIC ROADMAP CARD
# ==========================================
render_section_header("Strategic Executive Roadmap", "Prioritized retention action plan for leadership team", "STRATEGY ROADMAP", icon_name="activity")

st.markdown(
    """
    <div class="saas-card" style="border: 1px solid rgba(56, 189, 248, 0.3);">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px;">
            <div style="background: rgba(30, 41, 59, 0.5); padding: 16px; border-radius: 12px; border-top: 3px solid #ef4444;">
                <div style="color: #ef4444; font-weight: 800; font-size: 0.82rem;">PHASE 1 (IMMEDIATE)</div>
                <div style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">Overtime & Workload Cap</div>
                <div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.5;">Audit top 10% highest overtime logging employees in R&D and deploy immediate relief staff.</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 16px; border-radius: 12px; border-top: 3px solid #f59e0b;">
                <div style="color: #f59e0b; font-weight: 800; font-size: 0.82rem;">PHASE 2 (30-60 DAYS)</div>
                <div style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">Compensation Alignment</div>
                <div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.5;">Adjust entry and mid-level salary bands for Laboratory Technicians and Sales Executives.</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 16px; border-radius: 12px; border-top: 3px solid #22c55e;">
                <div style="color: #22c55e; font-weight: 800; font-size: 0.82rem;">PHASE 3 (90 DAYS)</div>
                <div style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">Predictive HR Integration</div>
                <div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.5;">Embed PulseHR ML prediction engine into quarterly manager reviews for early intervention.</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

render_footer()