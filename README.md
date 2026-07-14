# Credit Risk Scorecard & Probability of Default (PD) Prediction

> An end-to-end Credit Risk Analytics project that develops an interpretable Probability of Default (PD) model using Logistic Regression, Weight of Evidence (WOE), Information Value (IV), and Credit Scorecard techniques to support data-driven lending decisions.

---

## Project Overview

Financial institutions process thousands of loan applications every day. Incorrect lending decisions can lead to significant financial losses due to borrower defaults. Therefore, accurately estimating the probability that a borrower will default is one of the most important tasks in credit risk management.

This project simulates a real-world credit underwriting workflow by developing an interpretable credit risk scorecard capable of estimating the **Probability of Default (PD)** for loan applicants. The project emphasizes explainability, regulatory-friendly modelling practices, and business interpretability over purely maximizing predictive performance.

---

## Business Problem

The objective is to assist financial institutions in answering the following questions:

- Which loan applicants are likely to default?
- Which customer characteristics contribute most to credit risk?
- How can borrowers be segmented into Low, Medium, and High Risk groups?
- How can lending decisions become more consistent using data-driven credit scoring?

The final solution enables banks to:

- Estimate Probability of Default (PD)
- Generate interpretable credit scores
- Identify high-risk borrowers
- Support loan approval and rejection decisions
- Reduce expected credit losses

---

## Project Objectives

- Perform comprehensive exploratory data analysis.
- Handle missing values and outliers.
- Engineer meaningful borrower risk features.
- Perform feature selection using Weight of Evidence (WOE) and Information Value (IV).
- Compare multiple machine learning models.
- Develop an interpretable Logistic Regression-based credit scorecard.
- Predict Probability of Default (PD).
- Segment borrowers into risk categories.
- Deploy the model using Streamlit.

---

## Dataset

The project uses the **German Credit Dataset**, containing demographic, financial, and credit history information for loan applicants.

Example attributes include:

- Age
- Annual Income
- Employment Status
- Loan Amount
- Loan Duration
- Existing Credits
- Credit Utilization
- Payment History
- Savings
- Housing Status

Target Variable:

- Default (1)
- Non-Default (0)

---

# Project Workflow

```
Business Understanding
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
WOE & IV Transformation
        │
        ▼
Model Comparison
        │
        ▼
Logistic Regression Scorecard
        │
        ▼
Probability of Default
        │
        ▼
Credit Score Generation
        │
        ▼
Risk Segmentation
        │
        ▼
Streamlit Deployment
```

---

# Feature Engineering

Several borrower risk indicators were engineered to improve predictive performance.

Examples include:

- Debt-to-Income Ratio
- Credit Utilization
- Loan-to-Income Ratio
- Delinquency Ratio
- Average Days Past Due (DPD)
- Credit History Length
- Existing Credit Burden

These engineered variables better represent borrower financial behaviour than the original raw variables.

---

# Feature Selection

Feature selection was performed using industry-standard techniques commonly adopted in credit risk modelling.

Methods used:

- Weight of Evidence (WOE)
- Information Value (IV)
- Variance Inflation Factor (VIF)
- Correlation Analysis

This ensures the final model remains both predictive and interpretable.

---

# Model Comparison

Multiple supervised learning algorithms were trained and evaluated.

Models compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Evaluation metrics included:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- KS Statistic

Although ensemble methods achieved competitive performance, **Logistic Regression** was selected because of its transparency, explainability, and widespread adoption in regulated banking environments.

---

# Credit Scorecard Development

The final Logistic Regression model was transformed into an interpretable credit scorecard capable of assigning a numerical credit score to each applicant.

Each borrower receives:

- Probability of Default (PD)
- Credit Score
- Risk Category
- Lending Recommendation

Risk Categories:

| Credit Score | Risk Level |
|--------------|------------|
| High Score | Low Risk |
| Medium Score | Medium Risk |
| Low Score | High Risk |

---

# Model Evaluation

The final model was evaluated using:

- ROC-AUC
- Precision
- Recall
- F1 Score
- KS Statistic
- Confusion Matrix
- ROC Curve

These metrics demonstrate the model's ability to distinguish between defaulting and non-defaulting borrowers.

---

# Streamlit Application

An interactive Streamlit web application was developed that allows users to:

- Enter applicant information
- Predict Probability of Default
- Generate Credit Score
- Display Borrower Risk Category
- Provide Loan Approval Recommendation

---

# Project Structure

```
Credit-Risk-Analysis/

│
├── artifacts/
├── data/
├── notebooks/
├── models/
├── helper/
├── app/
├── screenshots/
├── requirements.txt
├── README.md
└── streamlit_app.py
```

---

# Technologies Used

Programming

- Python

Machine Learning

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Scikit-Learn

Data Processing

- Pandas
- NumPy

Visualization

- Matplotlib
- Seaborn

Deployment

- Streamlit

Feature Engineering

- Weight of Evidence (WOE)
- Information Value (IV)
- VIF

Version Control

- Git
- GitHub

---

# Future Improvements

The project can be extended by incorporating:

- SQL-based portfolio analysis
- Power BI Credit Risk Dashboard
- Expected Loss (PD × LGD × EAD)
- SHAP Explainability
- Population Stability Index (PSI)
- Model Monitoring
- Basel II / Basel III validation metrics

---

# Business Impact

This project demonstrates an end-to-end credit risk modelling workflow commonly used within banking and financial institutions.

It highlights practical applications of:

- Credit Risk Analytics
- Statistical Modelling
- Probability of Default (PD)
- Credit Scorecard Development
- Explainable Machine Learning
- Data-Driven Lending Decisions

The workflow closely aligns with the responsibilities of a Credit Risk Analyst involved in retail lending, underwriting, and portfolio risk management.

---

# Author

**Abhishek Rawat**

Master's in Operational Research

Python | SQL | Power BI | Machine Learning | Credit Risk Analytics
