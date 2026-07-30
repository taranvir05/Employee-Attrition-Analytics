"""
utils/pdf_report.py
-------------------
Generates a executive-grade downloadable PDF prediction report for PulseHR AI.
Designed to mirror enterprise reports from Power BI, Deloitte, SAP SuccessFactors & Workday.
Uses fpdf2 — 100% latin-1 safe typography and corporate styling.
"""

import io
import datetime
import random
from fpdf import FPDF, XPos, YPos


# ── Corporate Color Palette (RGB) ────────────────────────────
NAVY       = (15, 23, 42)        # #0F172A - Primary Header & Dark Cards
ROYAL_BLUE = (29, 78, 216)       # #1D4ED8 - Brand Primary
CYAN       = (14, 165, 233)      # #0EA5E9 - Accent
DARK_TEXT  = (30, 41, 59)        # #1E293B - Body Text
MUTED_TEXT = (100, 116, 139)     # #64748B - Subtitles & Labels
LIGHT_BG   = (248, 250, 252)     # #F8FAFC - Card Background
ALT_ROW    = (241, 245, 249)     # #F1F5F9 - Table Alternate Rows
BORDER     = (226, 232, 240)     # #E2E8F0 - Divider & Table Borders
WHITE      = (255, 255, 255)

# Risk Status Palette
RISK_RED   = (220, 38, 38)       # #DC2626
RISK_BG    = (254, 242, 242)     # #FEF2F2
SAFE_GREEN = (22, 163, 74)       # #16A34A
SAFE_BG    = (240, 253, 244)     # #F0FDF4
AMBER      = (217, 119, 6)       # #D97706


class _CorporatePDF(FPDF):
    """Subclass of FPDF for corporate PDF generation with strict margins & placement."""

    def __init__(self):
        super().__init__()
        self.set_margins(16, 16, 16)
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        # Header Top Bar
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 22, style="F")

        # Top Accent Stripe
        self.set_fill_color(*CYAN)
        self.rect(0, 0, 210, 2, style="F")

        # Brand Badge Block
        self.set_fill_color(*ROYAL_BLUE)
        self.rect(16, 5, 12, 12, style="F")
        self.set_fill_color(*CYAN)
        self.rect(19, 8, 12, 12, style="F")

        # Brand Title
        self.set_xy(34, 6)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*WHITE)
        self.cell(50, 6, "PulseHR AI", ln=False)

        self.set_xy(34, 13)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*CYAN)
        self.cell(80, 4, "Enterprise Workforce Analytics Platform")

        # Header Right Subtitle
        self.set_xy(120, 8)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*WHITE)
        self.cell(74, 5, "EXECUTIVE PREDICTION REPORT", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_x(16)
        self.ln(12)

    def footer(self):
        self.set_y(-14)
        self.set_draw_color(*BORDER)
        self.set_line_width(0.3)
        self.line(16, self.get_y(), 194, self.get_y())
        self.ln(2)

        self.set_font("Helvetica", "", 7.5)
        self.set_text_color(*MUTED_TEXT)
        self.cell(60, 5, "CONFIDENTIAL  |  PulseHR AI Platform", ln=False)
        self.cell(70, 5, "Internal HR Analytics Decision Support", align="C", ln=False)
        now_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.cell(48, 5, f"Generated: {now_date}", align="R")

    # ── Layout Helper Methods ───────────────────────────────

    def section_header(self, title: str, accent_color=ROYAL_BLUE):
        """Renders a clean corporate section header with a colored left bar."""
        self.set_x(self.l_margin)
        self.set_fill_color(*accent_color)
        self.rect(self.get_x(), self.get_y() + 1, 3.5, 6.5, style="F")

        self.set_xy(self.get_x() + 6, self.get_y())
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*NAVY)
        self.cell(0, 8, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_draw_color(*BORDER)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(self.l_margin, y, 210 - self.r_margin, y)
        self.set_x(self.l_margin)
        self.ln(3)

    def bullet_item(self, text: str):
        """Renders a bulleted recommendation item with crisp spacing."""
        self.set_x(self.l_margin + 2)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*ROYAL_BLUE)
        self.cell(5, 5.5, "-", ln=False)

        self.set_font("Helvetica", "", 9)
        self.set_text_color(*DARK_TEXT)
        self.multi_cell(0, 5.5, text)
        self.set_x(self.l_margin)
        self.ln(1)


# ─────────────────────────────────────────────────────────────
# Public Generator Function
# ─────────────────────────────────────────────────────────────

