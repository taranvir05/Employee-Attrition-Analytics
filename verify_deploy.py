"""
verify_deploy.py - PulseHR Deployment Readiness Verification
Checks SHAP images, no glow-divider HTML, data values, prediction pipeline
"""
import os, glob, sys
sys.path.insert(0, ".")

pass_count = 0
fail_count = 0

def chk(label, condition, detail=""):
    global pass_count, fail_count
    if condition:
        pass_count += 1
        print(f"  [PASS] {label}" + (f" - {detail}" if detail else ""))
    else:
        fail_count += 1
        print(f"  [FAIL] {label}" + (f" - {detail}" if detail else ""))

print("=" * 60)
print("  PULSEHR DEPLOYMENT READINESS REPORT")
print("=" * 60)

# 1. SHAP images
print()
print("[1] SHAP Image Files")
required_images = [
    "images/shap_summary.png",
    "images/shap_bar.png",
    "images/waterfall_high_risk.png",
    "images/waterfall_borderline.png",
    "images/waterfall_low_risk.png",
]
for img in required_images:
    exists = os.path.exists(img)
    size = os.path.getsize(img) if exists else 0
    chk(img, exists, str(size) + " bytes" if exists else "MISSING")

# 2. No glow-divider in page files
print()
print("[2] No glow-divider HTML in Page Files")
page_files = list(glob.glob("pages/*.py")) + ["app.py"]
for fpath in page_files:
    with open(fpath, encoding="utf-8") as f:
        content = f.read()
    # Only flag actual HTML usage, not the CSS class definition in style.py
    has_div = '<div class="glow-divider">' in content or "glow-divider\"></div>" in content
    chk(fpath, not has_div, "Clean" if not has_div else "glow-divider HTML found!")

# 3. Model artifact files
print()
print("[3] Model Artifact Files")
artifacts = ["models/best_model.pkl", "models/scaler.pkl", "models/feature_names.pkl", "models/model_metrics.json"]
for art in artifacts:
    exists = os.path.exists(art)
    chk(art, exists)

# 4. Model loader
print()
print("[4] Model Loader Verification")
try:
    from utils.model_loader import get_model_assets, get_model_display_name, get_model_metrics, get_top_model_drivers
    model, scaler, feature_names = get_model_assets()
    chk("Model loaded", model is not None, type(model).__name__)
    chk("Scaler loaded", scaler is not None)
    chk("Feature names loaded", isinstance(feature_names, list) and len(feature_names) > 0, str(len(feature_names)) + " features")
    
    mname = get_model_display_name()
    chk("Display name", mname == "Logistic Regression", mname)
    
    metrics = get_model_metrics()
    tm = metrics.get("test_metrics", {})
    chk("Accuracy = 87.76%", abs(tm.get("accuracy", 0) - 87.76) < 0.01, str(tm.get("accuracy")))
    chk("Precision = 73.91%", abs(tm.get("precision", 0) - 73.91) < 0.01, str(tm.get("precision")))
    chk("Recall = 36.17%", abs(tm.get("recall", 0) - 36.17) < 0.01, str(tm.get("recall")))
    chk("F1-Score = 48.57%", abs(tm.get("f1_score", 0) - 48.57) < 0.01, str(tm.get("f1_score")))
    chk("ROC-AUC = 83.26", abs(tm.get("roc_auc", 0) - 83.26) < 0.01, str(tm.get("roc_auc")))

    drivers = get_top_model_drivers()
    chk("Top attrition driver computed", bool(drivers.get("top_attrition_driver")), drivers.get("top_attrition_driver"))
    chk("Top retention driver computed", bool(drivers.get("top_retention_driver")), drivers.get("top_retention_driver"))
except Exception as e:
    chk("Model loader import", False, str(e))

# 5. Data values cross-check
print()
print("[5] Dataset Values Cross-Check (Notebook 05)")
try:
    import pandas as pd
    df = pd.read_csv("data/employee_attrition_feature_engineered.csv")
    chk("Total records = 1470", len(df) == 1470, str(len(df)))
    attr_rate = (df["Attrition"] == "Yes").mean() * 100
    chk("Attrition rate ~16.12%", abs(attr_rate - 16.12) < 0.1, f"{attr_rate:.2f}%")
    avg_inc = df["MonthlyIncome"].mean()
    chk("Avg income ~6503", abs(avg_inc - 6503) < 50, f"${avg_inc:.0f}")
    chk("Departments = 3", df["Department"].nunique() == 3, str(df["Department"].nunique()))
    ot_yes = (df[df["OverTime"] == "Yes"]["Attrition"] == "Yes").mean() * 100
    ot_no = (df[df["OverTime"] == "No"]["Attrition"] == "Yes").mean() * 100
    chk("OT attrition > non-OT attrition", ot_yes > ot_no, f"{ot_yes:.1f}% vs {ot_no:.1f}%")
    top_dept = df[df["Attrition"] == "Yes"]["Department"].value_counts().idxmax()
    chk("Top attrition dept = R&D", "Research" in top_dept, top_dept)
    top_role = df[df["Attrition"] == "Yes"]["JobRole"].value_counts().idxmax()
    chk("Top attrition role = Lab Technician", "Laboratory" in top_role, top_role)
