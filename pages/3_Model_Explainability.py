import streamlit as st
import os
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_insight_card, render_footer
from utils.shap_utils import get_shap_results, prettify_feature
from utils.icons import icon

st.set_page_config(
    page_title="Model Explainability - PulseHR",
    page_icon=":material/psychology:",
    layout="wide"
)

load_css()
render_sidebar()

# ── Single SHAP computation (cached) ─────────────────────────
_shap = get_shap_results()

_explainer_name  = _shap["explainer_name"]
_feature_count   = _shap["feature_count"]
_top_attr_driver = _shap["top_attrition_driver"]
_top_ret_driver  = _shap["top_retention_driver"]
_top_n_attr      = _shap["top_n_attrition"]
_top_n_ret       = _shap["top_n_retention"]
_feature_cnt_str = f"{_feature_count} Features"

render_section_header(
    "SHAP Explainable AI Dashboard",
    "Transparent decomposition of machine learning predictions into human-interpretable feature impacts",
    "EXPLAINABLE AI (XAI)",
    icon_name="brain",
)

# ==========================================
# SHAP SUMMARY KPI CARDS (100% DYNAMIC)
# ==========================================
k1, k2, k3, k4 = st.columns(4)

with k1:
    render_kpi_card("SHAP Explainer",      _explainer_name, "Game Theory Audit",   "brain",       "XAI Engine",   "cyan")
with k2:
    render_kpi_card("Engineered Features", _feature_cnt_str,"Full Pipeline Coverage","database",  "100% Audited", "purple")
with k3:
    render_kpi_card("Top Attrition Driver",_top_attr_driver,"Highest SHAP Impact",  "zap",        "Critical",     "danger")
with k4:
    render_kpi_card("Top Retention Driver",_top_ret_driver, "Reduces Risk Score",   "shield-check","Protective",  "success")

st.markdown('<div style="margin-bottom: 12px;"></div>', unsafe_allow_html=True)

# ==========================================
# SHAP DASHBOARD TABS
# ==========================================
tab_global, tab_waterfall, tab_drivers = st.tabs([
    "Global Feature Importance",
    "Local Waterfall Profiles",
    "Key Risk Driver Analysis",
])

