import streamlit as st

def load_css():
    """
    Injects custom Enterprise SaaS Dark Theme CSS styling into Streamlit.
    Inspired by Stripe, Linear, EcoScan, Vercel, and Power BI dashboards.
    Hides all Streamlit default branding elements and removes top sidebar spacing.
    """
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        /* Global Font and Background */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            background-color: #0b0f19 !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(99, 102, 241, 0.08) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(139, 92, 246, 0.06) 0px, transparent 50%) !important;
            color: #f1f5f9 !important;
        }

        /* Completely Hide Streamlit default branding & navigation */
        #MainMenu {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        header[data-testid="stHeader"] {display: none !important;}
        .stDeployButton {display: none !important;}
        [data-testid="stSidebarNav"] {display: none !important;}
        
        /* Main Container Padding */
        .block-container {
            padding-top: 1.2rem !important;
            padding-bottom: 2.5rem !important;
            max-width: 1380px !important;
        }

        /* --- SIDEBAR TOP SPACING RESET --- */
        section[data-testid="stSidebar"] {
            background-color: rgba(15, 23, 42, 0.95) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(16px);
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        /* Hide header/collapse button container completely */
        [data-testid="stSidebarHeader"],
        [data-testid="stSidebarCollapseButton"],
        header[data-testid="stHeader"] {
            display: none !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Remove top padding & margins from all inner sidebar wrappers */
        [data-testid="stSidebarContent"],
        section[data-testid="stSidebar"] > div,
        section[data-testid="stSidebar"] > div > div {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        /* Target sidebar user content container and first child elements */
        [data-testid="stSidebarUserContent"] {
            padding-top: 10px !important;
            padding-bottom: 1rem !important;
            margin-top: 0 !important;
        }

        [data-testid="stSidebarUserContent"] > div,
        [data-testid="stSidebarUserContent"] [data-testid="stVerticalBlock"],
        [data-testid="stSidebarUserContent"] [data-testid="stVerticalBlock"] > div:first-child,
        [data-testid="stSidebarUserContent"] [data-testid="stElementContainer"]:first-child,
        [data-testid="stSidebarUserContent"] [data-testid="stMarkdownContainer"]:first-child {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #94a3b8;
            font-size: 0.88rem;
        }

        /* Custom st.page_link Navigation Buttons styling in Sidebar */
        div[data-testid="stSidebar"] div.stPageLink > a {
            background: rgba(30, 41, 59, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            border-radius: 12px !important;
            padding: 10px 14px !important;
            margin-bottom: 6px !important;
            color: #cbd5e1 !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            transition: all 0.25s ease-in-out !important;
        }
        div[data-testid="stSidebar"] div.stPageLink > a:hover {
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.15) 0%, rgba(59, 130, 246, 0.15) 100%) !important;
            border-color: rgba(56, 189, 248, 0.4) !important;
            color: #38bdf8 !important;
            transform: translateX(4px) !important;
            box-shadow: 0 4px 12px rgba(56, 189, 248, 0.15) !important;
        }
        div[data-testid="stSidebar"] div.stPageLink > a[aria-current="page"] {
            background: linear-gradient(135deg, rgba(14, 165, 233, 0.25) 0%, rgba(59, 130, 246, 0.25) 100%) !important;
            border: 1px solid rgba(56, 189, 248, 0.5) !important;
            color: #38bdf8 !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 14px rgba(56, 189, 248, 0.2) !important;
        }

        /* Card Container Base Styling */
        .saas-card {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.09);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(12px);
            transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.25s cubic-bezier(0.4,0,0.2,1);
            position: relative;
            overflow: hidden;
        }
        .saas-card:hover {
            border-color: rgba(56, 189, 248, 0.3);
            box-shadow: 0 0 0 1px rgba(56,189,248,0.08), 0 16px 40px -12px rgba(14, 165, 233, 0.25);
            transform: translateY(-2px);
        }
        /* Equal-height insight card columns — wrap both cards in a flex row */
        .insight-row {
            display: flex;
            gap: 18px;
            align-items: stretch;
        }
        .insight-row .saas-card {
            flex: 1;
            margin-bottom: 0;
            display: flex;
            flex-direction: column;
        }
        .insight-row .saas-card p {
            flex: 1;
        }
        /* Recommendation bullet list */
        .rec-bullets {
            list-style: none;
            padding: 0;
            margin: 8px 0 0 0;
            display: flex;
            flex-direction: column;
            gap: 7px;
        }
        .rec-bullets li {
            display: flex;
            align-items: flex-start;
            gap: 9px;
            font-size: 0.86rem;
            color: #cbd5e1;
            line-height: 1.5;
        }
        .rec-bullets li::before {
            content: '';
            display: block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #38bdf8;
            margin-top: 6px;
            flex-shrink: 0;
        }

        /* Automatic SaaS Card Styling for Plotly Charts */
        [data-testid="stPlotlyChart"] {
            background: rgba(15, 23, 42, 0.75) !important;
            border: 1px solid rgba(255, 255, 255, 0.09) !important;
            border-radius: 16px !important;
            padding: 12px !important;
            margin-bottom: 12px !important;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5) !important;
            backdrop-filter: blur(12px) !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        [data-testid="stPlotlyChart"]:hover {
            border-color: rgba(56, 189, 248, 0.35) !important;
            box-shadow: 0 14px 35px -10px rgba(14, 165, 233, 0.2) !important;
        }

        /* KPI Cards */
        .kpi-card {
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.85) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 14px 14px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            position: relative;
        }
        .kpi-card:hover {
            border-color: rgba(56, 189, 248, 0.45);
            transform: translateY(-4px);
            box-shadow: 0 12px 28px rgba(14, 165, 233, 0.25);
        }
        .kpi-icon-wrapper {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
            margin-bottom: 8px;
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.25);
        }
        .kpi-title {
            color: #94a3b8;
            font-size: 0.74rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .kpi-value {
            color: #ffffff;
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.2;
            word-break: break-word;
            overflow-wrap: break-word;
        }
        .kpi-subtitle {
            font-size: 0.72rem;
            margin-top: 4px;
            color: #38bdf8;
            font-weight: 500;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* Mini sparkline bar graphic for KPI cards */
        .kpi-sparkline {
            display: flex;
            align-items: flex-end;
            gap: 3px;
            height: 16px;
            margin-top: 8px;
        }
        .kpi-sparkline-bar {
            flex: 1;
            background: rgba(56, 189, 248, 0.4);
            border-radius: 2px;
            transition: all 0.2s ease;
        }
        .kpi-sparkline-bar.active {
            background: #38bdf8;
            box-shadow: 0 0 6px rgba(56, 189, 248, 0.8);
        }

        /* Buttons — Premium gradient with micro-interaction */
        div.stButton > button {
            background: linear-gradient(135deg, #0369a1 0%, #1d4ed8 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: 1px solid rgba(56, 189, 248, 0.25) !important;
            padding: 12px 24px !important;
            font-size: 0.92rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.01em !important;
            box-shadow: 0 4px 18px rgba(2, 132, 199, 0.35), inset 0 1px 0 rgba(255,255,255,0.1) !important;
            transition: background 0.2s ease, box-shadow 0.2s ease, transform 0.15s ease !important;
            width: 100% !important;
        }
        div.stButton > button:hover {
            background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%) !important;
            box-shadow: 0 8px 28px rgba(56, 189, 248, 0.5), inset 0 1px 0 rgba(255,255,255,0.15) !important;
            transform: translateY(-2px) !important;
            border-color: rgba(56, 189, 248, 0.5) !important;
        }
        div.stButton > button:active {
            transform: translateY(0px) !important;
            box-shadow: 0 2px 8px rgba(2, 132, 199, 0.3) !important;
        }
        /* Download button — teal accent variant */
        div.stDownloadButton > button {
            background: linear-gradient(135deg, rgba(15,23,42,0.9) 0%, rgba(30,41,59,0.9) 100%) !important;
            color: #38bdf8 !important;
            border-radius: 12px !important;
            border: 1px solid rgba(56, 189, 248, 0.4) !important;
            padding: 11px 22px !important;
            font-size: 0.88rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.01em !important;
            box-shadow: 0 4px 14px rgba(56, 189, 248, 0.15), inset 0 1px 0 rgba(255,255,255,0.05) !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
        }
        div.stDownloadButton > button:hover {
            background: linear-gradient(135deg, rgba(56,189,248,0.12) 0%, rgba(99,102,241,0.12) 100%) !important;
            border-color: rgba(56, 189, 248, 0.7) !important;
            box-shadow: 0 6px 22px rgba(56, 189, 248, 0.3) !important;
            transform: translateY(-2px) !important;
            color: #7dd3fc !important;
        }
        div.stDownloadButton > button:active {
            transform: translateY(0px) !important;
        }

        /* Form Controls Styling */
        .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
            color: #cbd5e1 !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            margin-bottom: 4px !important;
        }
        div[data-baseweb="select"] > div {
            background-color: rgba(30, 41, 59, 0.7) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 10px !important;
            color: #ffffff !important;
        }

        /* Badges & Status Pills */
        .badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            border-radius: 9999px;
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            text-transform: uppercase;
            white-space: nowrap;
        }
        .badge-cyan {
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
        .badge-purple {
            background: rgba(168, 85, 247, 0.15);
            color: #c084fc;
            border: 1px solid rgba(168, 85, 247, 0.3);
        }
        .badge-danger {
            background: rgba(239, 68, 68, 0.15);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        .badge-success {
            background: rgba(34, 197, 94, 0.15);
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }
        .badge-warning {
            background: rgba(245, 158, 11, 0.15);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        /* Gradient Text */
        .gradient-text {
            background: linear-gradient(135deg, #ffffff 0%, #38bdf8 50%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* Clean Subtle Divider */
        .glow-divider {
            height: 1px;
            width: 100%;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            margin: 16px 0;
        }

        /* ── Suppress empty <br> spacer containers ─────────────
           Streamlit wraps every st.markdown() call in a stMarkdownContainer
           div. When the only content is a <br> tag the div renders as a
           visible blank bar.  We detect those containers and collapse them.  */
        [data-testid="stMarkdownContainer"]:has(> br:only-child) {
            display: none !important;
            margin: 0 !important;
            padding: 0 !important;
            height: 0 !important;
            min-height: 0 !important;
        }
        /* Collapse the wrapping stElementContainer */
        [data-testid="stElementContainer"]:has(
            [data-testid="stMarkdownContainer"] > br:only-child
        ) {
            display: none !important;
            margin: 0 !important;
            padding: 0 !important;
            height: 0 !important;
            min-height: 0 !important;
        }
        /* Collapse the outer vertical block wrapper */
        [data-testid="stVerticalBlockBorderWrapper"]:has(
            [data-testid="stMarkdownContainer"] > br:only-child
        ) {
            display: none !important;
            margin: 0 !important;
            padding: 0 !important;
            height: 0 !important;
            min-height: 0 !important;
        }
        /* Utility: section gap replacement instead of <br> */
        .section-gap { margin-top: 20px; }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 7px;
            height: 7px;
        }
        ::-webkit-scrollbar-track {
            background: #0b0f19;
        }
        ::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )