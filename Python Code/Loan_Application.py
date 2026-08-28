from pathlib import Path
import pandas as pd

csv_path = "/mnt/data/Banking_Loan_Risk_Analysis_Final.csv"
df = pd.read_csv(csv_path)

# Build a single GitHub-friendly Markdown file containing both Python and SQL sections.
content = r"""# Loan Application & Risk Analysis — Python + SQL

This file contains the Python exploratory analysis and SQL analysis used for the
Loan Application & Risk Analysis project.

**Dataset:** `Banking_Loan_Risk_Analysis_Final.csv`  
**Rows:** 5,000  
**Columns:** 17

---

# Part 1 — Python Analysis

The Python section uses pandas for data inspection, validation, cleaning checks,
KPI calculation, segmentation analysis, and exploratory analysis.

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("Banking_Loan_Risk_Analysis_Final.csv")

# -----------------------------
# 1. Basic inspection
# -----------------------------
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


# -----------------------------
# 2. Data preparation
# -----------------------------
df["Application_Date"] = pd.to_datetime(
    df["Application_Date"], errors="coerce"
)

numeric_columns = [
    "Age",
    "Annual_Income",
    "Credit_Score",
    "Loan_Amount",
    "Loan_Term_Months",
    "DTI_Ratio",
    "Interest_Rate"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Standardize text fields
text_columns = [
    "Employment",
    "Property_Area",
    "Region",
    "Loan_Purpose",
    "Loan_Status",
    "Credit_Category"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# Check data after preparation
print("\nMissing values after preparation:")
print(df.isnull().sum())


# -----------------------------
# 3. Overall KPIs
# -----------------------------
total_applications = len(df)

approved_applications = (
    df["Loan_Status"].eq("Approved").sum()
)

rejected_applications = (
    df["Loan_Status"].eq("Rejected").sum()
)

approval_rate = (
    approved_applications / total_applications * 100
    if total_applications else 0
)

total_loan_amount = df["Loan_Amount"].sum()
average_loan_amount = df["Loan_Amount"].mean()
average_credit_score = df["Credit_Score"].mean()
average_income = df["Annual_Income"].mean()
average_interest_rate = df["Interest_Rate"].mean()
average_dti = df["DTI_Ratio"].mean()

print("\n--- Overall KPIs ---")
print("Total Applications:", total_applications)
print("Approved Applications:", approved_applications)
print("Rejected Applications:", rejected_applications)
print("Approval Rate:", round(approval_rate, 2), "%")
print("Total Loan Amount:", round(total_loan_amount, 2))
print("Average Loan Amount:", round(average_loan_amount, 2))
print("Average Credit Score:", round(average_credit_score, 2))
print("Average Annual Income:", round(average_income, 2))
print("Average Interest Rate:", round(average_interest_rate, 2))
print("Average DTI Ratio:", round(average_dti, 2))


# -----------------------------
# 4. Applications by Region
# -----------------------------
applications_by_region = (
    df.groupby("Region")
      .size()
      .reset_index(name="Applications")
      .sort_values("Applications", ascending=False)
)

print("\n--- Applications by Region ---")
print(applications_by_region)


# -----------------------------
# 5. Applications by Employment
# -----------------------------
applications_by_employment = (
    df.groupby("Employment")
      .size()
      .reset_index(name="Applications")
      .sort_values("Applications", ascending=False)
)

print("\n--- Applications by Employment ---")
print(applications_by_employment)


# -----------------------------
# 6. Loan amount by purpose
# -----------------------------
loan_amount_by_purpose = (
    df.groupby("Loan_Purpose")["Loan_Amount"]
      .sum()
      .reset_index(name="Total_Loan_Amount")
      .sort_values("Total_Loan_Amount", ascending=False)
)

print("\n--- Loan Amount by Purpose ---")
print(loan_amount_by_purpose)


# -----------------------------
# 7. Average loan amount by region
# -----------------------------
avg_loan_by_region = (
    df.groupby("Region")["Loan_Amount"]
      .mean()
      .reset_index(name="Average_Loan_Amount")
      .sort_values("Average_Loan_Amount", ascending=False)
)

print("\n--- Average Loan Amount by Region ---")
print(avg_loan_by_region)


# -----------------------------
# 8. Average loan amount by employment
# -----------------------------
avg_loan_by_employment = (
    df.groupby("Employment")["Loan_Amount"]
      .mean()
      .reset_index(name="Average_Loan_Amount")
      .sort_values("Average_Loan_Amount", ascending=False)
)

print("\n--- Average Loan Amount by Employment ---")
print(avg_loan_by_employment)


# -----------------------------
# 9. Applications by credit category
# -----------------------------
applications_by_credit = (
    df.groupby("Credit_Category")
      .size()
      .reset_index(name="Applications")
      .sort_values("Applications", ascending=False)
)

print("\n--- Applications by Credit Category ---")
print(applications_by_credit)


# -----------------------------
# 10. Approval rate by credit category
# -----------------------------
credit_approval = (
    df.assign(
        Approved=df["Loan_Status"].eq("Approved").astype(int)
    )
    .groupby("Credit_Category")
    .agg(
        Applications=("Loan_ID", "count"),
        Approved_Applications=("Approved", "sum")
    )
)

credit_approval["Approval_Rate"] = (
    credit_approval["Approved_Applications"]
    / credit_approval["Applications"] * 100
)

credit_approval = (
    credit_approval.reset_index()
                   .sort_values("Approval_Rate", ascending=False)
)

print("\n--- Approval Rate by Credit Category ---")
print(credit_approval)


# -----------------------------
# 11. Average loan amount by credit category
# -----------------------------
avg_loan_by_credit = (
    df.groupby("Credit_Category")["Loan_Amount"]
      .mean()
      .reset_index(name="Average_Loan_Amount")
      .sort_values("Average_Loan_Amount", ascending=False)
)

print("\n--- Average Loan Amount by Credit Category ---")
print(avg_loan_by_credit)


# -----------------------------
# 12. Average interest rate by credit category
# -----------------------------
avg_interest_by_credit = (
    df.groupby("Credit_Category")["Interest_Rate"]
      .mean()
      .reset_index(name="Average_Interest_Rate")
      .sort_values("Average_Interest_Rate", ascending=False)
)

print("\n--- Average Interest Rate by Credit Category ---")
print(avg_interest_by_credit)


# -----------------------------
# 13. DTI and income by loan status
# -----------------------------
status_analysis = (
    df.groupby("Loan_Status")
      .agg(
          Average_DTI_Ratio=("DTI_Ratio", "mean"),
          Average_Annual_Income=("Annual_Income", "mean"),
          Average_Loan_Amount=("Loan_Amount", "mean"),
          Applications=("Loan_ID", "count")
      )
      .reset_index()
)

print("\n--- Analysis by Loan Status ---")
print(status_analysis)


# -----------------------------
# 14. Applications by loan term
# -----------------------------
applications_by_term = (
    df.groupby("Loan_Term_Months")
      .size()
      .reset_index(name="Applications")
      .sort_values("Loan_Term_Months")
)

print("\n--- Applications by Loan Term ---")
print(applications_by_term)


# -----------------------------
# 15. Approval rate by employment
# -----------------------------
employment_approval = (
    df.assign(
        Approved=df["Loan_Status"].eq("Approved").astype(int)
    )
    .groupby("Employment")
    .agg(
        Applications=("Loan_ID", "count"),
        Approved_Applications=("Approved", "sum")
    )
)

employment_approval["Approval_Rate"] = (
    employment_approval["Approved_Applications"]
    / employment_approval["Applications"] * 100
)

employment_approval = (
    employment_approval.reset_index()
                       .sort_values("Approval_Rate", ascending=False)
)

print("\n--- Approval Rate by Employment ---")
print(employment_approval)


# -----------------------------
# 16. Basic descriptive statistics
# -----------------------------
print("\n--- Descriptive Statistics ---")
print(
    df[
        [
            "Age",
            "Annual_Income",
            "Credit_Score",
            "Loan_Amount",
            "Loan_Term_Months",
            "DTI_Ratio",
            "Interest_Rate"
        ]
    ].describe()
)
