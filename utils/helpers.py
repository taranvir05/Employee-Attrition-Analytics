import streamlit as st

def render_sidebar():
    """
    Renders an EcoScan-inspired premium sidebar with custom navigation links,
    model metrics, and bottom badges. Ensures zero empty vertical space and zero top padding.
    """
    with st.sidebar:
        # Header Brand Logo & Title (Zero top margin/padding)
        st.markdown(
            """
            <div style="padding: 0px 0 14px 0; margin-top: 0px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="width: 42px; height: 42px; border-radius: 12px; background: linear-gradient(135deg, #0284c7, #6366f1); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);">
                        ⚡
                    </div>
                    <div>
                        <h2 style="font-size: 1.2rem; font-weight: 800; margin: 0; color: #ffffff; letter-spacing: -0.02em;">PulseHR <span style="color: #38bdf8;">AI</span></h2>
                        <p style="font-size: 0.76rem; color: #94a3b8; margin: 0; font-weight: 500;">Attrition Intelligence Platform</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Custom Navigation Menu (Replacing default stSidebarNav)
        st.markdown('<div style="font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Navigation</div>', unsafe_allow_html=True)
        
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/1_HR_Dashboard.py", label="HR Dashboard", icon="📊")
        st.page_link("pages/2_Predict_Attrition.py", label="Predict Attrition", icon="🎯")
        st.page_link("pages/3_Model_Explainability.py", label="Model Explainability", icon="🧠")
        st.page_link("pages/4_Business_Insights.py", label="Business Insights", icon="📈")
        st.page_link("pages/5_About_Project.py", label="About Project", icon="📄")

        st.markdown("<br>", unsafe_allow_html=True)

        # Model Snapshot Card in Sidebar
        st.markdown(
            """
            <div style="padding: 14px; border-radius: 14px; background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255,255,255,0.07); font-size: 0.8rem; margin-bottom: 16px;">
                <div style="color: #ffffff; font-weight: 700; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <span>🤖 Engine Specifications</span>
                    <span style="color: #4ade80; font-size: 0.72rem; font-weight: 700;">🟢 Online</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px; color: #94a3b8; font-size: 0.78rem;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Model:</span>
                        <span style="color: #38bdf8; font-weight: 600;">Random Forest</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Accuracy:</span>
                        <span style="color: #4ade80; font-weight: 700;">92.4%</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Explainability:</span>
                        <span style="color: #c084fc; font-weight: 600;">SHAP Enabled</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Dataset:</span>
                        <span style="color: #cbd5e1; font-weight: 600;">1,470 Records</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Premium Footer Badges Widget
        st.markdown(
            """
            <div style="padding: 14px; border-radius: 14px; background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); font-size: 0.78rem; text-align: center;">
                <div style="font-weight: 800; color: #ffffff; font-size: 0.85rem; margin-bottom: 2px;">PulseHR AI</div>
                <div style="color: #94a3b8; font-size: 0.72rem; margin-bottom: 10px;">Attrition Intelligence Platform</div>
                <div style="display: flex; gap: 4px; justify-content: center; flex-wrap: wrap;">
                    <span class="badge-pill badge-cyan" style="font-size: 0.68rem; padding: 2px 8px;">Random Forest</span>
                    <span class="badge-pill badge-purple" style="font-size: 0.68rem; padding: 2px 8px;">SHAP Enabled</span>
                    <span class="badge-pill badge-success" style="font-size: 0.68rem; padding: 2px 8px;">Version 2.4</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

def render_kpi_card(title, value, subtitle="", icon="📊", badge_text="", badge_type="cyan", sparkline_bars=[40, 60, 35, 80, 95, 70]):
    """
    Renders a glassmorphism KPI card with mini sparkline graphic.
    """
    badge_html = f'<span class="badge-pill badge-{badge_type}">{badge_text}</span>' if badge_text else ''
    
    # Generate HTML sparkline bars
    bars_html = "".join([
        f'<div class="kpi-sparkline-bar {"active" if i == len(sparkline_bars)-1 else ""}" style="height: {h}%;"></div>'
        for i, h in enumerate(sparkline_bars)
    ])
    
    html_code = f"""
    <div class="kpi-card">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div class="kpi-icon-wrapper">{icon}</div>
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

def render_section_header(title, subtitle="", badge=""):
    """
    Renders a styled dark SaaS section header.
    """
    badge_html = f'<span class="badge-pill badge-cyan" style="margin-bottom: 6px;">{badge}</span><br>' if badge else ''
    subtitle_html = f'<p style="color: #94a3b8; font-size: 0.9rem; margin-top: 4px; font-weight: 400;">{subtitle}</p>' if subtitle else ''
    
    st.markdown(
        f"""
        <div style="margin-top: 8px; margin-bottom: 16px;">
            {badge_html}
            <h2 style="color: #ffffff; font-size: 1.45rem; font-weight: 800; margin: 0; letter-spacing: -0.02em;">{title}</h2>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True
    )

def render_insight_card(icon, title, text, category="warning"):
    """
    Renders a single-sentence executive insight card with colored left border.
    """
    border_colors = {
        "danger": "#ef4444",
        "warning": "#f59e0b",
        "success": "#22c55e",
        "info": "#38bdf8",
        "purple": "#8b5cf6"
    }
    color = border_colors.get(category, "#38bdf8")
    
    st.markdown(
        f"""
        <div style="background: rgba(15, 23, 42, 0.75); border-left: 4px solid {color}; border-radius: 14px; padding: 18px 20px; margin-bottom: 14px; border-top: 1px solid rgba(255,255,255,0.06); border-right: 1px solid rgba(255,255,255,0.06); border-bottom: 1px solid rgba(255,255,255,0.06); transition: all 0.25s ease;" class="saas-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                <span style="font-size: 1.3rem;">{icon}</span>
                <h4 style="color: #ffffff; font-size: 1.05rem; font-weight: 700; margin: 0;">{title}</h4>
            </div>
            <p style="color: #cbd5e1; font-size: 0.88rem; margin: 0; line-height: 1.5; font-weight: 500;">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """
    Renders corporate footer.
    """
    st.markdown(
        """
        <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; color: #64748b; font-size: 0.8rem;">
            <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 8px; font-weight: 600; color: #94a3b8;">
                <span>PulseHR AI</span> • <span>Predictive Attrition Intelligence</span> • <span>SHAP XAI</span>
            </div>
            <p style="margin: 0;">Enterprise Workforce Analytics Platform | Built with Python, Streamlit & Scikit-learn</p>
        </div>
        """,
        unsafe_allow_html=True
    )
