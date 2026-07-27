import streamlit as st
import pandas as pd
import joblib
import numpy as np
from utils.style import load_css
from utils.helpers import render_sidebar, render_section_header, render_footer

st.set_page_config(
    page_title="Predict Attrition - PulseHR",
    page_icon="🤖",
    layout="wide"
)

load_css()
render_sidebar()

# Model Loading (Preserving exact backend logic)
@st.cache_resource
def load_ml_assets():
    model = joblib.load("models/best_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_names = joblib.load("models/feature_names.pkl")
    return model, scaler, feature_names

model, scaler, feature_names = load_ml_assets()

render_section_header(
    "Employee Attrition Prediction Studio",
    "Enter employee characteristics to calculate real-time departure probability & risk evaluation",
    "PREDICTIVE ENGINE"
)

# ==========================================
# SPLIT SCREEN LAYOUT
# ==========================================
col_form, col_result = st.columns([1.1, 1])

with col_form:
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #ffffff; font-size: 1.15rem; font-weight: 700; margin-top:0;">👤 Employee Data Entry Form</h3>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Profile & Edu", "Job & Role", "Satisfaction", "Tenure & Pay"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            age = st.slider("Age", 18, 60, 30)
            gender = st.selectbox("Gender", ["Male", "Female"])
            marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        with c2:
            education = st.selectbox("Education Level", [1, 2, 3, 4, 5], format_func=lambda x: f"Level {x}")
            education_field = st.selectbox("Education Field", [
                "Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"
            ])
            distance = st.slider("Distance From Home (miles)", 1, 30, 10)

    with tab2:
        c1, c2 = st.columns(2)
        with c1:
            department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
            job_role = st.selectbox("Job Role", sorted([
                "Sales Executive", "Research Scientist", "Laboratory Technician",
                "Manufacturing Director", "Healthcare Representative", "Manager",
                "Sales Representative", "Research Director", "Human Resources"
            ]))
            job_level = st.slider("Job Level", 1, 5, 2)
            job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
        with c2:
            business_travel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
            overtime = st.selectbox("OverTime Work", ["No", "Yes"])
            performance_rating = st.selectbox("Performance Rating", [3, 4])

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
            environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
        with c2:
            relationship_satisfaction = st.selectbox("Relationship Satisfaction (1-4)", [1, 2, 3, 4])
            work_life_balance = st.slider("Work-Life Balance (1-4)", 1, 4, 3)

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            monthly_income = st.number_input("Monthly Income ($)", 1000, 30000, 6500, step=500)
            stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
            percent_salary_hike = st.slider("Percent Salary Hike (%)", 10, 25, 15)
            training = st.slider("Training Times Last Year", 0, 6, 2)
        with c2:
            total_working_years = st.slider("Total Working Years", 0, 40, 10)
            years_company = st.slider("Years at Company", 0, 40, 5)
            num_companies_worked = st.slider("Companies Worked For", 0, 10, 2)
            years_promotion = st.slider("Years Since Last Promotion", 0, 15, 2)
            years_current_role = st.slider("Years in Current Role", 0, 20, 3)
            years_with_manager = st.slider("Years with Current Manager", 0, 20, 4)

    st.markdown("<br>", unsafe_allow_html=True)
    predict_button = st.button("⚡ Run ML Prediction Analysis", key="btn_run_pred")
    st.markdown('</div>', unsafe_allow_html=True)

with col_result:
    if not predict_button:
        st.markdown(
            """
            <div class="saas-card" style="text-align: center; padding: 60px 20px; border: 2px dashed rgba(56, 189, 248, 0.2);">
                <div style="font-size: 3rem; margin-bottom: 12px; opacity: 0.8;">🧠</div>
                <h3 style="color: #ffffff; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Awaiting Input Parameters</h3>
                <p style="color: #94a3b8; font-size: 0.9rem; max-width: 360px; margin: 0 auto 20px auto;">
                    Adjust the employee profile form on the left and click <b>"Run ML Prediction Analysis"</b> to generate real-time risk assessment.
                </p>
                <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;">
                    <span class="badge-pill badge-cyan">Random Forest</span>
                    <span class="badge-pill badge-purple">SHAP Factor Analysis</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # ==========================================
        # PRESET EXACT FEATURE PREPROCESSING & PREDICTION
        # ==========================================
        input_df = pd.DataFrame({
            "Age": [age],
            "Gender": [gender],
            "MaritalStatus": [marital_status],
            "Education": [education],
            "EducationField": [education_field],
            "Department": [department],
            "JobRole": [job_role],
            "JobLevel": [job_level],
            "JobInvolvement": [job_involvement],
            "BusinessTravel": [business_travel],
            "OverTime": [overtime],
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
            "DistanceFromHome": [distance]
        })

        input_df["IncomeGroup"] = pd.cut(
            input_df["MonthlyIncome"],
            bins=[1009, 2911, 4919, 8379, 19999],
            labels=["Low", "Medium", "High", "Very High"],
            include_lowest=True
        )

        input_df["ExperienceGroup"] = pd.cut(
            input_df["TotalWorkingYears"],
            bins=[0, 5, 10, 20, 40],
            labels=["Early Career", "Mid Career", "Senior", "Highly Experienced"]
        )

        input_df["PromotionDelay"] = pd.cut(
            input_df["YearsSinceLastPromotion"],
            bins=[-1, 1, 3, 6, 20],
            labels=["Recently Promoted", "Moderate Delay", "Long Delay", "Very Long Delay"]
        )

        input_df["DistanceCategory"] = pd.cut(
            input_df["DistanceFromHome"],
            bins=[0, 5, 15, 30],
            labels=["Near", "Moderate", "Far"]
        )

        input_df["OverallSatisfaction"] = (
            input_df["EnvironmentSatisfaction"]
            + input_df["JobSatisfaction"]
            + input_df["RelationshipSatisfaction"]
            + input_df["WorkLifeBalance"]
        )

        input_df["TenureGroup"] = pd.cut(
            input_df["YearsAtCompany"],
            bins=[0, 2, 5, 10, 40],
            labels=["New", "Junior", "Experienced", "Veteran"]
        )

        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

        numerical_columns = [
            "Age", "DailyRate", "DistanceFromHome", "Education", "EnvironmentSatisfaction",
            "HourlyRate", "JobInvolvement", "JobLevel", "JobSatisfaction", "MonthlyIncome",
            "MonthlyRate", "NumCompaniesWorked", "PercentSalaryHike", "PerformanceRating",
            "RelationshipSatisfaction", "StockOptionLevel", "TotalWorkingYears",
            "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany", "YearsInCurrentRole",
            "YearsSinceLastPromotion", "YearsWithCurrManager", "OverallSatisfaction"
        ]
        
        input_scaled = input_encoded.copy()
        input_scaled[numerical_columns] = scaler.transform(input_scaled[numerical_columns])

        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        confidence = max(probability, 1 - probability)

        # ==========================================
        # RENDER PREDICTION DASHBOARD CARD
        # ==========================================
        is_high_risk = (prediction == 1)
        status_color = "#ef4444" if is_high_risk else "#22c55e"
        badge_text = "⚠️ HIGH ATTRITION RISK" if is_high_risk else "✅ LOW ATTRITION RISK"
        badge_type = "danger" if is_high_risk else "success"

        st.markdown('<div class="saas-card" style="border: 1px solid ' + status_color + ';">', unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <span class="badge-pill badge-{badge_type}" style="font-size: 0.85rem; padding: 6px 14px;">{badge_text}</span>
                <span style="color: #94a3b8; font-size: 0.82rem; font-weight: 600;">Model Confidence: {confidence*100:.1f}%</span>
            </div>
            <div style="text-align: center; margin: 15px 0 20px 0;">
                <div style="font-size: 0.82rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">ESTIMATED ATTRITION PROBABILITY</div>
                <div style="font-size: 3.2rem; font-weight: 800; color: {status_color}; margin: 4px 0;">{probability*100:.1f}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(float(probability))

        # Risk breakdown factors
        st.markdown(
            f"""
            <div style="margin-top: 24px; padding: 16px; background: rgba(30, 41, 59, 0.6); border-radius: 12px; border: 1px solid rgba(255,255,255,0.06);">
                <div style="color: #ffffff; font-weight: 700; font-size: 0.9rem; margin-bottom: 10px;">🔍 Top Risk Factor Assessment</div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.82rem;">
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #cbd5e1;">OverTime Status:</span>
                        <span style="font-weight: 700; color: {'#ef4444' if overtime == 'Yes' else '#4ade80'};">{overtime}</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #cbd5e1;">Job Satisfaction Level:</span>
                        <span style="font-weight: 700; color: {'#ef4444' if job_satisfaction <= 2 else '#4ade80'};">{job_satisfaction} / 4</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #cbd5e1;">Work-Life Balance Level:</span>
                        <span style="font-weight: 700; color: {'#ef4444' if work_life_balance <= 2 else '#4ade80'};">{work_life_balance} / 4</span>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: #cbd5e1;">Years Since Last Promotion:</span>
                        <span style="font-weight: 700; color: {'#f59e0b' if years_promotion >= 4 else '#38bdf8'};">{years_promotion} yrs</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Strategic Recommendation
        rec_title = "Immediate HR Retention Plan Required" if is_high_risk else "Standard Retention & Development Plan"
        rec_text = "Schedule a 1-on-1 career review, evaluate workload balancing, and consider salary/bonus adjustments." if is_high_risk else "Maintain ongoing engagement, offer regular training opportunities, and review career progression targets."
        
        st.markdown(
            f"""
            <div style="margin-top: 16px; padding: 14px; background: rgba(56, 189, 248, 0.08); border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">
                <div style="color: #38bdf8; font-weight: 700; font-size: 0.88rem; margin-bottom: 4px;">💡 Recommendation: {rec_title}</div>
                <div style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.5;">{rec_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Download PDF/TXT Report
        report_txt = f"""PULSEHR ATTRITION PREDICTION REPORT
----------------------------------
Employee Profile Summary:
Department: {department}
Job Role: {job_role}
Age: {age} | Gender: {gender}
Monthly Income: ${monthly_income:,}
OverTime: {overtime} | Job Satisfaction: {job_satisfaction}/4

ML Model Assessment:
Prediction: {'HIGH ATTRITION RISK' if prediction == 1 else 'LOW ATTRITION RISK'}
Departure Probability: {probability*100:.2f}%
Model Confidence: {confidence*100:.2f}%

Recommended Action:
{rec_text}
"""
        st.download_button(
            label="📄 Download Prediction Executive Report",
            data=report_txt,
            file_name=f"attrition_report_{department.lower().replace(' ', '_')}.txt",
            mime="text/plain"
        )
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()