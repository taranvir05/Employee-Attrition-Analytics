import streamlit as st
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Model Explainability",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Model Explainability")
st.write(
    """
Understand **why** the machine learning model predicted that an employee
is likely (or unlikely) to leave the organisation using Explainable AI (SHAP).
    """
)

model = joblib.load("models/best_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.info(
"""
SHAP (SHapley Additive exPlanations) explains how each feature contributes
towards the final prediction.

Positive SHAP values increase the likelihood of attrition.

Negative SHAP values decrease the likelihood of attrition.
"""
)

st.subheader("📊 Individual Prediction Explanation")

st.warning(
"""
Prediction explanations will appear here after integrating
the prediction module with SHAP.
"""
)
st.subheader("🌍 Global Feature Importance")

st.write(
"""
These plots show which employee attributes generally have the
largest impact on predicting attrition across the entire dataset.
"""
)

col1, col2 = st.columns(2)

with col1:

    st.image(
        "images/shap_summary.png",
        caption="SHAP Summary Plot",
        use_container_width=True
    )

with col2:

    st.image(
        "images/shap_bar.png",
        caption="SHAP Feature Importance",
        use_container_width=True
    )

st.subheader("💼 HR Interpretation")

st.success("""
The SHAP analysis indicates which employee characteristics
have the strongest influence on attrition predictions.

For example:

• Frequent overtime generally increases attrition risk.

• Higher job satisfaction tends to reduce attrition risk.

• Long promotion delays often contribute positively to attrition risk.

• Employees with better work-life balance are generally less likely to leave.
""")

st.subheader("📌 Recommended HR Actions")

st.markdown("""
- Reduce excessive overtime where possible.
- Improve employee engagement through feedback sessions.
- Provide timely promotions and career progression.
- Encourage healthy work-life balance initiatives.
- Recognise high-performing employees regularly.
""")

with st.expander("📖 What is SHAP?"):

    st.write("""
SHAP (SHapley Additive exPlanations) is an Explainable AI technique
that assigns each feature a contribution value for every prediction.

Instead of simply stating that an employee is likely to leave,
SHAP explains **why** by showing which features pushed the prediction
towards higher or lower attrition risk.
""")