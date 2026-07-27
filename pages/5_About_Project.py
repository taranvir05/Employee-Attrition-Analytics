import streamlit as st
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_footer

st.set_page_config(
    page_title="About Project - PulseHR",
    page_icon="📄",
    layout="wide"
)

load_css()
render_sidebar()

render_section_header(
    "PulseHR Platform Architecture & Documentation",
    "End-to-end Machine Learning, Explainable AI (SHAP), and HR Analytics System Specifications",
    "SYSTEM SPECIFICATIONS"
)

# ==========================================
# PROBLEM STATEMENT & OBJECTIVES
# ==========================================
col_prob, col_obj = st.columns(2)

with col_prob:
    st.markdown('<div class="saas-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<span class="badge-pill badge-cyan" style="margin-bottom: 8px;">Business Problem</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 4px 0 10px 0;">The Cost of Unplanned Employee Turnover</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
            Employee turnover costs organizations 1.5x to 2x an employee's annual salary in recruiting, onboarding, and lost productivity.
            PulseHR addresses this challenge by deploying predictive ML models to flag flight risk early and explain <b>why</b> staff leave using SHAP Shapley values.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_obj:
    st.markdown('<div class="saas-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<span class="badge-pill badge-purple" style="margin-bottom: 8px;">Key Deliverables</span>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-weight: 700; margin: 4px 0 10px 0;">Platform Engineering Goals</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.85rem;">
            <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">✔ 92%+ Predictive Accuracy</div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">✔ Transparent SHAP XAI</div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">✔ Executive Analytics Hub</div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">✔ Real-Time Risk Profiler</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# SYSTEM WORKFLOW ARCHITECTURE (VISUAL NODES)
# ==========================================
render_section_header("System Pipeline Architecture", "Data ingestion through feature engineering to ML inference & SHAP audit", "WORKFLOW")

st.markdown(
    """
    <div class="saas-card">
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; text-align: center;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">📥</div>
                <div style="color: #38bdf8; font-weight: 700; font-size: 0.85rem;">1. Data Ingestion</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">IBM HR Dataset (1,470 records)</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(99, 102, 241, 0.2);">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">⚙️</div>
                <div style="color: #818cf8; font-weight: 700; font-size: 0.85rem;">2. Feature Pipeline</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">One-Hot Encoding & Standard Scaling</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(168, 85, 247, 0.2);">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">🤖</div>
                <div style="color: #c084fc; font-weight: 700; font-size: 0.85rem;">3. ML Ensemble</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">Random Forest Classifier</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">🧠</div>
                <div style="color: #38bdf8; font-weight: 700; font-size: 0.85rem;">4. SHAP XAI Engine</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">TreeExplainer Shapley Analysis</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">📊</div>
                <div style="color: #4ade80; font-weight: 700; font-size: 0.85rem;">5. SaaS Dashboard</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">Streamlit + Plotly Interface</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# MODEL COMPARISON MATRIX TABLE
# ==========================================
render_section_header("Machine Learning Model Comparison Matrix", "Evaluation metrics across candidate algorithms", "MODEL BENCHMARKS")

st.markdown(
    """
    <div class="saas-card">
        <table style="width: 100%; border-collapse: collapse; color: #cbd5e1; font-size: 0.88rem; text-align: left;">
            <thead>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #ffffff;">
                    <th style="padding: 12px;">Algorithm</th>
                    <th style="padding: 12px;">Role / Purpose</th>
                    <th style="padding: 12px;">Accuracy</th>
                    <th style="padding: 12px;">ROC-AUC</th>
                    <th style="padding: 12px;">Status</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 12px; font-weight: 700; color: #ffffff;">Logistic Regression</td>
                    <td style="padding: 12px;">Linear Baseline Classification</td>
                    <td style="padding: 12px;">84.2%</td>
                    <td style="padding: 12px;">0.78</td>
                    <td style="padding: 12px;"><span class="badge-pill badge-cyan">Baseline</span></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 12px; font-weight: 700; color: #ffffff;">Decision Tree</td>
                    <td style="padding: 12px;">Non-Linear Single Tree</td>
                    <td style="padding: 12px;">81.6%</td>
                    <td style="padding: 12px;">0.71</td>
                    <td style="padding: 12px;"><span class="badge-pill badge-warning">Evaluated</span></td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: 800; color: #38bdf8;">Random Forest Ensemble</td>
                    <td style="padding: 12px;">Production Bagging Model</td>
                    <td style="padding: 12px; font-weight: 800; color: #4ade80;">92.4%</td>
                    <td style="padding: 12px; font-weight: 800; color: #4ade80;">0.89</td>
                    <td style="padding: 12px;"><span class="badge-pill badge-success">Selected Model</span></td>
                </tr>
            </tbody>
        </table>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# GITHUB & SYSTEM METRICS
# ==========================================
c_tech, c_stat = st.columns(2)

with c_tech:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #ffffff; font-weight: 700; margin-top:0;">🚀 Future Enhancements Roadmap</h4>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: #cbd5e1;">
            <div>• Real-time REST API integration with Workday & SAP SuccessFactors</div>
            <div>• Automated weekly email alerts to HR managers for high-risk staff</div>
            <div>• XGBoost & LightGBM model benchmarking</div>
            <div>• Role-based access control (RBAC) authentication</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with c_stat:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #ffffff; font-weight: 700; margin-top:0;">📊 Project Statistics Summary</h4>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.82rem;">
            <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                <div style="color: #94a3b8;">DATASET RECORDS</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #ffffff;">1,470 Employees</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                <div style="color: #94a3b8;">PIPELINE FEATURES</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #38bdf8;">38 Variables</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                <div style="color: #94a3b8;">XAI FRAMEWORK</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #c084fc;">SHAP v0.42</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                <div style="color: #94a3b8;">AUTHOR & ROLE</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #4ade80;">Taranvir Kaur</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

render_footer()