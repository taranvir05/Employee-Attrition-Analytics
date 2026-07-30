import streamlit as st
import os
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_insight_card, render_footer
from utils.model_loader import get_model_display_name, get_model_assets, get_top_model_drivers, get_model_metadata

st.set_page_config(
    page_title="Model Explainability - PulseHR",
    page_icon="🧠",
    layout="wide"
)

load_css()
render_sidebar()

# Determine SHAP explainer type based on actual model & fetch dynamic drivers
_model, _, _ = get_model_assets()
_model_class = type(_model).__name__
_is_tree = any(t in _model_class for t in ["Forest", "Tree", "Gradient", "XGB", "LGBM", "Boost"])
_explainer_name = "TreeExplainer" if _is_tree else "LinearExplainer"
_prod_model = get_model_display_name()
_meta = get_model_metadata()
_drivers = get_top_model_drivers()

_top_attr_driver = _drivers["top_attrition_driver"]
_top_ret_driver = _drivers["top_retention_driver"]
_feature_cnt_str = f"{_meta['feature_count']} Features"

render_section_header(
    "SHAP Explainable AI Dashboard",
    "Transparent decomposition of machine learning predictions into human-interpretable feature impacts",
    "EXPLAINABLE AI (XAI)"
)

# ==========================================
# SHAP SUMMARY KPI CARDS (100% DYNAMIC)
# ==========================================
k1, k2, k3, k4 = st.columns(4)

with k1:
    render_kpi_card("SHAP Explainer", _explainer_name, "Game Theory Audit", "🧠", "XAI Engine", "cyan")
with k2:
    render_kpi_card("Engineered Features", _feature_cnt_str, "Full Pipeline Coverage", "📊", "100% Audited", "purple")
with k3:
    render_kpi_card("Top Attrition Driver", _top_attr_driver, "Highest Model Weight", "⚡", "Critical", "danger")
with k4:
    render_kpi_card("Top Retention Driver", _top_ret_driver, "Reduces Risk Score", "🛡️", "Protective", "success")

st.markdown('<div style="margin-bottom: 12px;"></div>', unsafe_allow_html=True)

# ==========================================
# SHAP DASHBOARD TABS
# ==========================================
tab_global, tab_waterfall, tab_drivers = st.tabs([
    "🌍 Global Feature Importance",
    "📊 Local Waterfall Profiles",
    "⚖️ Key Risk Driver Analysis"
])

