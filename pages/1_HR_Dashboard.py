import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="HR Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HR Dashboard")

st.markdown(
    """
This dashboard provides an overview of the workforce and highlights key employee characteristics, workforce composition, and attrition trends.
"""
)

st.markdown("---")

@st.cache_data
def load_data():
    return pd.read_csv("data/employee_attrition_feature_engineered.csv")

df = load_data()

st.subheader("📌 Company Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        "Employees",
        len(df)
    )
with col2:
    st.metric(
        "Departments",
        df["Department"].nunique()
    )
with col3:
    st.metric(
        "Average Age",
        round(df["Age"].mean(), 1)
    )
attrition_rate = (
    (df["Attrition"] == "Yes").mean() * 100
)

with col4:
    st.metric(
        "Attrition Rate",
        f"{attrition_rate:.1f}%"
    )

st.markdown("---")
st.subheader("👥 Employee Distribution")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="Department",
        ax=ax
    )

    plt.xticks(rotation=15)

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="Gender",
        ax=ax
    )

    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:

    fig, ax = plt.subplots(figsize=(8,4))

    sns.countplot(
        data=df,
        y="JobRole",
        order=df["JobRole"].value_counts().index,
        ax=ax
    )

    st.pyplot(fig)

with col4:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        y="EducationField",
        order=df["EducationField"].value_counts().index,
        ax=ax
    )

    st.pyplot(fig)

st.markdown("---")

st.subheader("📉 Attrition Analysis")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="Department",
        hue="Attrition",
        ax=ax
    )

    plt.xticks(rotation=15)
    plt.title("Attrition by Department")

    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="OverTime",
        hue="Attrition",
        ax=ax
    )

    plt.title("Attrition by Overtime")

    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="WorkLifeBalance",
        hue="Attrition",
        ax=ax
    )

    plt.title("Attrition by Work-Life Balance")

    st.pyplot(fig)

with col4:
    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="JobSatisfaction",
        hue="Attrition",
        ax=ax
    )

    plt.title("Attrition by Job Satisfaction")

    st.pyplot(fig)

st.markdown("---")
st.subheader("📈 Numerical Analysis")

col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.histplot(
        data=df,
        x="Age",
        bins=20,
        kde=True,
        ax=ax
    )

    plt.title("Age Distribution")

    st.pyplot(fig)

with col2:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.histplot(
        data=df,
        x="MonthlyIncome",
        bins=20,
        kde=True,
        ax=ax
    )

    plt.title("Monthly Income Distribution")

    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:

    fig, ax = plt.subplots(figsize=(6,4))

    sns.histplot(
        data=df,
        x="YearsAtCompany",
        bins=15,
        kde=True,
        ax=ax
    )

    plt.title("Years at Company")

    st.pyplot(fig)

with col4:

    fig, ax = plt.subplots(figsize=(7,4))

    sns.barplot(
        data=df,
        x="Department",
        y="MonthlyIncome",
        estimator="mean",
        errorbar=None,
        ax=ax
    )

    plt.xticks(rotation=15)
    plt.title("Average Monthly Income by Department")

    st.pyplot(fig)

st.markdown("---")
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(14,10))

corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False,
    linewidths=0.5,
    ax=ax
)

plt.title("Correlation Matrix")

st.pyplot(fig)

st.markdown("---")
st.subheader("💡 Key Business Insights")

st.info("""
📌 Research & Development has the largest workforce in the organization.

📌 Employees working overtime show noticeably higher attrition than those who do not.

📌 Lower job satisfaction and poorer work-life balance are associated with increased employee turnover.

📌 Employees with fewer years at the company tend to leave more frequently.

📌 Monthly income varies across departments, but salary alone is not the strongest predictor of attrition.
""")