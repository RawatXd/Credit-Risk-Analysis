# 📊 Credit Risk Modelling

A machine learning web application that predicts loan default probability and generates a credit score (300–900) for applicants in real time — built with Logistic Regression, feature engineering on 50,000 customer records, and deployed via Streamlit.

---

## 🔍 Problem Statement

Financial institutions need an automated, explainable way to assess borrower risk before approving loans. Manual credit evaluation is slow, inconsistent, and prone to bias. This project builds a production-style credit risk pipeline: from raw multi-source data → feature engineering → model training → live scoring via a web UI.

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.x |
| ML Model | Scikit-learn (Logistic Regression) |
| Data Processing | Pandas, NumPy |
| Feature Selection | WoE / IV, VIF Analysis |
| Scaling | MinMaxScaler |
| Model Persistence | Joblib |
| Web App | Streamlit |
| Notebooks | Jupyter |

---

## 📁 Project Structure

```
credit-risk-modelling/
│
├── artifacts/
│   └── model_data.joblib          # Trained model + scaler + feature list
│
├── dataset/
│   ├── customers.csv              # 50,000 customer demographic records
│   ├── loans.csv                  # 50,000 loan application records
│   └── bureau_data.csv            # 50,000 credit bureau records
│
├── credit_risk_model.ipynb        # End-to-end ML pipeline notebook
├── prediction_helper.py           # Feature preparation + scoring logic
├── main.py                        # Streamlit app entry point
└── README.md
```

---

## ⚙️ ML Pipeline Overview

### 1. Data Ingestion & Merging
Three datasets — `customers`, `loans`, and `bureau_data` — are joined on `cust_id` to create a unified 50,000-row training dataset.

### 2. Train-Test Split (Pre-EDA)
A stratified 75/25 split is performed **before** any EDA or feature engineering to prevent data leakage.

### 3. Data Cleaning
- Missing values in `residence_type` imputed with mode
- Business-rule-based outlier removal (e.g., `processing_fee / loan_amount > 3%` flagged as invalid)

### 4. Feature Engineering
- `loan_to_income` ratio derived from `loan_amount` and `income`
- `avg_dpd_per_delinquency` and `delinquency_ratio` computed from bureau fields
- Categorical features encoded via One-Hot Encoding

### 5. Feature Selection
- **VIF Analysis** to drop multicollinear features (`sanction_amount`, `processing_fee`, `gst`, `net_disbursement`, `principal_outstanding`)
- **WoE / Information Value (IV)** to retain only features with IV > 0.02

### 6. Model Training & Selection
Three models benchmarked — Logistic Regression, Random Forest, XGBoost. Logistic Regression selected for its comparable AUC performance and superior interpretability for credit scoring use cases. Final model tuned via `RandomizedSearchCV`.

### 7. Credit Score Generation
Default probability → credit score mapped to [300, 900] range using:

```
credit_score = 300 + (1 - P_default) × 600
```

| Score Range | Rating |
|---|---|
| 300 – 499 | Poor |
| 500 – 649 | Average |
| 650 – 749 | Good |
| 750 – 900 | Excellent |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/credit-risk-modelling.git
cd credit-risk-modelling
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> **requirements.txt** (create this file):
> ```
> streamlit
> scikit-learn
> pandas
> numpy
> joblib
> ```

### 3. Place the Model Artifact
Ensure `model_data.joblib` is placed in the `artifacts/` directory.

### 4. Run the App
```bash
streamlit run main.py
```

---

## 🖥️ App Inputs

| Input | Description |
|---|---|
| Age | Applicant age (18–100) |
| Income | Annual income |
| Loan Amount | Requested loan amount |
| Loan Tenure | Duration in months |
| Avg DPD | Average days past due per delinquency |
| Delinquency Ratio | % of delinquent months |
| Credit Utilization Ratio | % of credit limit used |
| Open Accounts | Number of active loan accounts |
| Residence Type | Owned / Rented / Mortgage |
| Loan Purpose | Education / Home / Auto / Personal |
| Loan Type | Secured / Unsecured |

---

## 📤 App Output

- **Default Probability** — likelihood the applicant will default (e.g., `12.45%`)
- **Credit Score** — integer score between 300 and 900
- **Rating** — Poor / Average / Good / Excellent

---

## 📌 Key Design Decisions

- **Logistic Regression over XGBoost**: Chosen for interpretability — critical in financial/regulatory contexts where model explainability is required.
- **Dummy fields for scaling**: The scaler was fitted on all original numeric columns. Unused features are passed as dummy values at inference time to maintain scaling consistency without retraining.
- **Pre-EDA split**: Prevents EDA insights from inadvertently leaking into feature engineering decisions on test data.

---
