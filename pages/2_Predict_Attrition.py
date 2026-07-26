import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Predict Attrition",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Employee Attrition Prediction")
st.markdown("Enter employee information to estimate the likelihood of attrition.")

model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

feature_names = joblib.load("models/feature_names.pkl")

st.subheader("👤 Employee Profile")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        18,
        60,
        30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

with col2:

    education = st.selectbox(
        "Education Level",
        [1,2,3,4,5]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

st.subheader("💼 Job Information")

col1, col2 = st.columns(2)

with col1:

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    job_role = st.selectbox(
        "Job Role",
        sorted([
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ])
    )

    job_level = st.slider(
        "Job Level",
        1,
        5,
        2
    )

    job_involvement = st.selectbox(
    "Job Involvement",
    [1, 2, 3, 4]
    )

with col2:

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    overtime = st.selectbox(
        "OverTime",
        [
            "No",
            "Yes"
        ]
    )

    performance_rating = st.selectbox(
    "Performance Rating",
    [3, 4]
   )

st.subheader("📈 Performance & Satisfaction")

col1, col2 = st.columns(2)

with col1:

    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        3
    )

    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        3
    )
    
    relationship_satisfaction = st.selectbox(
    "Relationship Satisfaction",
    [1, 2, 3, 4]
    )
    
    work_life_balance = st.slider(
        "Work-Life Balance",
        1,
        4,
        3
    )

with col2:

    monthly_income = st.number_input(
        "Monthly Income",
        1000,
        30000,
        6500
    )

    stock_option_level = st.selectbox(
    "Stock Option Level",
    [0, 1, 2, 3]
   )

    percent_salary_hike = st.slider(
        "Percent Salary Hike",
        10,
        25,
        15
    )

    training = st.slider(
        "Training Times Last Year",
        0,
        6,
        2
    )

st.subheader("📅 Experience")

col1, col2 = st.columns(2)

with col1:

    total_working_years = st.slider(
        "Total Working Years",
        0,
        40,
        10
    )

    years_company = st.slider(
        "Years at Company",
        0,
        40,
        5
    )

    num_companies_worked = st.slider(
    "Number of Companies Worked",
    0,
    10,
    2
   )

with col2:

    years_promotion = st.slider(
        "Years Since Last Promotion",
        0,
        15,
        2
    )

    years_current_role = st.slider(
    "Years in Current Role",
    0,
    20,
    3
    )

    years_with_manager = st.slider(
        "Years with Current Manager",
        0,
        20,
        4
    )

    distance = st.slider(
        "Distance From Home",
        1,
        30,
        10
    )

predict_button = st.button(
    "🔍 Predict Attrition"
)

if predict_button:

    input_df = pd.DataFrame({

        "Age":[age],
        "Gender":[gender],
        "MaritalStatus":[marital_status],
        "Education":[education],
        "EducationField":[education_field],

        "Department":[department],
        "JobRole":[job_role],
        "JobLevel":[job_level],
        "JobInvolvement": [job_involvement],
        "BusinessTravel":[business_travel],
        "OverTime":[overtime],
        "PerformanceRating": [performance_rating],

        "JobSatisfaction":[job_satisfaction],
        "EnvironmentSatisfaction":[environment_satisfaction],
        "RelationshipSatisfaction": [relationship_satisfaction],
        "WorkLifeBalance":[work_life_balance],

        "MonthlyIncome":[monthly_income],
        "StockOptionLevel": [stock_option_level],
        "PercentSalaryHike":[percent_salary_hike],
        "TrainingTimesLastYear":[training],

        "TotalWorkingYears":[total_working_years],
        "YearsAtCompany":[years_company],
        "NumCompaniesWorked": [num_companies_worked],

        "YearsSinceLastPromotion":[years_promotion],
        "YearsInCurrentRole": [years_current_role],
        "YearsWithCurrManager": [years_with_manager],
        "DistanceFromHome":[distance]
    })

    input_df["IncomeGroup"] = pd.cut(
    input_df["MonthlyIncome"],
    bins=[1009, 2911, 4919, 8379, 19999],
    labels=["Low", "Medium", "High", "Very High"],
    include_lowest=True
    )

    input_df["ExperienceGroup"] = pd.cut(

    input_df["TotalWorkingYears"],

    bins=[0,5,10,20,40],

    labels=[
        "Early Career",
        "Mid Career",
        "Senior",
        "Highly Experienced"
    ]
    )

    input_df["PromotionDelay"] = pd.cut(

    input_df["YearsSinceLastPromotion"],

    bins=[-1,1,3,6,20],

    labels=[
        "Recently Promoted",
        "Moderate Delay",
        "Long Delay",
        "Very Long Delay"
    ]
    )

    input_df["DistanceCategory"] = pd.cut(

    input_df["DistanceFromHome"],

    bins=[0,5,15,30],

    labels=[
        "Near",
        "Moderate",
        "Far"
    ]
    )

    input_df["OverallSatisfaction"] = (
    input_df["EnvironmentSatisfaction"]
    + input_df["JobSatisfaction"]
    + input_df["RelationshipSatisfaction"]
    + input_df["WorkLifeBalance"]
    )

    input_df["TenureGroup"] = pd.cut(

    input_df["YearsAtCompany"],

    bins=[0,2,5,10,40],

    labels=[
        "New",
        "Junior",
        "Experienced",
        "Veteran"
    ]
    )

    input_df = pd.get_dummies(input_df)

    feature_names = joblib.load("models/feature_names.pkl")

    input_df = input_df.reindex(
    columns=feature_names,
    fill_value=0
    )

    numerical_columns = [
    "Age",
    "DailyRate",
    "DistanceFromHome",
    "Education",
    "EnvironmentSatisfaction",
    "HourlyRate",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "MonthlyIncome",
    "MonthlyRate",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
    "OverallSatisfaction"
    ]
    input_scaled = input_df.copy()

    input_scaled[numerical_columns] = scaler.transform(
        input_scaled[numerical_columns]
    )

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]   

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ High Attrition Risk")

    else:

     st.success("✅ Low Attrition Risk")

    st.metric(

    "Attrition Probability",

    f"{probability*100:.2f}%"
    )
    st.progress(float(probability))

    confidence = max(probability,1-probability)

    st.write(
        f"**Model Confidence:** {confidence*100:.2f}%"
    )