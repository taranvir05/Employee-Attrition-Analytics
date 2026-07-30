import time
import streamlit as st
import pandas as pd
import numpy as np
from utils.style import load_css
from utils.helpers import render_sidebar, render_section_header, render_footer
from utils.model_loader import get_model_assets, get_model_display_name
from utils.icons import icon
from utils.pdf_report import generate_prediction_pdf
from utils.shap_utils import prettify_feature

st.set_page_config(
    page_title="Predict Attrition - PulseHR",
    page_icon=":material/target:",
    layout="wide"
)

load_css()
render_sidebar()

# Model Loading — timestamp-aware cache via model_loader
model, scaler, feature_names = get_model_assets()

render_section_header(
    "Employee Attrition Prediction Studio",
    "Enter employee characteristics to calculate real-time departure probability & risk evaluation",
    "PREDICTIVE ENGINE",
    icon_name="target",
)

# ==========================================
# SPLIT SCREEN LAYOUT
# ==========================================
col_form, col_result = st.columns([1.1, 1])

with col_form:
    st.markdown(
        f"""
        <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(255,255,255,0.09);
                    border-radius: 16px; padding: 16px 20px 14px 20px; margin-bottom: 16px;
                    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5); backdrop-filter: blur(12px);">
            <h3 style="color: #ffffff; font-size: 1.1rem; font-weight: 700; margin: 0;
                       display:flex; align-items:center; gap: 8px;">
                {icon("user", size=18, colour="#38bdf8")}
                Employee Data Entry Form
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(["Profile & Edu", "Job & Role", "Satisfaction", "Tenure & Pay"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            age            = st.slider("Age", 18, 60, 30)
            gender         = st.selectbox("Gender", ["Male", "Female"])
            marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        with c2:
            education       = st.selectbox("Education Level", [1, 2, 3, 4, 5], format_func=lambda x: f"Level {x}")
            education_field = st.selectbox("Education Field", [
                "Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"
            ])
            distance = st.slider("Distance From Home (miles)", 1, 30, 10)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            department       = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
            job_role         = st.selectbox("Job Role", sorted([
                "Sales Executive", "Research Scientist", "Laboratory Technician",
                "Manufacturing Director", "Healthcare Representative", "Manager",
                "Sales Representative", "Research Director", "Human Resources"
            ]))
            job_level        = st.slider("Job Level", 1, 5, 2)
            job_involvement  = st.selectbox("Job Involvement", [1, 2, 3, 4])
        with c2:
            business_travel    = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
            overtime           = st.selectbox("OverTime Work", ["No", "Yes"])
            performance_rating = st.selectbox("Performance Rating", [3, 4])

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            job_satisfaction         = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
            environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
        with c2:
            relationship_satisfaction = st.selectbox("Relationship Satisfaction (1-4)", [1, 2, 3, 4])
            work_life_balance         = st.slider("Work-Life Balance (1-4)", 1, 4, 3)

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            monthly_income     = st.number_input("Monthly Income ($)", 1000, 30000, 6500, step=500)
            stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
            percent_salary_hike = st.slider("Percent Salary Hike (%)", 10, 25, 15)
            training           = st.slider("Training Times Last Year", 0, 6, 2)
        with c2:
            total_working_years = st.slider("Total Working Years", 0, 40, 10)
            years_company       = st.slider("Years at Company", 0, 40, 5)
            num_companies_worked = st.slider("Companies Worked For", 0, 10, 2)
            years_promotion     = st.slider("Years Since Last Promotion", 0, 15, 2)
            years_current_role  = st.slider("Years in Current Role", 0, 20, 3)
            years_with_manager  = st.slider("Years with Current Manager", 0, 20, 4)

    st.markdown('<div style="margin-top: 18px;"></div>', unsafe_allow_html=True)
    predict_button = st.button("Run ML Prediction Analysis", key="btn_run_pred")

# ==========================================
# RESULT PANEL
# ==========================================
with col_result:
    # ── Top Result Header Card (Matches Form Header) ───
    st.markdown(
        f"""
        <div style="background: rgba(15,23,42,0.75); border: 1px solid rgba(56,189,248,0.25);
                    border-radius: 16px; padding: 16px 20px 14px 20px; margin-bottom: 16px;
                    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5); backdrop-filter: blur(12px);">
            <h3 style="color: #ffffff; font-size: 1.1rem; font-weight: 700; margin: 0;
                       display:flex; align-items:center; justify-content:space-between;">
                <span style="display:flex; align-items:center; gap: 8px;">
                    {icon("target", size=18, colour="#38bdf8")}
                    Predicted Attrition Analysis Result
                </span>
                <span class="badge-pill badge-cyan" style="font-size: 0.72rem; padding: 3px 8px;">
                    Live ML Output
                </span>
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not predict_button:
        _pred_model_name = get_model_display_name()
        st.markdown(
            f"""
            <div class="saas-card" style="text-align: center; padding: 50px 20px;
                                          border: 2px dashed rgba(56, 189, 248, 0.2);">
                <div style="display:flex;justify-content:center;margin-bottom:16px;opacity:0.7;">
                    {icon("brain", size=48, colour="#38bdf8")}
                </div>
                <h3 style="color: #ffffff; font-size: 1.2rem; font-weight: 700; margin-bottom: 8px;">
                    Awaiting Input Parameters
                </h3>
                <p style="color: #94a3b8; font-size: 0.88rem; max-width: 340px; margin: 0 auto 20px auto;">
                    Adjust the employee profile on the left and click
                    <b>Run ML Prediction Analysis</b> to generate a risk assessment.
                </p>
                <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;">
                    <span class="badge-pill badge-cyan">{_pred_model_name}</span>
                    <span class="badge-pill badge-purple">SHAP Factor Analysis</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        # ── Staged loading spinner ────────────────────────────
        spinner_placeholder = st.empty()
        stages = [
            ("Analysing employee profile...",          0.4),
            ("Running ML prediction model...",         0.6),
            ("Computing feature contributions...",     0.8),
            ("Generating executive report...",         1.0),
        ]
        for stage_label, _ in stages:
            with spinner_placeholder.container():
                st.markdown(
                    f"""
                    <div style="display:flex;align-items:center;gap:12px;
                                padding:14px 18px;border-radius:12px;
                                background:rgba(30,41,59,0.6);
                                border:1px solid rgba(56,189,248,0.2);
                                margin-bottom:12px;">
                        <div style="width:18px;height:18px;border-radius:50%;
                                    border:2px solid rgba(56,189,248,0.25);
                                    border-top-color:#38bdf8;
                                    animation:spin 0.8s linear infinite;
                                    flex-shrink:0;">
                        </div>
                        <span style="color:#94a3b8;font-size:0.88rem;">{stage_label}</span>
                    </div>
                    <style>
                        @keyframes spin {{
                            to {{ transform: rotate(360deg); }}
                        }}
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                time.sleep(0.35)

        spinner_placeholder.empty()

        # ==========================================
        # PREPROCESSING & PREDICTION
        # ==========================================
        input_df = pd.DataFrame({
            "Age": [age], "DailyRate": [802], "HourlyRate": [66], "MonthlyRate": [14235],
            "Gender": [gender], "MaritalStatus": [marital_status],
            "Education": [education], "EducationField": [education_field],
            "Department": [department], "JobRole": [job_role],
            "JobLevel": [job_level], "JobInvolvement": [job_involvement],
            "BusinessTravel": [business_travel], "OverTime": [overtime],
            "PerformanceRating": [performance_rating],
            "JobSatisfaction": [job_satisfaction],
            "EnvironmentSatisfaction": [environment_satisfaction],
            "RelationshipSatisfaction": [relationship_satisfaction],
            "WorkLifeBalance": [work_life_balance],
            "MonthlyIncome": [monthly_income],
            "StockOptionLevel": [stock_option_level],
            "PercentSalaryHike": [percent_salary_hike],
            "TrainingTimesLastYear": [training],
            "TotalWorkingYears": [total_working_years],
            "YearsAtCompany": [years_company],
            "NumCompaniesWorked": [num_companies_worked],
            "YearsSinceLastPromotion": [years_promotion],
            "YearsInCurrentRole": [years_current_role],
            "YearsWithCurrManager": [years_with_manager],
            "DistanceFromHome": [distance],
        })

        input_df["IncomeGroup"] = pd.cut(
            input_df["MonthlyIncome"],
            bins=[1009, 2911, 4919, 8379, 19999],
            labels=["Low", "Medium", "High", "Very High"],
            include_lowest=True,
        )
        input_df["ExperienceGroup"] = pd.cut(
            input_df["TotalWorkingYears"],
            bins=[-1, 5, 10, 20, 40],
            labels=["Early Career", "Mid Career", "Senior", "Highly Experienced"],
        )
        input_df["PromotionDelay"] = pd.cut(
            input_df["YearsSinceLastPromotion"],
            bins=[-1, 1, 3, 6, 20],
            labels=["Recently Promoted", "Moderate Delay", "Long Delay", "Very Long Delay"],
        )
        input_df["DistanceCategory"] = pd.cut(
            input_df["DistanceFromHome"],
            bins=[-1, 5, 15, 30],
            labels=["Near", "Moderate", "Far"],
        )
        input_df["OverallSatisfaction"] = (
            input_df["EnvironmentSatisfaction"]
            + input_df["JobSatisfaction"]
            + input_df["RelationshipSatisfaction"]
            + input_df["WorkLifeBalance"]
        )
        input_df["TenureGroup"] = pd.cut(
            input_df["YearsAtCompany"],
            bins=[-1, 2, 5, 10, 40],
            labels=["New", "Junior", "Experienced", "Veteran"],
        )

        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

        numerical_columns = [
            "Age", "DailyRate", "DistanceFromHome", "Education", "EnvironmentSatisfaction",
            "HourlyRate", "JobInvolvement", "JobLevel", "JobSatisfaction", "MonthlyIncome",
            "MonthlyRate", "NumCompaniesWorked", "PercentSalaryHike", "PerformanceRating",
            "RelationshipSatisfaction", "StockOptionLevel", "TotalWorkingYears",
            "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany", "YearsInCurrentRole",
            "YearsSinceLastPromotion", "YearsWithCurrManager", "OverallSatisfaction",
        ]

        input_scaled = input_encoded.copy()
        input_scaled[numerical_columns] = scaler.transform(input_scaled[numerical_columns])

        prediction  = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        confidence  = max(probability, 1 - probability)

        # Feature contributions from log-odds coefficients
        contributions = input_scaled.values[0] * model.coef_[0]
        contrib_df = pd.DataFrame({
            "Feature":     feature_names,
            "Contribution": contributions,
            "AbsContrib":  np.abs(contributions),
        }).sort_values(by="AbsContrib", ascending=False)

        top_risk_drivers      = contrib_df[contrib_df["Contribution"] > 0].head(4)
        top_retention_drivers = contrib_df[contrib_df["Contribution"] < 0].head(3)

        # ==========================================
        # PREDICTION RESULT CARD
        # ==========================================
        is_high_risk  = prediction == 1
        status_color  = "#ef4444" if is_high_risk else "#22c55e"
        badge_icon    = icon("alert-triangle", size=13, colour="#f87171") if is_high_risk else icon("shield-check", size=13, colour="#4ade80")
        badge_type    = "danger" if is_high_risk else "success"
        result_label  = "HIGH ATTRITION RISK" if is_high_risk else "LOW ATTRITION RISK"

        st.markdown(
            f"""
            <div style="background: rgba(15,23,42,0.75); border: 1px solid {status_color};
                        border-radius: 16px; padding: 20px; margin-bottom: 16px;
                        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                    <span class="badge-pill badge-{badge_type}"
                          style="font-size: 0.82rem; padding: 5px 12px; gap: 6px;">
                        {badge_icon} {result_label}
                    </span>
                    <span style="color: #94a3b8; font-size: 0.8rem; font-weight: 600;">
                        Confidence: {confidence*100:.1f}%
                    </span>
                </div>
                <div style="text-align: center; margin: 12px 0 18px 0;">
                    <div style="font-size: 0.78rem; color: #94a3b8; font-weight: 700;
                                 text-transform: uppercase; letter-spacing: 0.06em;">
                        Estimated Attrition Probability
                    </div>
                    <div style="font-size: 3.2rem; font-weight: 800; color: {status_color};
                                 letter-spacing: -0.03em; margin: 4px 0;">
                        {probability*100:.1f}%
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(float(probability))

        # ── Top Feature Drivers ───────────────────────────────
        risk_rows = ""
        for _, r in top_risk_drivers.iterrows():
            pretty = prettify_feature(r["Feature"])
            risk_rows += f"""
            <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;
                        border-bottom:1px solid rgba(255,255,255,0.05);">
                <span style="color:#cbd5e1;font-size:0.82rem;">{pretty}</span>
                <span style="font-weight:700;color:#ef4444;font-size:0.82rem;">
                    +{r['Contribution']:.3f}
                </span>
            </div>"""
        for _, r in top_retention_drivers.iterrows():
            pretty = prettify_feature(r["Feature"])
            risk_rows += f"""
            <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;
                        border-bottom:1px solid rgba(255,255,255,0.05);">
                <span style="color:#cbd5e1;font-size:0.82rem;">{pretty}</span>
                <span style="font-weight:700;color:#4ade80;font-size:0.82rem;">
                    {r['Contribution']:.3f}
                </span>
            </div>"""

        st.markdown(
            f"""
            <div style="margin-top:20px;padding:14px 16px;background:rgba(30,41,59,0.6);
                        border-radius:12px;border:1px solid rgba(255,255,255,0.06);">
                <div style="display:flex;align-items:center;gap:8px;
                            color:#ffffff;font-weight:700;font-size:0.88rem;margin-bottom:10px;">
                    {icon("search", size=14, colour="#38bdf8")} Model-Derived Feature Contributions
                </div>
                <div style="display:flex;flex-direction:column;">{risk_rows}</div>
                <p style="color:#475569;font-size:0.72rem;margin:8px 0 0 0;">
                    Values show log-odds contribution to this prediction
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Recommendations (bulleted) ────────────────────────
        if is_high_risk:
            rec_title   = "Immediate HR Retention Plan Required"
            rec_bullets = [
                "Evaluate and reduce overtime workload immediately",
                "Schedule a structured 1-on-1 career development conversation",
                "Review compensation vs. market benchmarks for this role",
                "Increase engagement through mentoring or project ownership",
                "Monitor job satisfaction scores monthly for the next quarter",
                "Assess promotion timelines and accelerate where feasible",
            ]
        else:
            rec_title   = "Standard Retention & Development Plan"
            rec_bullets = [
                "Maintain current engagement cadence with regular 1-on-1 check-ins",
                "Offer training and certification opportunities aligned to career goals",
                "Recognise contributions through structured performance reviews",
                "Ensure clarity of promotion pathway and timeline",
                "Monitor satisfaction and work-life balance on a quarterly basis",
            ]

        bullets_html = "\n".join(f"<li>{b}</li>" for b in rec_bullets)
        rec_icon     = icon("alert-triangle", size=14, colour="#f59e0b") if is_high_risk else icon("lightbulb", size=14, colour="#38bdf8")
        rec_border   = "rgba(245,158,11,0.25)" if is_high_risk else "rgba(56,189,248,0.2)"
        rec_bg       = "rgba(245,158,11,0.06)" if is_high_risk else "rgba(56,189,248,0.06)"
        rec_title_colour = "#fbbf24" if is_high_risk else "#38bdf8"

        st.markdown(
            f"""
            <div style="margin-top:14px;padding:14px 16px;background:{rec_bg};
                        border-radius:12px;border:1px solid {rec_border};">
                <div style="display:flex;align-items:center;gap:8px;
                            font-weight:700;font-size:0.88rem;color:{rec_title_colour};margin-bottom:10px;">
                    {rec_icon} {rec_title}
                </div>
                <ul class="rec-bullets">
                    {bullets_html}
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── PDF Download ──────────────────────────────────────
        st.markdown('<div style="margin-top: 14px;"></div>', unsafe_allow_html=True)

        _model_name = get_model_display_name()
        _risk_pairs      = [(r["Feature"], r["Contribution"]) for _, r in top_risk_drivers.iterrows()]
        _retention_pairs = [(r["Feature"], r["Contribution"]) for _, r in top_retention_drivers.iterrows()]

        try:
            pdf_bytes = generate_prediction_pdf(
                department=department,
                job_role=job_role,
                age=age,
                gender=gender,
                monthly_income=monthly_income,
                overtime=overtime,
                job_satisfaction=job_satisfaction,
                marital_status=marital_status,
                prediction=int(prediction),
                probability=float(probability),
                confidence=float(confidence),
                top_risk_features=_risk_pairs,
                top_retention_features=_retention_pairs,
                model_name=_model_name,
                rec_title=rec_title,
                rec_bullets=rec_bullets,
            )
            st.download_button(
                label="Download Executive PDF Report",
                data=pdf_bytes,
                file_name=f"pulsehr_attrition_report_{job_role.lower().replace(' ', '_')}.pdf",
                mime="application/pdf",
                key="btn_download_pdf",
            )
        except Exception as e:
            st.error(f"PDF generation failed: {e}")

render_footer()