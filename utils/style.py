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

        /* Remove ALL Top Padding and Space above Left Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(15, 23, 42, 0.95) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(16px);
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }
        [data-testid="stSidebarContent"] {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }
        [data-testid="stSidebarUserContent"] {
            padding-top: 0.5rem !important;
            padding-bottom: 1rem !important;
            margin-top: 0rem !important;
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
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
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        .saas-card:hover {
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 14px 35px -10px rgba(14, 165, 233, 0.2);
            transform: translateY(-2px);
        }

        /* KPI Cards */
        .kpi-card {
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.85) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 18px 20px;
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
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            margin-bottom: 10px;
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.25);
        }
        .kpi-title {
            color: #94a3b8;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 4px;
        }
        .kpi-value {
            color: #ffffff;
            font-size: 1.75rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }
        .kpi-subtitle {
            font-size: 0.75rem;
            margin-top: 4px;
            color: #38bdf8;
            font-weight: 500;
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

        /* Buttons Custom Styling */
        div.stButton > button {
            background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
            color: #ffffff !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            padding: 12px 22px !important;
            font-size: 0.92rem !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.35) !important;
            transition: all 0.25s ease-in-out !important;
            width: 100% !important;
        }
        div.stButton > button:hover {
            background: linear-gradient(135deg, #38bdf8 0%, #3b82f6 100%) !important;
            box-shadow: 0 8px 25px rgba(56, 189, 248, 0.45) !important;
            transform: translateY(-2px) !important;
            color: #ffffff !important;
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
            gap: 6px;
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            text-transform: uppercase;
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

        /* Glowing Accent Divider */
        .glow-divider {
            height: 2px;
            width: 100%;
            background: linear-gradient(90deg, rgba(56, 189, 248, 0) 0%, rgba(56, 189, 248, 0.6) 50%, rgba(139, 92, 246, 0) 100%);
            margin: 20px 0;
        }

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