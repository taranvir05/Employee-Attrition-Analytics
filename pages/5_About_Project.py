import streamlit as st
from utils.style import load_css
from utils.helpers import render_sidebar, render_kpi_card, render_section_header, render_footer
from utils.model_loader import get_model_display_name, get_model_metadata, get_model_metrics
from utils.icons import icon

st.set_page_config(
    page_title="About Project - PulseHR",
    page_icon=":material/description:",
    layout="wide"
)

load_css()
render_sidebar()

_prod_model = get_model_display_name()
_meta = get_model_metadata()

_metrics_data = get_model_metrics()
_test_m = _metrics_data.get("test_metrics", {})
_stats = _metrics_data.get("dataset_stats", {})
_comp_list = _metrics_data.get("model_comparison", [])

render_section_header(
    "PulseHR Platform Architecture & Documentation",
    "End-to-end Machine Learning, Explainable AI (SHAP), and HR Analytics System Specifications",
    "SYSTEM SPECIFICATIONS",
    icon_name="file-text",
)

# ==========================================
# PROBLEM STATEMENT & OBJECTIVES
# ==========================================
col_prob, col_obj = st.columns(2)

with col_prob:
    st.markdown(
        """
        <div class="saas-card" style="height: 100%;">
            <span class="badge-pill badge-cyan" style="margin-bottom: 8px;">Business Problem</span>
            <h3 style="color: #ffffff; font-weight: 700; margin: 4px 0 10px 0;">The Cost of Unplanned Employee Turnover</h3>
            <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                Employee turnover costs organizations 1.5x to 2x an employee's annual salary in recruiting,
                onboarding, and lost productivity. PulseHR addresses this challenge by deploying predictive
                ML models to flag flight risk early and explain <b>why</b> staff leave using SHAP Shapley values.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_obj:
    st.markdown(
        f"""
        <div class="saas-card" style="height: 100%;">
            <span class="badge-pill badge-purple" style="margin-bottom: 8px;">Key Deliverables</span>
            <h3 style="color: #ffffff; font-weight: 700; margin: 4px 0 10px 0;">Platform Engineering Goals</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.85rem;">
                <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">[+] {_prod_model} Model</div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">[+] Transparent SHAP XAI</div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">[+] Executive Analytics Hub</div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 8px 12px; border-radius: 8px; color: #4ade80;">[+] Real-Time Risk Profiler</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# SYSTEM WORKFLOW ARCHITECTURE (VISUAL NODES)
# ==========================================
render_section_header("System Pipeline Architecture", "Data ingestion through feature engineering to ML inference & SHAP audit", "WORKFLOW", icon_name="activity")

st.markdown(
    f"""
    <div class="saas-card">
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; text-align: center;">
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:6px;">{icon('database', size=22, colour='#38bdf8')}</div>
                <div style="color: #38bdf8; font-weight: 700; font-size: 0.85rem;">1. Data Ingestion</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">IBM HR Dataset ({_stats.get('total_records', 1470):,} records)</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(99, 102, 241, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:6px;">{icon('settings', size=22, colour='#818cf8')}</div>
                <div style="color: #818cf8; font-weight: 700; font-size: 0.85rem;">2. Feature Pipeline</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">One-Hot Encoding &amp; Standard Scaling</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(168, 85, 247, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:6px;">{icon('cpu', size=22, colour='#c084fc')}</div>
                <div style="color: #c084fc; font-weight: 700; font-size: 0.85rem;">3. ML Model</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">{_prod_model}</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:6px;">{icon('brain', size=22, colour='#38bdf8')}</div>
                <div style="color: #38bdf8; font-weight: 700; font-size: 0.85rem;">4. SHAP XAI Engine</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">LinearExplainer / Shapley Analysis</div>
            </div>
            <div style="background: rgba(30, 41, 59, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:6px;">{icon('bar-chart', size=22, colour='#4ade80')}</div>
                <div style="color: #4ade80; font-weight: 700; font-size: 0.85rem;">5. SaaS Dashboard</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-top: 4px;">Streamlit + Plotly Interface</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# PRODUCTION MODEL SNAPSHOT CARDS
# ==========================================
render_section_header("Production Model Performance Snapshot", "Notebook 09 verified evaluation metrics on unseen 20% test partition (294 samples)", "MODEL METRICS", icon_name="cpu")

s1, s2, s3, s4, s5 = st.columns(5)
with s1:
    render_kpi_card("Selected Model", _prod_model, "Primary Engine", "cpu", "Best Model", "cyan")
with s2:
    render_kpi_card("Test Accuracy", f"{_test_m.get('accuracy', 87.76):.2f}%", "Unseen Test Set", "target", "Notebook 09", "success")
with s3:
    render_kpi_card("Precision", f"{_test_m.get('precision', 73.91):.2f}%", "Positive Class (1)", "activity", "Notebook 09", "purple")
with s4:
    render_kpi_card("Recall", f"{_test_m.get('recall', 36.17):.2f}%", "Sensitivity", "search", "Notebook 09", "warning")
with s5:
    render_kpi_card("F1-Score / ROC-AUC", f"{_test_m.get('f1_score', 48.57):.2f}% / {(_test_m.get('roc_auc', 83.26)/100 if _test_m.get('roc_auc', 83.26)>1 else _test_m.get('roc_auc', 83.26)):.2f}", "Harmonic Mean / AUC", "trending-up", "Notebook 09", "cyan")

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

s6, s7, s8, s9 = st.columns(4)
with s6:
    render_kpi_card("Training Partition", f"{_stats.get('train_samples', 1176):,} Rows", "80% Split", "bar-chart", "Notebook 07", "purple")
with s7:
    render_kpi_card("Testing Partition", f"{_stats.get('test_samples', 294):,} Rows", "20% Holdout Split", "activity", "Notebook 07", "cyan")
with s8:
    render_kpi_card("Engineered Features", f"{_stats.get('feature_count', 59)} Features", "Pipeline Dimension", "settings", "Notebook 06", "success")
with s9:
    render_kpi_card("Explainability Engine", "LinearExplainer", "SHAP XAI Active", "brain", "Notebook 10", "warning")

st.markdown('<div style="margin-bottom: 16px;"></div>', unsafe_allow_html=True)

# ==========================================
# MODEL COMPARISON MATRIX TABLE (DYNAMIC)
# ==========================================
render_section_header("Machine Learning Model Comparison Matrix", "Evaluation benchmarks computed across candidate algorithms in Notebook 09", "MODEL BENCHMARKS", icon_name="bar-chart")

rows_html = ""
for item in _comp_list:
    is_sel = (item["model"] == _prod_model or "Selected" in item.get("status", ""))
    row_bg = "background: rgba(56, 189, 248, 0.08);" if is_sel else ""
    text_col = "#38bdf8" if is_sel else "#ffffff"
    badge_cls = "badge-success" if is_sel else "badge-cyan"

    rows_html += f"""
    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); {row_bg}">
        <td style="padding: 12px; font-weight: {'800' if is_sel else '600'}; color: {text_col};">{item['model']}</td>
        <td style="padding: 12px; font-weight: 700; color: #4ade80;">{item['accuracy']:.2f}%</td>
        <td style="padding: 12px;">{item['precision']:.2f}%</td>
        <td style="padding: 12px;">{item['recall']:.2f}%</td>
        <td style="padding: 12px;">{item['f1'] if 'f1' in item else item.get('f1_score', 0):.2f}%</td>
        <td style="padding: 12px; font-weight: 700; color: #c084fc;">{item['roc_auc']/100:.4f}</td>
        <td style="padding: 12px;"><span class="badge-pill {badge_cls}">{item.get('status', 'Evaluated')}</span></td>
    </tr>
    """

st.markdown(
    f"""
    <div class="saas-card">
        <table style="width: 100%; border-collapse: collapse; color: #cbd5e1; font-size: 0.88rem; text-align: left;">
            <thead>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #ffffff;">
                    <th style="padding: 12px;">Algorithm</th>
                    <th style="padding: 12px;">Accuracy</th>
                    <th style="padding: 12px;">Precision</th>
                    <th style="padding: 12px;">Recall</th>
                    <th style="padding: 12px;">F1-Score</th>
                    <th style="padding: 12px;">ROC-AUC</th>
                    <th style="padding: 12px;">Status</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
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
    st.markdown(
        f"""
        <div class="saas-card">
            <h4 style="color: #ffffff; font-weight: 700; margin-top:0; display:flex; align-items:center; gap:8px;">
                {icon('arrow-up-right', size=16, colour='#38bdf8')} Future Enhancements Roadmap
            </h4>
            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; color: #cbd5e1;">
                <div>• Real-time REST API integration with Workday &amp; SAP SuccessFactors</div>
                <div>• Automated weekly email alerts to HR managers for high-risk staff</div>
                <div>• XGBoost &amp; LightGBM model benchmarking</div>
                <div>• Role-based access control (RBAC) authentication</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c_stat:
    st.markdown(
        f"""
        <div class="saas-card">
            <h4 style="color: #ffffff; font-weight: 700; margin-top:0; display:flex; align-items:center; gap:8px;">
                {icon('bar-chart', size=16, colour='#38bdf8')} Project Statistics Summary
            </h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.82rem;">
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                    <div style="color: #94a3b8;">DATASET RECORDS</div>
                    <div style="font-size: 1.2rem; font-weight: 800; color: #ffffff;">{_stats.get('total_records', 1470):,} Employees</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                    <div style="color: #94a3b8;">PIPELINE FEATURES</div>
                    <div style="font-size: 1.2rem; font-weight: 800; color: #38bdf8;">{_stats.get('feature_count', 59)} Features</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                    <div style="color: #94a3b8;">XAI FRAMEWORK</div>
                    <div style="font-size: 1.2rem; font-weight: 800; color: #c084fc;">SHAP Active</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.5); padding: 10px; border-radius: 8px;">
                    <div style="color: #94a3b8;">AUTHOR &amp; ROLE</div>
                    <div style="font-size: 1.2rem; font-weight: 800; color: #4ade80;">Taranvir Kaur</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

render_footer()