import streamlit as st
st.set_page_config(
    page_title="About Project",
    page_icon="📄",
    layout="wide"
)

st.title("📄 About the Project")

st.write(
    """
This application demonstrates how Machine Learning and Explainable AI can
support Human Resource (HR) teams in identifying employees at risk of attrition
and making informed retention decisions.
"""
)

st.markdown("---")
st.header("🎯 Problem Statement")

st.info("""
Employee attrition is a major challenge for organizations as it leads to
increased recruitment costs, knowledge loss, and reduced productivity.

The goal of this project is to build a predictive analytics solution that
identifies employees who are likely to leave the organization and explains
the reasons behind those predictions using Explainable AI.
""")

st.markdown("---")
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("✔ Predict employee attrition")
    st.success("✔ Identify key attrition drivers")
    st.success("✔ Provide HR business insights")

with col2:
    st.success("✔ Explain predictions using SHAP")
    st.success("✔ Support proactive retention strategies")
    st.success("✔ Build an interactive HR Analytics dashboard")

st.markdown("---")
st.header("📊 Dataset")

st.markdown("""
**Dataset:** IBM HR Employee Attrition Dataset

- Employees: **1,470**
- Features: **38 (including engineered features)**
- Target Variable: **Attrition**
- Type: Binary Classification
""")

st.markdown("---")
st.header("🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### Programming
- Python
- Pandas
- NumPy
""")

with col2:
    st.markdown("""
### Machine Learning
- Scikit-learn
- SHAP
- Joblib
""")

with col3:
    st.markdown("""
### Visualization
- Streamlit
- Matplotlib
- Seaborn
""")

st.markdown("---")
st.header("⚙️ Project Workflow")

st.code("""
Data Collection
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Data Preprocessing
        ↓
Model Building
        ↓
Model Evaluation
        ↓
Model Explainability (SHAP)
        ↓
Streamlit Dashboard
""")

st.markdown("---")
st.header("🤖 Machine Learning Models")

st.table({
    "Algorithm":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Purpose":[
        "Baseline Classification Model",
        "Non-linear Decision Model",
        "Final Ensemble Model"
    ]
})

st.markdown("---")
st.header("⭐ Application Features")

st.markdown("""
- 📊 Interactive HR Analytics Dashboard
- 🤖 Employee Attrition Prediction
- 🧠 Explainable AI using SHAP
- 💼 Business Insights and Recommendations
- 📈 Professional Data Visualizations
- 📄 End-to-End Machine Learning Pipeline
""")

st.markdown("---")
st.header("🚀 Future Enhancements")

st.markdown("""
- Integration with live HR databases
- Real-time employee monitoring
- Automated email alerts for high-risk employees
- Hyperparameter tuning for improved model performance
- Cloud deployment with authentication
- Advanced workforce analytics dashboards
""")

st.markdown("---")
st.header("📈 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Employees", "1,470")

with col2:
    st.metric("Features", "38")

with col3:
    st.metric("ML Models", "3")

with col4:
    st.metric("Target", "Attrition")

st.markdown("---")
st.header("🙏 Acknowledgement")

st.write("""
This project was developed as an end-to-end Machine Learning and HR Analytics solution.
It demonstrates the complete workflow from data preprocessing and model development
to explainable AI and interactive dashboard deployment using Streamlit.
""")