def generate_prediction_pdf(
    department: str,
    job_role: str,
    age: int,
    gender: str,
    monthly_income: int,
    overtime: str,
    job_satisfaction: int,
    marital_status: str,
    prediction: int,
    probability: float,
    confidence: float,
    top_risk_features: list,      # list of (feature_name, contribution_value)
    top_retention_features: list,
    model_name: str = "Logistic Regression",
    rec_title: str = "",
    rec_bullets: list = None,
) -> bytes:
    """
    Generate a corporate downloadable PDF executive report.
    Returns raw PDF bytes.
    """
    if rec_bullets is None:
        rec_bullets = []

    is_high_risk  = (prediction == 1)
    risk_label    = "HIGH ATTRITION RISK" if is_high_risk else "LOW ATTRITION RISK"
    status_bg     = RISK_BG if is_high_risk else SAFE_BG
    status_fg     = RISK_RED if is_high_risk else SAFE_GREEN
    prob_pct      = f"{probability * 100:.1f}%"
    conf_pct      = f"{confidence * 100:.1f}%"
    now_str       = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    report_id     = f"PHR-{datetime.datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"

    pdf = _CorporatePDF()
    pdf.add_page()

    # ── METADATA BAR ──────────────────────────────────────────
    pdf.set_fill_color(*LIGHT_BG)
    pdf.rect(16, pdf.get_y(), 178, 10, style="F")
    pdf.set_draw_color(*BORDER)
    pdf.rect(16, pdf.get_y(), 178, 10, style="D")

    pdf.set_xy(19, pdf.get_y() + 2.5)
    pdf.set_font("Helvetica", "B", 7.5)
    pdf.set_text_color(*MUTED_TEXT)
    pdf.cell(45, 5, f"REPORT ID: {report_id}", ln=False)
    pdf.cell(45, 5, f"GENERATED: {now_str}", ln=False)
    pdf.cell(45, 5, f"MODEL: {model_name.upper()}", ln=False)
    pdf.cell(43, 5, f"DEPT: {department.upper()}", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.ln(5)

    # ── EXECUTIVE SUMMARY SECTION ─────────────────────────────
    pdf.section_header("1. Executive Summary", accent_color=ROYAL_BLUE)

    # Risk Summary Hero Box
    box_y = pdf.get_y()
    pdf.set_fill_color(*status_bg)
    pdf.rect(16, box_y, 178, 22, style="F")
    pdf.set_draw_color(*status_fg)
    pdf.set_line_width(0.8)
    pdf.rect(16, box_y, 178, 22, style="D")

    pdf.set_xy(22, box_y + 3.5)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(*status_fg)
    pdf.cell(100, 6, risk_label, ln=False)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(66, 6, f"Departure Probability: {prob_pct}", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_xy(22, box_y + 11.5)
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(*DARK_TEXT)
    summary_text = (
        f"Employee profile evaluated for role of {job_role} in {department}. "
        f"Model Confidence: {conf_pct}."
    )
    pdf.cell(166, 5, summary_text)

    pdf.set_x(16)
    pdf.set_y(box_y + 26)

    # Structured Executive Breakdown Box
    pdf.set_fill_color(*LIGHT_BG)
    pdf.rect(16, pdf.get_y(), 178, 38, style="F")
    pdf.set_draw_color(*BORDER)
    pdf.set_line_width(0.3)
    pdf.rect(16, pdf.get_y(), 178, 38, style="D")

    start_y = pdf.get_y() + 3
    pdf.set_xy(20, start_y)

    items = [
        ("Employee Risk Classification", risk_label, status_fg),
        ("Risk Probability & Confidence", f"{prob_pct}  (Model Confidence: {conf_pct})", DARK_TEXT),
        ("Primary Risk Factors", ", ".join([f[0].replace("_", " ").title() for f in top_risk_features[:2]]) if top_risk_features else "None", DARK_TEXT),
        ("Recommended Action", rec_title if rec_title else "Standard HR Monitoring & Development", ROYAL_BLUE),
        ("Business Conclusion", "Immediate proactive retention intervention recommended to mitigate flight risk." if is_high_risk else "Employee displays strong retention stability; standard engagement posture recommended.", DARK_TEXT),
    ]

    for label, val, color in items:
        pdf.set_x(20)
        pdf.set_font("Helvetica", "B", 8)
        pdf.set_text_color(*MUTED_TEXT)
        pdf.cell(50, 6, f"{label}:", ln=False)

        pdf.set_font("Helvetica", "B" if color != DARK_TEXT else "", 8)
        pdf.set_text_color(*color)
        pdf.cell(120, 6, str(val), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.set_y(start_y + 38)
    pdf.ln(4)

    # ── EMPLOYEE PROFILE SECTION ──────────────────────────────
    pdf.section_header("2. Employee Profile & Parameters", accent_color=ROYAL_BLUE)

    # Profile Grid Table
    col_w = 42
    profile_data = [
        [("Department", department), ("Job Role", job_role), ("Age / Gender", f"{age} yrs / {gender}")],
        [("Monthly Income", f"${monthly_income:,}"), ("OverTime Work", overtime), ("Marital Status", marital_status)],
        [("Job Satisfaction", f"{job_satisfaction} / 4"), ("Work-Life Balance", "3 / 4"), ("Model Used", model_name)],
    ]

    for row in profile_data:
        pdf.set_x(16)
        for label, val in row:
            pdf.set_fill_color(*LIGHT_BG)
            pdf.rect(pdf.get_x(), pdf.get_y(), 57, 10, style="F")
            pdf.set_draw_color(*BORDER)
            pdf.rect(pdf.get_x(), pdf.get_y(), 57, 10, style="D")

            pdf.set_font("Helvetica", "", 7.5)
            pdf.set_text_color(*MUTED_TEXT)
            pdf.cell(24, 10, f" {label}:", ln=False)

            pdf.set_font("Helvetica", "B", 8)
            pdf.set_text_color(*DARK_TEXT)
            pdf.cell(33, 10, f"{val}", new_x=XPos.RIGHT, new_y=YPos.TOP)

        pdf.ln(11)

    pdf.set_x(16)
    pdf.ln(2)

    # ── TOP FEATURE DRIVERS TABLES SECTION ────────────────────
    pdf.section_header("3. Key Risk Driver Decomposition", accent_color=ROYAL_BLUE)

    # Table 1: Top Attrition-Increasing Factors
    pdf.set_x(16)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(*RISK_RED)
    pdf.cell(0, 5, "TOP POSITIVE CONTRIBUTORS (INCREASES ATTRITION RISK)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Table Header
    pdf.set_x(16)
    pdf.set_fill_color(*NAVY)
    pdf.rect(16, pdf.get_y(), 178, 6, style="F")

    pdf.set_font("Helvetica", "B", 7.5)
    pdf.set_text_color(*WHITE)
    pdf.cell(15, 6, " RANK", ln=False)
    pdf.cell(75, 6, "FEATURE NAME", ln=False)
    pdf.cell(50, 6, "IMPACT DIRECTION", ln=False)
    pdf.cell(38, 6, "LOG-ODDS VALUE", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    for i, (feat, val) in enumerate(top_risk_features[:4], 1):
        pdf.set_x(16)
        bg = ALT_ROW if i % 2 == 1 else WHITE
        pdf.set_fill_color(*bg)
        pdf.rect(16, pdf.get_y(), 178, 6, style="F")
        pdf.set_draw_color(*BORDER)
        pdf.rect(16, pdf.get_y(), 178, 6, style="D")

        feat_clean = feat.replace("_", " ").title()
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK_TEXT)
        pdf.cell(15, 6, f"  #{i}", ln=False)
        pdf.cell(75, 6, f" {feat_clean}", ln=False)
        pdf.set_text_color(*RISK_RED)
        pdf.cell(50, 6, " Increases Attrition Risk", ln=False)
        pdf.set_font("Helvetica", "B", 8)
        pdf.cell(38, 6, f"+{val:.3f} log-odds  ", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.ln(3)

    # Table 2: Top Retention-Supporting Factors
    pdf.set_x(16)
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(*SAFE_GREEN)
    pdf.cell(0, 5, "TOP NEGATIVE CONTRIBUTORS (SUPPORTS RETENTION)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Table Header
    pdf.set_x(16)
    pdf.set_fill_color(*NAVY)
    pdf.rect(16, pdf.get_y(), 178, 6, style="F")

    pdf.set_font("Helvetica", "B", 7.5)
    pdf.set_text_color(*WHITE)
    pdf.cell(15, 6, " RANK", ln=False)
    pdf.cell(75, 6, "FEATURE NAME", ln=False)
    pdf.cell(50, 6, "IMPACT DIRECTION", ln=False)
    pdf.cell(38, 6, "LOG-ODDS VALUE", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    for i, (feat, val) in enumerate(top_retention_features[:3], 1):
        pdf.set_x(16)
        bg = ALT_ROW if i % 2 == 1 else WHITE
        pdf.set_fill_color(*bg)
        pdf.rect(16, pdf.get_y(), 178, 6, style="F")
        pdf.set_draw_color(*BORDER)
        pdf.rect(16, pdf.get_y(), 178, 6, style="D")

        feat_clean = feat.replace("_", " ").title()
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*DARK_TEXT)
        pdf.cell(15, 6, f"  #{i}", ln=False)
        pdf.cell(75, 6, f" {feat_clean}", ln=False)
        pdf.set_text_color(*SAFE_GREEN)
        pdf.cell(50, 6, " Supports Retention", ln=False)
        pdf.set_font("Helvetica", "B", 8)
        pdf.cell(38, 6, f"{val:.3f} log-odds  ", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.ln(5)

    # ── RECOMMENDED HR ACTION PLAN SECTION ────────────────────
    pdf.section_header("4. Strategic HR Action Plan", accent_color=ROYAL_BLUE)

    # Strategy Title Header
    plan_title = rec_title if rec_title else ("Immediate HR Retention Plan Required" if is_high_risk else "Standard Retention & Development Plan")
    pdf.set_x(16)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*(RISK_RED if is_high_risk else ROYAL_BLUE))
    pdf.cell(0, 6, plan_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_x(16)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 6, "Recommended Actions", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    if rec_bullets:
        for point in rec_bullets:
            pdf.bullet_item(point.strip())
    else:
        pdf.bullet_item("Maintain regular one-to-one management check-ins")
        pdf.bullet_item("Offer quarterly learning and professional development opportunities")
        pdf.bullet_item("Recognise employee performance through structured reviews")
        pdf.bullet_item("Review and clarify career progression timelines")
        pdf.bullet_item("Monitor work-life balance and overtime hours")

    # ── Render to Bytes ───────────────────────────────────────
    pdf_bytes = pdf.output()
    return bytes(pdf_bytes)