with tab_global:
    st.markdown(
        """
        <div style="margin-bottom: 16px; color: #94a3b8; font-size: 0.9rem;">
            Global SHAP summary plots quantify feature contributions across all 1,470 employees in the training & validation datasets.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(255,255,255,0.09);
                        border-radius: 16px; padding: 18px 20px 8px 20px; margin-bottom: 8px;
                        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
                <h4 style="color: #ffffff; font-weight: 700; margin-top:0; margin-bottom: 10px;">SHAP Beeswarm Summary Plot</h4>
            </div>""", unsafe_allow_html=True)
        if os.path.exists("images/shap_summary.png"):
            st.image("images/shap_summary.png", use_container_width=True)
        else:
            st.info("SHAP Summary plot image not found in images/ directory.")
        st.markdown('<p style="color: #94a3b8; font-size: 0.78rem; margin-top: 4px;">Red dots = high feature values; blue = low. Rightward shift increases attrition probability.</p>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(255,255,255,0.09);
                        border-radius: 16px; padding: 18px 20px 8px 20px; margin-bottom: 8px;
                        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
                <h4 style="color: #ffffff; font-weight: 700; margin-top:0; margin-bottom: 10px;">SHAP Feature Importance Bar Chart</h4>
            </div>""", unsafe_allow_html=True)
        if os.path.exists("images/shap_bar.png"):
            st.image("images/shap_bar.png", use_container_width=True)
        else:
            st.info("SHAP Bar plot image not found in images/ directory.")
        st.markdown('<p style="color: #94a3b8; font-size: 0.78rem; margin-top: 4px;">Ranks employee attributes by mean absolute SHAP value impact across the model.</p>', unsafe_allow_html=True)

with tab_waterfall:
    st.markdown(
        """
        <div style="margin-bottom: 16px; color: #94a3b8; font-size: 0.9rem;">
            Waterfall plots illustrate how specific employee feature values step-by-step push individual predictions above or below the baseline.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    w1, w2, w3 = st.columns(3)

    with w1:
        st.markdown('<span class="badge-pill badge-danger" style="margin-bottom: 8px;">High Attrition Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">High Risk Employee</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_high_risk.png"):
            st.image("images/waterfall_high_risk.png", use_container_width=True)
        else:
            st.info("High risk waterfall image not found.")

    with w2:
        st.markdown('<span class="badge-pill badge-warning" style="margin-bottom: 8px;">Borderline Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">Moderate Risk Profile</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_borderline.png"):
            st.image("images/waterfall_borderline.png", use_container_width=True)
        else:
            st.info("Borderline waterfall image not found.")

    with w3:
        st.markdown('<span class="badge-pill badge-success" style="margin-bottom: 8px;">Low Risk Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color: #ffffff; font-weight: 700; margin: 4px 0 8px 0;">Retained Employee</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_low_risk.png"):
            st.image("images/waterfall_low_risk.png", use_container_width=True)
        else:
            st.info("Low risk waterfall image not found.")

with tab_drivers:
    c_pos, c_neg = st.columns(2)
    
    with c_pos:
        st.markdown(
            """
            <div class="saas-card" style="border-left: 4px solid #ef4444;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                    <span style="font-size: 1.4rem;">🔴</span>
                    <h3 style="color: #ffffff; font-size: 1.1rem; font-weight: 700; margin: 0;">Positive Risk Drivers (Increase Attrition)</h3>
                </div>
                <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #f87171; font-weight: 700;">OverTime = Yes:</span> Pushes attrition probability up significantly due to burnout.
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #f87171; font-weight: 700;">Promotion Delay > 4 Yrs:</span> Long promotion gaps correlate with external job hunting.
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #f87171; font-weight: 700;">Single Marital Status:</span> Younger single staff demonstrate higher geographic mobility.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c_neg:
        st.markdown(
            """
            <div class="saas-card" style="border-left: 4px solid #22c55e;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                    <span style="font-size: 1.4rem;">🟢</span>
                    <h3 style="color: #ffffff; font-size: 1.1rem; font-weight: 700; margin: 0;">Negative Risk Drivers (Increase Retention)</h3>
                </div>
                <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #4ade80; font-weight: 700;">High Job Satisfaction (3-4):</span> Strong predictor of organizational commitment.
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #4ade80; font-weight: 700;">Higher Stock Options (Level 1-3):</span> Financial lock-in incentivizes long-term tenure.
                    </div>
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 10px 14px; border-radius: 8px;">
                        <span style="color: #4ade80; font-weight: 700;">Long Tenure with Manager:</span> Strong interpersonal alignment reduces friction.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# ACTION RECOMMENDATIONS
# ==========================================
render_section_header("Strategic HR Interventions", "Data-backed actions derived from SHAP importance ranking", "HR ACTION PLAN")

r1, r2 = st.columns(2)

with r1:
    render_insight_card(
        "⚡",
        f"{_top_attr_driver} Mitigation Strategy",
        f"{_top_attr_driver} is identified as the largest positive contributor to employee attrition risk in model feature ranking.",
        "Implement automated workload and scheduling caps when employee indicators exceed standard operational limits.",
        "danger"
    )

with r2:
    render_insight_card(
        "📈",
        "Career Velocity Acceleration",
        "Employees with promotion delays exceeding 3 years show elevated attrition risk vectors.",
        "Establish structured annual career path reviews and skill progression milestones.",
        "warning"
    )

with st.expander("📖 Technical Primer: What is SHAP?"):
    st.markdown(
        """
        <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
            <b>SHAP (SHapley Additive exPlanations)</b> is an Explainable AI methodology grounded in cooperative game theory. 
            It computes the marginal contribution of each feature to the model outcome for every individual prediction.
            Unlike black-box models, SHAP guarantees consistency and local accuracy, enabling HR leaders to explain predictions with complete auditing transparency.
        </div>
        """,
        unsafe_allow_html=True
    )

render_footer()