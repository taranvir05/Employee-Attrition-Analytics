import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Color Palette Constants matching Enterprise Dark Theme
CYAN = "#38bdf8"
BLUE = "#3b82f6"
PURPLE = "#8b5cf6"
RED = "#ef4444"
GREEN = "#22c55e"
AMBER = "#f59e0b"

def apply_theme(fig, title=""):
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>",
            font=dict(size=14, color="#ffffff"),
            x=0.01, y=0.98
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#cbd5e1", family="Plus Jakarta Sans, sans-serif"),
        margin=dict(l=35, r=35, t=60, b=35),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title_text=""
        )
    )
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.06)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255, 255, 255, 0.06)")
    return fig

def plot_department_attrition(df):
    counts = df.groupby(["Department", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x="Department",
        y="Count",
        color="Attrition",
        barmode="group",
        color_discrete_map={"Yes": RED, "No": CYAN},
        text="Count"
    )
    fig.update_traces(textposition="outside", marker_line_width=0)
    return apply_theme(fig, "Department Attrition Breakdown")

def plot_attrition_distribution(df):
    counts = df["Attrition"].value_counts().reset_index()
    counts.columns = ["Attrition", "Count"]
    fig = px.pie(
        counts,
        names="Attrition",
        values="Count",
        hole=0.6,
        color="Attrition",
        color_discrete_map={"Yes": RED, "No": CYAN}
    )
    fig.update_traces(textinfo="percent+label", pull=[0.05, 0])
    return apply_theme(fig, "Overall Attrition Distribution")

def plot_gender_donut(df):
    counts = df["Gender"].value_counts().reset_index()
    counts.columns = ["Gender", "Count"]
    fig = px.pie(
        counts,
        names="Gender",
        values="Count",
        hole=0.55,
        color_discrete_sequence=[CYAN, PURPLE]
    )
    fig.update_traces(textinfo="percent+label", pull=[0.02, 0.02])
    return apply_theme(fig, "Workforce Gender Composition")

def plot_job_role_attrition(df):
    counts = df.groupby(["JobRole", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        y="JobRole",
        x="Count",
        color="Attrition",
        orientation="h",
        barmode="stack",
        color_discrete_map={"Yes": RED, "No": BLUE}
    )
    return apply_theme(fig, "Job Role Attrition Volume")

def plot_business_travel_attrition(df):
    counts = df.groupby(["BusinessTravel", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x="BusinessTravel",
        y="Count",
        color="Attrition",
        barmode="group",
        color_discrete_map={"Yes": RED, "No": PURPLE},
        text="Count"
    )
    fig.update_traces(textposition="outside")
    return apply_theme(fig, "Business Travel Impact")

def plot_education_field(df):
    counts = df.groupby(["EducationField", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        y="EducationField",
        x="Count",
        color="Attrition",
        orientation="h",
        color_discrete_map={"Yes": RED, "No": CYAN}
    )
    return apply_theme(fig, "Education Field Distribution")

def plot_promotion_delay_attrition(df):
    col_name = "YearsSinceLastPromotion" if "YearsSinceLastPromotion" in df.columns else "PromotionDelay"
    counts = df.groupby([col_name, "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x=col_name,
        y="Count",
        color="Attrition",
        barmode="stack",
        color_discrete_map={"Yes": RED, "No": GREEN}
    )
    return apply_theme(fig, "Years Since Last Promotion")

def plot_overtime_attrition(df):
    counts = df.groupby(["OverTime", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x="OverTime",
        y="Count",
        color="Attrition",
        barmode="group",
        color_discrete_map={"Yes": RED, "No": GREEN},
        text="Count"
    )
    fig.update_traces(textposition="outside")
    return apply_theme(fig, "Overtime Impact on Attrition")

def plot_work_life_balance(df):
    counts = df.groupby(["WorkLifeBalance", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x="WorkLifeBalance",
        y="Count",
        color="Attrition",
        barmode="group",
        color_discrete_map={"Yes": RED, "No": CYAN}
    )
    return apply_theme(fig, "Work-Life Balance Rating vs Attrition")

def plot_job_satisfaction(df):
    counts = df.groupby(["JobSatisfaction", "Attrition"]).size().reset_index(name="Count")
    fig = px.bar(
        counts,
        x="JobSatisfaction",
        y="Count",
        color="Attrition",
        barmode="group",
        color_discrete_map={"Yes": RED, "No": BLUE}
    )
    return apply_theme(fig, "Job Satisfaction Levels")

def plot_age_distribution(df):
    fig = px.histogram(
        df,
        x="Age",
        color="Attrition",
        nbins=25,
        barmode="overlay",
        color_discrete_map={"Yes": RED, "No": CYAN},
        opacity=0.7
    )
    return apply_theme(fig, "Employee Age Distribution")

def plot_income_distribution(df):
    fig = px.histogram(
        df,
        x="MonthlyIncome",
        color="Attrition",
        nbins=30,
        barmode="overlay",
        color_discrete_map={"Yes": RED, "No": GREEN},
        opacity=0.7
    )
    return apply_theme(fig, "Monthly Income Distribution ($)")

def plot_income_by_dept(df):
    fig = px.box(
        df,
        x="Department",
        y="MonthlyIncome",
        color="Department",
        color_discrete_sequence=[CYAN, BLUE, PURPLE]
    )
    fig.update_layout(showlegend=False)
    return apply_theme(fig, "Monthly Income Spread by Department")

def plot_years_at_company(df):
    fig = px.histogram(
        df,
        x="YearsAtCompany",
        color="Attrition",
        nbins=20,
        barmode="overlay",
        color_discrete_map={"Yes": RED, "No": CYAN},
        opacity=0.75
    )
    return apply_theme(fig, "Tenure (Years at Company)")

def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include="number")
    corr = numeric_df.corr().round(2)
    fig = px.imshow(
        corr,
        text_auto=False,
        aspect="auto",
        color_continuous_scale="Viridis"
    )
    fig.update_coloraxes(showscale=True)
    return apply_theme(fig, "Numerical Correlation Heatmap")

def plot_income_vs_attrition_box(df):
    fig = px.box(
        df,
        x="Attrition",
        y="MonthlyIncome",
        color="Attrition",
        color_discrete_map={"Yes": RED, "No": GREEN},
        points="all"
    )
    return apply_theme(fig, "Monthly Income by Attrition Status")
