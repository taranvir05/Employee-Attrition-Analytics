"""
utils/shap_utils.py
-------------------
Single source of truth for ALL SHAP-related computation in PulseHR.

Public API
----------
get_shap_results()      -> dict with shap_values, feature_names, explainer_name,
                           top_attrition_driver, top_retention_driver,
                           top_n_attrition, top_n_retention, mean_abs_shap
prettify_feature(name)  -> human-readable label string
"""

import os
import numpy as np
import pandas as pd
import streamlit as st
import joblib
import shap

# ── Artifact paths ───────────────────────────────────────────
MODEL_PATH   = "models/best_model.pkl"
FEATURE_PATH = "models/feature_names.pkl"
X_TEST_PATH  = "data/X_test_scaled.csv"

TOP_N = 5

# ─────────────────────────────────────────────────────────────
# Human-Readable Feature Name Mapping
# ─────────────────────────────────────────────────────────────
_FEATURE_LABELS = {
    # Numeric columns
    "Age":                                "Age",
    "DailyRate":                          "Daily Rate",
    "DistanceFromHome":                   "Distance From Home",
    "Education":                          "Education Level",
    "EnvironmentSatisfaction":            "Environment Satisfaction",
    "HourlyRate":                         "Hourly Rate",
    "JobInvolvement":                     "Job Involvement",
    "JobLevel":                           "Job Level",
    "JobSatisfaction":                    "Job Satisfaction",
    "MonthlyIncome":                      "Monthly Income",
    "MonthlyRate":                        "Monthly Rate",
    "NumCompaniesWorked":                 "Companies Worked For",
    "PercentSalaryHike":                  "Salary Hike %",
    "PerformanceRating":                  "Performance Rating",
    "RelationshipSatisfaction":           "Relationship Satisfaction",
    "StockOptionLevel":                   "Stock Option Level",
    "TotalWorkingYears":                  "Total Working Years",
    "TrainingTimesLastYear":              "Training Frequency",
    "WorkLifeBalance":                    "Work-Life Balance",
    "YearsAtCompany":                     "Years at Company",
    "YearsInCurrentRole":                 "Years in Current Role",
    "YearsSinceLastPromotion":            "Years Since Promotion",
    "YearsWithCurrManager":               "Years with Manager",
    "OverallSatisfaction":                "Overall Satisfaction Score",
    # BusinessTravel
    "BusinessTravel_Travel_Frequently":   "Frequent Business Travel",
    "BusinessTravel_Travel_Rarely":       "Occasional Business Travel",
    "BusinessTravel_Non-Travel":          "Non-Travel",
    # Department
    "Department_Research & Development":  "Research & Development Dept",
    "Department_Sales":                   "Sales Department",
    "Department_Human Resources":         "Human Resources Dept",
    # EducationField
    "EducationField_Life Sciences":       "Life Sciences Education",
    "EducationField_Marketing":           "Marketing Education",
    "EducationField_Medical":             "Medical Education",
    "EducationField_Other":               "Other Education",
    "EducationField_Technical Degree":    "Technical Degree",
    "EducationField_Human Resources":     "HR Education",
    # Gender
    "Gender_Male":                        "Gender: Male",
    "Gender_Female":                      "Gender: Female",
    # JobRole
    "JobRole_Human Resources":            "Human Resources Role",
    "JobRole_Laboratory Technician":      "Laboratory Technician",
    "JobRole_Manager":                    "Manager",
    "JobRole_Manufacturing Director":     "Manufacturing Director",
    "JobRole_Research Director":          "Research Director",
    "JobRole_Research Scientist":         "Research Scientist",
    "JobRole_Sales Executive":            "Sales Executive",
    "JobRole_Sales Representative":       "Sales Representative",
    "JobRole_Healthcare Representative":  "Healthcare Representative",
    # MaritalStatus
    "MaritalStatus_Single":               "Marital Status: Single",
    "MaritalStatus_Married":              "Marital Status: Married",
    "MaritalStatus_Divorced":             "Marital Status: Divorced",
    # OverTime
    "OverTime_Yes":                       "Overtime (Yes)",
    "OverTime_No":                        "Overtime (No)",
    # IncomeGroup
    "IncomeGroup_Low":                    "Income Group: Low",
    "IncomeGroup_Medium":                 "Income Group: Medium",
    "IncomeGroup_High":                   "Income Group: High",
    "IncomeGroup_Very High":              "Income Group: Very High",
    # ExperienceGroup
    "ExperienceGroup_Early Career":       "Experience: Early Career",
    "ExperienceGroup_Mid Career":         "Experience: Mid Career",
    "ExperienceGroup_Senior":             "Experience: Senior",
    "ExperienceGroup_Highly Experienced": "Experience: Highly Experienced",
    # PromotionDelay
    "PromotionDelay_Recently Promoted":   "Promotion: Recently Promoted",
    "PromotionDelay_Moderate Delay":      "Promotion: Moderate Delay",
    "PromotionDelay_Long Delay":          "Promotion: Long Delay",
    "PromotionDelay_Very Long Delay":     "Promotion: Very Long Delay",
    # DistanceCategory
    "DistanceCategory_Near":              "Distance: Near",
    "DistanceCategory_Moderate":          "Distance: Moderate",
    "DistanceCategory_Far":               "Distance: Far",
    # TenureGroup
    "TenureGroup_New":                    "Tenure: New",
    "TenureGroup_Junior":                 "Tenure: Junior",
    "TenureGroup_Experienced":            "Tenure: Experienced",
    "TenureGroup_Veteran":                "Tenure: Veteran",
}


