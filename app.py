import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Employee Attrition Analytics")

st.subheader("Predict • Explain • Retain")

st.markdown("---")

st.markdown("""
## Welcome!

This HR Analytics platform combines Machine Learning, Explainable AI, and Business Intelligence to help organizations identify employees who are at risk of leaving and support proactive retention strategies.
""")

st.markdown("## 🎯 Project Objectives")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🤖\n\nPredict Employee Attrition")
with col2:
    st.info("🧠\n\nExplain Model Predictions")
with col3:
    st.info("📊\n\nHR Analytics Dashboard")
with col4:
    st.info("💼\n\nBusiness Decision Support")

st.markdown("---")

st.markdown("## 📁 Dataset")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Employees", "1470")
with col2:
    st.metric("Features", "35+")
with col3:
    st.metric("Target Variable", "Attrition")

st.markdown("---")

st.markdown("## 🛠 Technology Stack")

st.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP
- Streamlit
- Matplotlib
- Seaborn
""")

st.markdown("---")

st.markdown("## 🔄 Project Workflow")
with st.expander("View Project Workflow"):
        st.markdown("""
1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Model Evaluation
8. Model Explainability
9. Streamlit Deployment
""")
st.markdown("---")

st.markdown("## ✅ Current Progress")

st.success("✔ Data Understanding")
st.success("✔ Data Cleaning")
st.success("✔ Exploratory Data Analysis")
st.success("✔ Feature Engineering")
st.success("✔ Data Preprocessing")
st.success("✔ Model Building")
st.success("✔ Model Evaluation")
st.success("✔ Model Explainability")
st.info("🚀 Streamlit Dashboard Development")

st.sidebar.title("Employee Attrition Analytics")

st.sidebar.info("""
Navigate through the pages using the menu above.

This application demonstrates an end-to-end Machine Learning workflow for predicting employee attrition and supporting HR decision-making.
""")

st.markdown("---")

st.caption(
    "Developed by Taranvir Kaur | Employee Attrition Analytics | Streamlit + Machine Learning + Explainable AI"
)