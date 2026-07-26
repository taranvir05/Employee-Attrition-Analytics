import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Business Insights",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Business Insights")
st.write(
    """
This page summarizes the key findings from the employee attrition analysis
and provides actionable HR recommendations based on data-driven insights.
"""
)

df = pd.read_csv(
    "data/employee_attrition_feature_engineered.csv"
)

st.markdown("## 📊 Executive Summary")

attrition_rate = df["Attrition"].value_counts(normalize=True)["Yes"] * 100

highest_department = (
    df[df["Attrition"] == "Yes"]["Department"]
    .value_counts()
    .idxmax()
)

highest_jobrole = (
    df[df["Attrition"] == "Yes"]["JobRole"]
    .value_counts()
    .idxmax()
)

st.success(f"""
### Key Findings

• Overall Attrition Rate: **{attrition_rate:.2f}%**

• Department with Highest Attrition:
**{highest_department}**

• Job Role with Highest Attrition:
**{highest_jobrole}**
""")

st.markdown("---")
st.subheader("📌 Insight 1 – Attrition by Department")

fig, ax = plt.subplots(figsize=(7,4))

sns.countplot(
    data=df,
    x="Department",
    hue="Attrition",
    ax=ax
)

plt.xticks(rotation=15)

st.pyplot(fig)

st.info("""
### Observation

Sales and Research & Development departments account for the majority
of employee attrition.

Employees in these departments may experience higher workloads,
greater performance pressure, or more competitive external opportunities.
""")

st.success("""
### Recommendation

HR should monitor attrition trends in high-risk departments,
conduct regular engagement surveys, and implement targeted
retention strategies.
""")

st.markdown("---")
st.subheader("⏰ Insight 2 – Overtime vs Attrition")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="OverTime",
    hue="Attrition",
    ax=ax
)

st.pyplot(fig)

st.info("""
### Observation

Employees who frequently work overtime are much more likely
to leave the company than employees who do not work overtime.
""")

st.success("""
### Recommendation

Reduce excessive overtime through workload balancing,
resource planning, and flexible scheduling.
""")

st.markdown("---")
st.subheader("😊 Insight 3 – Job Satisfaction")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="JobSatisfaction",
    hue="Attrition",
    ax=ax
)

st.pyplot(fig)

st.info("""
### Observation

Lower job satisfaction is associated with a higher likelihood
of employee attrition.
""")

st.success("""
### Recommendation

Regular feedback sessions,
recognition programmes,
and career development initiatives
can improve employee satisfaction.
""")
st.markdown("---")
st.subheader("💰 Insight 4 – Monthly Income")

fig, ax = plt.subplots(figsize=(7,4))

sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome",
    ax=ax
)

st.pyplot(fig)

st.info("""
### Observation

Employees with lower monthly income tend to leave
more frequently than higher-paid employees.
""")

st.success("""
### Recommendation

Review compensation structures,
especially for critical job roles,
to improve employee retention.
""")

st.markdown("---")
st.subheader("⚖️ Insight 5 – Work-Life Balance")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="WorkLifeBalance",
    hue="Attrition",
    ax=ax
)

st.pyplot(fig)

st.info("""
### Observation

Employees reporting poor work-life balance
are more likely to leave the organisation.
""")

st.success("""
### Recommendation

Encourage flexible working arrangements,
mental wellness initiatives,
and balanced workloads.
""")

st.markdown("---")
st.subheader("🎯 Strategic HR Recommendations")

st.markdown("""
### Based on the analysis, the following actions are recommended:

- Monitor employees working overtime regularly.
- Improve job satisfaction through recognition and career growth.
- Prioritise retention efforts in high-attrition departments.
- Review compensation for critical roles.
- Strengthen work-life balance initiatives.
- Identify high-risk employees early using predictive analytics.
""")

st.markdown("---")

st.subheader("📌 Key Takeaways")

st.success("""
✔ Attrition is influenced by multiple factors rather than a single cause.

✔ Overtime, job satisfaction, monthly income, and work-life balance are among the strongest indicators.

✔ Predictive analytics enables HR teams to identify employees at risk before they resign.

✔ Combining machine learning with explainable AI supports informed and proactive retention strategies.
""")