def prettify_feature(name: str) -> str:
    """Convert a raw feature name to a human-readable label."""
    if name in _FEATURE_LABELS:
        return _FEATURE_LABELS[name]
    return name.replace("_", " ").strip().title()


def _detect_explainer_name(model) -> str:
    """Detect SHAP explainer type from model class."""
    cls = type(model).__name__
    tree_types = {"RandomForestClassifier", "DecisionTreeClassifier",
                  "GradientBoostingClassifier", "XGBClassifier",
                  "LGBMClassifier", "ExtraTreesClassifier"}
    if cls in tree_types or any(k in cls for k in ("Forest", "Tree", "Boost", "XGB", "LGBM")):
        return "TreeExplainer"
    return "LinearExplainer"


@st.cache_resource(show_spinner=False)
def _compute_shap(model_mtime: float, feature_mtime: float):
    model         = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURE_PATH)
    X_test        = pd.read_csv(X_TEST_PATH)
    X_test        = X_test.reindex(columns=feature_names, fill_value=0)

    explainer   = shap.LinearExplainer(model, X_test)
    shap_values = explainer.shap_values(X_test)

    return shap_values, feature_names, explainer, model


def get_shap_results(top_n: int = TOP_N) -> dict:
    model_mtime   = os.path.getmtime(MODEL_PATH)   if os.path.exists(MODEL_PATH)   else 0.0
    feature_mtime = os.path.getmtime(FEATURE_PATH) if os.path.exists(FEATURE_PATH) else 0.0

    shap_values, feature_names, explainer, model = _compute_shap(model_mtime, feature_mtime)

    mean_abs    = np.abs(shap_values).mean(axis=0)
    mean_signed = shap_values.mean(axis=0)

    importance_df = pd.DataFrame({
        "feature":     feature_names,
        "mean_abs":    mean_abs,
        "mean_signed": mean_signed,
    }).sort_values("mean_abs", ascending=False)

    top_attr_driver = prettify_feature(importance_df.iloc[0]["feature"])

    retention_df   = importance_df.sort_values("mean_signed", ascending=True)
    top_ret_driver = prettify_feature(retention_df.iloc[0]["feature"])

    top_n_attr = [
        {
            "feature":       row["feature"],
            "pretty":        prettify_feature(row["feature"]),
            "mean_abs_shap": float(row["mean_abs"]),
        }
        for _, row in importance_df.head(top_n).iterrows()
    ]

    top_n_ret = [
        {
            "feature":          row["feature"],
            "pretty":           prettify_feature(row["feature"]),
            "mean_signed_shap": float(row["mean_signed"]),
        }
        for _, row in retention_df.head(top_n).iterrows()
    ]

    return {
        "shap_values":          shap_values,
        "feature_names":        feature_names,
        "explainer":            explainer,
        "explainer_name":       _detect_explainer_name(model),
        "mean_abs_shap":        importance_df.set_index("feature")["mean_abs"],
        "top_attrition_driver": top_attr_driver,
        "top_retention_driver": top_ret_driver,
        "top_n_attrition":      top_n_attr,
        "top_n_retention":      top_n_ret,
        "feature_count":        len(feature_names),
    }
