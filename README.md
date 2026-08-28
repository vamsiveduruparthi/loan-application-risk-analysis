# Loan Application & Risk Analysis Dashboard

## 📊 Project Overview

An interactive Power BI dashboard developed to analyze loan application performance, approval trends, customer segments, and lending patterns.

The project transforms loan application data into meaningful KPIs and interactive visualizations to support data-driven analysis and business decision-making.

---

## 🎯 Project Objective

The objective of this project is to analyze loan application data and identify patterns related to:

- Loan application volume
- Approval and rejection performance
- Regional application trends
- Employment segments
- Loan purposes
- Credit categories
- Loan amounts
- Annual income
- Interest rates
- Debt-to-Income (DTI) ratio
- Loan terms

---

## 🛠️ Tools & Technologies

- **Power BI Desktop**
- **DAX**
- **Data Cleaning & Transformation**
- **Data Visualization**
- **Business Intelligence**

---

## 📌 Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Applications | 5,000 |
| Approved Applications | 931 |
| Rejected Applications | 4,069 |
| Approval Rate | 18.62% |
| Total Loan Amount | 3.06bn |
| Average Loan Amount | 611.16K |
| Average Credit Score | 682.37 |
| Average Annual Income | 637.46K |
| Average Interest Rate | 17.96 |
| Average DTI Ratio | 0.75 |

---

# 📈 Dashboard

## Page 1 — Loan Application Overview

The overview page provides a high-level view of loan application performance.

### Analysis included:

- Total loan applications
- Approved vs. rejected applications
- Approval rate
- Total loan amount
- Applications by region
- Applications by employment type
- Loan amount by purpose
- Average loan amount by region
- Average loan amount by employment type

### Interactive Filters

Users can dynamically filter the dashboard using:

- Region
- Employment
- Loan Purpose
- Loan Status

### Dashboard Preview

![Loan Application Overview](screenshots/Loan_Application_Risk_Analysis.jpg)

---

## Page 2 — Loan Analysis

The loan analysis page provides deeper insights into customer and loan characteristics.

### Analysis included:

- Applications by credit category
- Approval rate by credit category
- Average loan amount by credit category
- Average interest rate by credit category
- Average DTI ratio by loan status
- Average annual income by loan status
- Applications by loan term
- Approval rate by employment
- Average loan amount by loan status

### Interactive Filters

- Credit Category
- Employment
- Loan Status

### Dashboard Preview

![Loan Analysis](screenshots/Loan_Application_Risk_Analysis.jpg)

---

# 🔍 Key Insights

The analysis highlights several patterns within the loan portfolio:

- The majority of applications fall within the **Good** and **Fair** credit categories.
- **Excellent** credit customers show the strongest approval rate among the credit categories.
- Salaried applicants represent the largest employment segment by application volume.
- Vehicle and Personal loans account for some of the highest loan amounts by purpose.
- Approved and rejected applications show differences in average income and DTI characteristics.
- Approval performance varies across employment and credit categories.
- Regional analysis helps identify differences in application volume and average loan amounts.

---

# 💡 Business Value

The dashboard can help stakeholders:

- Monitor loan application and approval performance
- Identify high-performing customer segments
- Compare regional lending activity
- Understand loan demand by purpose
- Analyze credit-related approval patterns
- Evaluate income, interest rate and DTI trends
- Support data-driven lending decisions

---

# 📂 Project Structure

```text
loan-application-risk-analysis/
│
├── PowerBI/
│   └── Loan_Application_Risk_Analysis.pbix
│
├── screenshots/
│   ├── Loan_Application_Risk_Analysis.jpg
│   └── Loan_Application_Risk_Analysis2.jpg
│
└── README.md