except Exception as e:
    chk("Dataset cross-check", False, str(e))

# 6. Prediction pipeline end-to-end
print()
print("[6] End-to-End Prediction Pipeline")
try:
    import pandas as pd
    import numpy as np
    model, scaler, feature_names = get_model_assets()
    input_df = pd.DataFrame({
        "Age": [30], "DailyRate": [802], "HourlyRate": [66], "MonthlyRate": [14235],
        "Gender": ["Male"], "MaritalStatus": ["Single"], "Education": [3],
        "EducationField": ["Life Sciences"], "Department": ["Sales"],
        "JobRole": ["Sales Executive"], "JobLevel": [2], "JobInvolvement": [3],
        "BusinessTravel": ["Travel_Rarely"], "OverTime": ["Yes"],
        "PerformanceRating": [3], "JobSatisfaction": [2], "EnvironmentSatisfaction": [2],
        "RelationshipSatisfaction": [2], "WorkLifeBalance": [2], "MonthlyIncome": [3500],
        "StockOptionLevel": [0], "PercentSalaryHike": [12], "TrainingTimesLastYear": [2],
        "TotalWorkingYears": [5], "YearsAtCompany": [3], "NumCompaniesWorked": [2],
        "YearsSinceLastPromotion": [2], "YearsInCurrentRole": [2],
        "YearsWithCurrManager": [2], "DistanceFromHome": [10]
    })
    input_df["IncomeGroup"] = pd.cut(input_df["MonthlyIncome"], bins=[1009,2911,4919,8379,19999], labels=["Low","Medium","High","Very High"], include_lowest=True)
    input_df["ExperienceGroup"] = pd.cut(input_df["TotalWorkingYears"], bins=[-1,5,10,20,40], labels=["Early Career","Mid Career","Senior","Highly Experienced"])
    input_df["PromotionDelay"] = pd.cut(input_df["YearsSinceLastPromotion"], bins=[-1,1,3,6,20], labels=["Recently Promoted","Moderate Delay","Long Delay","Very Long Delay"])
    input_df["DistanceCategory"] = pd.cut(input_df["DistanceFromHome"], bins=[-1,5,15,30], labels=["Near","Moderate","Far"])
    input_df["OverallSatisfaction"] = input_df["EnvironmentSatisfaction"] + input_df["JobSatisfaction"] + input_df["RelationshipSatisfaction"] + input_df["WorkLifeBalance"]
    input_df["TenureGroup"] = pd.cut(input_df["YearsAtCompany"], bins=[-1,2,5,10,40], labels=["New","Junior","Experienced","Veteran"])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)
    numerical_columns = ["Age","DailyRate","DistanceFromHome","Education","EnvironmentSatisfaction","HourlyRate","JobInvolvement","JobLevel","JobSatisfaction","MonthlyIncome","MonthlyRate","NumCompaniesWorked","PercentSalaryHike","PerformanceRating","RelationshipSatisfaction","StockOptionLevel","TotalWorkingYears","TrainingTimesLastYear","WorkLifeBalance","YearsAtCompany","YearsInCurrentRole","YearsSinceLastPromotion","YearsWithCurrManager","OverallSatisfaction"]
    input_scaled = input_encoded.copy()
    input_scaled[numerical_columns] = scaler.transform(input_scaled[numerical_columns])
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]
    chk("High-risk profile predicts attrition=1", pred == 1, "pred=" + str(pred))
    chk("High-risk probability > 50%", prob > 0.5, f"{prob*100:.1f}%")
    chk("Input shape matches feature list", input_scaled.shape[1] == len(feature_names), str(input_scaled.shape))
except Exception as e:
    chk("Prediction pipeline", False, str(e))

print()
print("=" * 60)
print(f"  RESULT: {pass_count} PASSED / {fail_count} FAILED")
print("=" * 60)
if fail_count == 0:
    print("  DEPLOYMENT READY")
else:
    print("  ISSUES NEED TO BE FIXED BEFORE DEPLOYMENT")