with tab_global:
    st.markdown(
        f"""
        <div style="margin-bottom: 16px; color: #94a3b8; font-size: 0.9rem;">
            Global SHAP summary plots quantify feature contributions across all
            {_feature_count} model features in the test dataset.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(255,255,255,0.09);
                        border-radius: 16px; padding: 16px 20px 8px 20px; margin-bottom: 8px;
                        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
                <h4 style="color:#fff;font-weight:700;margin:0 0 8px 0;
                           display:flex;align-items:center;gap:8px;">
                    {icon("activity", size=15, colour="#38bdf8")} SHAP Beeswarm Summary Plot
                </h4>
            </div>""", unsafe_allow_html=True)
        if os.path.exists("images/shap_summary.png"):
            st.image("images/shap_summary.png", use_container_width=True)
        else:
            st.info("SHAP Summary plot image not found in images/ directory.")
        st.markdown(
            '<p style="color:#94a3b8;font-size:0.78rem;margin-top:4px;">'
            'Red dots = high feature values; blue = low. Rightward shift increases attrition probability.'
            '</p>',
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(f"""
            <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(255,255,255,0.09);
                        border-radius: 16px; padding: 16px 20px 8px 20px; margin-bottom: 8px;
                        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
                <h4 style="color:#fff;font-weight:700;margin:0 0 8px 0;
                           display:flex;align-items:center;gap:8px;">
                    {icon("bar-chart", size=15, colour="#38bdf8")} SHAP Feature Importance Bar Chart
                </h4>
            </div>""", unsafe_allow_html=True)
        if os.path.exists("images/shap_bar.png"):
            st.image("images/shap_bar.png", use_container_width=True)
        else:
            st.info("SHAP Bar plot image not found in images/ directory.")
        st.markdown(
            f'<p style="color:#94a3b8;font-size:0.78rem;margin-top:4px;">'
            f'Top feature by mean |SHAP|: <b style="color:#38bdf8">{_top_attr_driver}</b>. '
            f'Ranks all {_feature_count} model inputs by impact.</p>',
            unsafe_allow_html=True,
        )

with tab_waterfall:
    st.markdown(
        """
        <div style="margin-bottom: 16px; color: #94a3b8; font-size: 0.9rem;">
            Waterfall plots illustrate how specific employee feature values step-by-step
            push individual predictions above or below the baseline.
        </div>
        """,
        unsafe_allow_html=True,
    )

    w1, w2, w3 = st.columns(3)

    with w1:
        st.markdown('<span class="badge-pill badge-danger" style="margin-bottom: 8px;">High Attrition Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color:#fff;font-weight:700;margin:4px 0 8px 0;">High Risk Employee</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_high_risk.png"):
            st.image("images/waterfall_high_risk.png", use_container_width=True)
        else:
            st.info("High risk waterfall image not found.")

    with w2:
        st.markdown('<span class="badge-pill badge-warning" style="margin-bottom: 8px;">Borderline Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color:#fff;font-weight:700;margin:4px 0 8px 0;">Moderate Risk Profile</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_borderline.png"):
            st.image("images/waterfall_borderline.png", use_container_width=True)
        else:
            st.info("Borderline waterfall image not found.")

    with w3:
        st.markdown('<span class="badge-pill badge-success" style="margin-bottom: 8px;">Low Risk Case</span>', unsafe_allow_html=True)
        st.markdown('<h4 style="color:#fff;font-weight:700;margin:4px 0 8px 0;">Retained Employee</h4>', unsafe_allow_html=True)
        if os.path.exists("images/waterfall_low_risk.png"):
            st.image("images/waterfall_low_risk.png", use_container_width=True)
        else:
            st.info("Low risk waterfall image not found.")

with tab_drivers:
    c_pos, c_neg = st.columns(2)

    # ── Attrition driver rows (dynamic from SHAP) ─────────────
    max_attr = max(x["mean_abs_shap"] for x in _top_n_attr) if _top_n_attr else 1
    attr_rows_html = ""
    for item in _top_n_attr:
        bar_w = int(min(item["mean_abs_shap"] / max_attr * 100, 100))
        attr_rows_html += f"""
        <div style="background:rgba(30,41,59,0.5);padding:10px 14px;border-radius:8px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                <span style="color:#f87171;font-weight:700;font-size:0.87rem;">{item['pretty']}</span>
                <span style="color:#94a3b8;font-size:0.74rem;">+{item['mean_abs_shap']:.4f} SHAP</span>
            </div>
            <div style="background:rgba(239,68,68,0.15);border-radius:4px;height:5px;">
                <div style="background:#ef4444;width:{bar_w}%;height:100%;border-radius:4px;"></div>
            </div>
        </div>"""

    with c_pos:
        st.markdown(
            f"""
            <div class="saas-card" style="border-left:4px solid #ef4444;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
                    {icon("alert-triangle", size=18, colour="#f87171")}
                    <h3 style="color:#fff;font-size:1.05rem;font-weight:700;margin:0;">
                        Positive Risk Drivers
                    </h3>
                </div>
                <p style="color:#94a3b8;font-size:0.8rem;margin:0 0 12px 0;">
                    Features that most increase attrition probability for this model.
                </p>
                <div style="display:flex;flex-direction:column;gap:8px;">
                    {attr_rows_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Retention driver rows ─────────────────────────────────
    max_ret_abs = max(abs(x["mean_signed_shap"]) for x in _top_n_ret) if _top_n_ret else 1
    ret_rows_html = ""
    for item in _top_n_ret:
        bar_w = int(min(abs(item["mean_signed_shap"]) / max_ret_abs * 100, 100))
        ret_rows_html += f"""
        <div style="background:rgba(30,41,59,0.5);padding:10px 14px;border-radius:8px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                <span style="color:#4ade80;font-weight:700;font-size:0.87rem;">{item['pretty']}</span>
                <span style="color:#94a3b8;font-size:0.74rem;">{item['mean_signed_shap']:.4f} SHAP</span>
            </div>
            <div style="background:rgba(34,197,94,0.15);border-radius:4px;height:5px;">
                <div style="background:#22c55e;width:{bar_w}%;height:100%;border-radius:4px;"></div>
            </div>
        </div>"""

    with c_neg:
        st.markdown(
            f"""
            <div class="saas-card" style="border-left:4px solid #22c55e;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
                    {icon("shield-check", size=18, colour="#4ade80")}
                    <h3 style="color:#fff;font-size:1.05rem;font-weight:700;margin:0;">
                        Negative Risk Drivers
                    </h3>
                </div>
                <p style="color:#94a3b8;font-size:0.8rem;margin:0 0 12px 0;">
                    Features that most reduce attrition probability for this model.
                </p>
                <div style="display:flex;flex-direction:column;gap:8px;">
                    {ret_rows_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# STRATEGIC HR INTERVENTIONS (Equal height)
# ==========================================
render_section_header(
    "Strategic HR Interventions",
    "Data-backed actions derived from SHAP importance ranking",
    "HR ACTION PLAN",
    icon_name="trending-up",
)

_driver_1 = _top_n_attr[0]["pretty"] if len(_top_n_attr) > 0 else _top_attr_driver
_driver_2 = _top_n_attr[1]["pretty"] if len(_top_n_attr) > 1 else "Promotion Delays"

# Equal-height row — both cards in one HTML block, no Streamlit columns
st.markdown(
    f"""
    <div style="display:flex;gap:18px;align-items:stretch;margin-bottom:18px;">
        <div style="flex:1;background:rgba(15,23,42,0.75);
                    border-left:4px solid #ef4444;border-top:1px solid rgba(255,255,255,0.06);
                    border-right:1px solid rgba(255,255,255,0.06);border-bottom:1px solid rgba(255,255,255,0.06);
                    border-radius:14px;padding:18px 20px;box-sizing:border-box;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                {icon("zap", size=18, colour="#f87171")}
                <h4 style="color:#fff;font-size:1rem;font-weight:700;margin:0;">
                    {_driver_1} Mitigation Strategy
                </h4>
            </div>
            <p style="color:#cbd5e1;font-size:0.87rem;margin:0 0 8px 0;line-height:1.6;">
                <b style="color:#f87171;">'{_driver_1}'</b> is identified as the #1 positive SHAP
                contributor to employee attrition risk in this model.
            </p>
            <p style="color:#94a3b8;font-size:0.82rem;margin:0;line-height:1.5;">
                Implement proactive monitoring and policy guardrails to reduce this risk factor
                across all teams. Prioritise employees with compounding risk signals.
            </p>
        </div>
        <div style="flex:1;background:rgba(15,23,42,0.75);
                    border-left:4px solid #f59e0b;border-top:1px solid rgba(255,255,255,0.06);
                    border-right:1px solid rgba(255,255,255,0.06);border-bottom:1px solid rgba(255,255,255,0.06);
                    border-radius:14px;padding:18px 20px;box-sizing:border-box;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                {icon("trending-up", size=18, colour="#fbbf24")}
                <h4 style="color:#fff;font-size:1rem;font-weight:700;margin:0;">
                    {_driver_2} Intervention
                </h4>
            </div>
            <p style="color:#cbd5e1;font-size:0.87rem;margin:0 0 8px 0;line-height:1.6;">
                <b style="color:#fbbf24;">'{_driver_2}'</b> is the #2 SHAP-ranked attrition driver.
                Stagnation in this area is a compounding flight-risk signal.
            </p>
            <p style="color:#94a3b8;font-size:0.82rem;margin:0;line-height:1.5;">
                Establish structured annual career path reviews and skill progression milestones.
                Early intervention at the 2-year mark significantly reduces departure probability.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("Technical Primer: What is SHAP?"):
    st.markdown(
        f"""
        <div style="color:#cbd5e1;font-size:0.9rem;line-height:1.6;">
            <b>SHAP (SHapley Additive exPlanations)</b> is an Explainable AI methodology grounded
            in cooperative game theory. It computes the marginal contribution of each feature to
            the model outcome for every individual prediction. The current model uses
            <b style="color:#38bdf8;">{_explainer_name}</b>, computing values across
            {_feature_count} engineered features. Unlike black-box models, SHAP guarantees
            consistency and local accuracy — enabling HR leaders to explain predictions with
            complete auditing transparency.
        </div>
        """,
        unsafe_allow_html=True,
    )

render_footer()