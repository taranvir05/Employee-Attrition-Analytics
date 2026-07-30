import streamlit as st
from utils.model_loader import get_model_display_name, get_model_metadata
from utils.icons import icon


def render_sidebar():
    """
    Renders a premium enterprise sidebar with Material navigation icons,
    model status snapshot, and branded footer badges.
    """
    with st.sidebar:
        # ── Brand header ────────────────────────────────────
        st.markdown(
            f"""
            <div style="padding: 0px 0 14px 0; margin-top: 0px;
                        border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 42px; height: 42px; border-radius: 12px;
                                background: linear-gradient(135deg, #0284c7, #6366f1);
                                display: flex; align-items: center; justify-content: center;
                                box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);">
                        {icon("activity", size=20, colour="#ffffff")}
                    </div>
                    <div>
                        <h2 style="font-size: 1.2rem; font-weight: 800; margin: 0;
                                   color: #ffffff; letter-spacing: -0.02em;">
                            PulseHR <span style="color: #38bdf8;">AI</span>
                        </h2>
                        <p style="font-size: 0.76rem; color: #94a3b8; margin: 0; font-weight: 500;">
                            Attrition Intelligence Platform
                        </p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Navigation label ────────────────────────────────
        st.markdown(
            '<div style="font-size: 0.75rem; font-weight: 700; color: #64748b; '
            'text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Navigation</div>',
            unsafe_allow_html=True,
        )

        # Custom Navigation Links using Streamlit 1.59 material symbols
        st.page_link("app.py",                             label="Home",                 icon=":material/home:")
        st.page_link("pages/1_HR_Dashboard.py",            label="HR Dashboard",         icon=":material/bar_chart:")
        st.page_link("pages/2_Predict_Attrition.py",       label="Predict Attrition",    icon=":material/target:")
        st.page_link("pages/3_Model_Explainability.py",    label="Model Explainability", icon=":material/psychology:")
        st.page_link("pages/4_Business_Insights.py",       label="Business Insights",    icon=":material/trending_up:")
        st.page_link("pages/5_About_Project.py",           label="About Project",        icon=":material/description:")

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Model snapshot card ─────────────────────────────
        _meta       = get_model_metadata()
        _model_name = _meta["model_name"]
        _modified   = _meta["last_modified"]
        st.markdown(
            f"""
            <div style="padding: 14px; border-radius: 14px;
                        background: rgba(30, 41, 59, 0.5);
                        border: 1px solid rgba(255,255,255,0.07);
                        font-size: 0.8rem; margin-bottom: 16px;">
                <div style="color: #ffffff; font-weight: 700; margin-bottom: 8px;
                            display: flex; justify-content: space-between; align-items: center;">
                    <span style="display:flex;align-items:center;gap:6px;">
                        {icon("cpu", size=14, colour="#38bdf8")} Engine Specifications
                    </span>
                    <span style="color: #4ade80; font-size: 0.72rem; font-weight: 700;
                                 display:flex;align-items:center;gap:4px;">
                        {icon("check-circle", size=11, colour="#4ade80")} Online
                    </span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px;
                            color: #94a3b8; font-size: 0.78rem;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Model:</span>
                        <span style="color: #38bdf8; font-weight: 600;">{_model_name}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Explainability:</span>
                        <span style="color: #c084fc; font-weight: 600;">SHAP Enabled</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Dataset:</span>
                        <span style="color: #cbd5e1; font-weight: 600;">1,470 Records</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Updated:</span>
                        <span style="color: #64748b; font-weight: 500; font-size: 0.72rem;">{_modified}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Footer badges ───────────────────────────────────
        _badge_model = get_model_display_name()
        st.markdown(
            f"""
            <div style="padding: 14px; border-radius: 14px;
                        background: rgba(15, 23, 42, 0.7);
                        border: 1px solid rgba(56, 189, 248, 0.2);
                        font-size: 0.78rem; text-align: center;">
                <div style="font-weight: 800; color: #ffffff; font-size: 0.85rem; margin-bottom: 2px;">
                    PulseHR AI
                </div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-bottom: 10px;">
                    Attrition Intelligence Platform
                </div>
                <div style="display: flex; gap: 4px; justify-content: center; flex-wrap: wrap;">
                    <span class="badge-pill badge-cyan"    style="font-size:0.68rem;padding:2px 8px;">{_badge_model}</span>
                    <span class="badge-pill badge-purple"  style="font-size:0.68rem;padding:2px 8px;">SHAP Enabled</span>
                    <span class="badge-pill badge-success" style="font-size:0.68rem;padding:2px 8px;">v2.5</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_kpi_card(
    title,
    value,
    subtitle="",
    icon_name="bar-chart",
    badge_text="",
    badge_type="cyan",
    sparkline_bars=None,
):
    """
    Renders a glassmorphism KPI card with SVG icon and mini sparkline.
    0 emojis.
    """
    if sparkline_bars is None:
        sparkline_bars = [40, 60, 35, 80, 95, 70]

    badge_html = (
        f'<span class="badge-pill badge-{badge_type}">{badge_text}</span>'
        if badge_text else ""
    )

    bars_html = "".join([
        f'<div class="kpi-sparkline-bar {"active" if i == len(sparkline_bars) - 1 else ""}"'
        f' style="height: {h}%;"></div>'
        for i, h in enumerate(sparkline_bars)
    ])

    icon_html = (
        f'<div class="kpi-icon-wrapper">'
        f'{icon(icon_name, size=17, colour="#38bdf8")}'
        f'</div>'
    )

    html_code = f"""
    <div class="kpi-card">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            {icon_html}
            {badge_html}
        </div>
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-subtitle">{subtitle}</div>
        <div class="kpi-sparkline">
            {bars_html}
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)


def render_section_header(title, subtitle="", badge="", icon_name=""):
    """
    Renders a styled dark SaaS section header with SVG icon. Zero emojis.
    """
    badge_html    = (
        f'<span class="badge-pill badge-cyan" style="margin-bottom: 6px;">{badge}</span><br>'
        if badge else ""
    )
    subtitle_html = (
        f'<p style="color: #94a3b8; font-size: 0.9rem; margin-top: 4px; font-weight: 400;">{subtitle}</p>'
        if subtitle else ""
    )
    icon_html = ""
    if icon_name:
        icon_html = (
            f'<span style="display:inline-flex;align-items:center;vertical-align:middle;'
            f'margin-right:10px;">{icon(icon_name, size=22, colour="#38bdf8")}</span>'
        )

    st.markdown(
        f"""
        <div style="margin-top: 8px; margin-bottom: 16px;">
            {badge_html}
            <h2 style="color: #ffffff; font-size: 1.45rem; font-weight: 800; margin: 0;
                       letter-spacing: -0.02em; display:flex; align-items:center;">
                {icon_html}{title}
            </h2>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_insight_card(icon_or_name, title, text, detail_or_category="", category="warning"):
    """
    Renders a premium executive insight card with coloured left border.
    Zero emojis.
    """
    if detail_or_category in ("danger", "warning", "success", "info", "purple", ""):
        detail   = ""
        category = detail_or_category if detail_or_category else "warning"
    else:
        detail = detail_or_category

    border_colors = {
        "danger":  "#ef4444",
        "warning": "#f59e0b",
        "success": "#22c55e",
        "info":    "#38bdf8",
        "purple":  "#8b5cf6",
    }
    icon_colors = {
        "danger":  "#f87171",
        "warning": "#fbbf24",
        "success": "#4ade80",
        "info":    "#38bdf8",
        "purple":  "#c084fc",
    }
    color      = border_colors.get(category, "#38bdf8")
    icon_color = icon_colors.get(category, "#38bdf8")

    icon_html = icon(icon_or_name, size=20, colour=icon_color)

    detail_html = (
        f'<p style="color: #94a3b8; font-size: 0.82rem; margin: 6px 0 0 0; line-height: 1.5;">{detail}</p>'
        if detail else ""
    )

    st.markdown(
        f"""
        <div style="background: rgba(15, 23, 42, 0.75); border-left: 4px solid {color};
                    border-radius: 14px; padding: 18px 20px;
                    border-top: 1px solid rgba(255,255,255,0.06);
                    border-right: 1px solid rgba(255,255,255,0.06);
                    border-bottom: 1px solid rgba(255,255,255,0.06);
                    transition: border-color 0.25s ease, box-shadow 0.25s ease;
                    height: 100%; box-sizing: border-box;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                {icon_html}
                <h4 style="color: #ffffff; font-size: 1rem; font-weight: 700; margin: 0;">{title}</h4>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; margin: 0; line-height: 1.6; font-weight: 500;">{text}</p>
            {detail_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    """Renders corporate footer with SVG icons. Zero emojis."""
    st.markdown(
        f"""
        <div style="margin-top: 40px; padding-top: 20px;
                    border-top: 1px solid rgba(255,255,255,0.08);
                    text-align: center; color: #64748b; font-size: 0.8rem;">
            <div style="display: flex; justify-content: center; align-items: center;
                        gap: 16px; margin-bottom: 8px; font-weight: 600; color: #94a3b8;">
                <span style="display:flex;align-items:center;gap:6px;">
                    {icon("activity", size=14, colour="#38bdf8")} PulseHR AI
                </span>
                <span style="color:#475569;">•</span>
                <span>Predictive Attrition Intelligence</span>
                <span style="color:#475569;">•</span>
                <span style="display:flex;align-items:center;gap:6px;">
                    {icon("brain", size=14, colour="#c084fc")} SHAP XAI
                </span>
            </div>
            <p style="margin: 0;">
                Enterprise Workforce Analytics Platform | Built with Python, Streamlit &amp; Scikit-learn
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
