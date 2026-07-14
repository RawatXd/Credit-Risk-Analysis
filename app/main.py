import streamlit as st
import plotly.graph_objects as go
from prediction_helper import predict

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="CreditLens",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:2rem;
    padding-left:4rem;
    padding-right:4rem;
    padding-bottom:2rem;
}

html{
    scroll-behavior:smooth;
}

.card{
    background:#ffffff;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.08);
    border:1px solid #E5E7EB;
}

.metric-card{
    background:#F8FAFC;
    border-radius:16px;
    padding:20px;
    text-align:center;
    border:1px solid #E2E8F0;
}

.hero{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:40px;
    border-radius:20px;
    color:white;
}

.small{
    color:#64748B;
    font-size:15px;
}

.big{
    font-size:42px;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Hero
# --------------------------------------------------

st.markdown("""
<div class="hero">

<div class="big">
💳 CreditLens
</div>

### Intelligent Credit Risk Assessment Platform

Estimate the **Probability of Default (PD)** using an interpretable
machine learning credit scorecard developed with Logistic Regression.

</div>
""", unsafe_allow_html=True)

st.write("")

st.info(
"""
This application assists lenders in assessing borrower creditworthiness by predicting
Probability of Default (PD), generating a credit score, and providing a lending recommendation.
"""
)

st.write("")

left, right = st.columns([1.2,1])

# =====================================================
# LEFT COLUMN
# =====================================================

with left:

    st.markdown("## 📝 Applicant Information")

    with st.container(border=True):

        age = st.number_input(
            "Age",
            18,
            100,
            28
        )

        income = st.number_input(
            "Annual Income (₹)",
            value=1200000
        )

        loan_amount = st.number_input(
            "Loan Amount (₹)",
            value=2560000
        )

        loan_tenure_months = st.number_input(
            "Loan Tenure (Months)",
            value=36
        )

        avg_dpd_per_delinquency = st.number_input(
            "Average Days Past Due",
            value=20
        )

        delinquency_ratio = st.number_input(
            "Delinquency Ratio (%)",
            value=30
        )

        credit_utilization_ratio = st.number_input(
            "Credit Utilization (%)",
            value=30
        )

        num_open_accounts = st.number_input(
            "Open Loan Accounts",
            value=2,
            min_value=1
        )

        residence_type = st.selectbox(
            "Residence Type",
            ["Owned","Rented","Mortgage"]
        )

        loan_purpose = st.selectbox(
            "Loan Purpose",
            ["Education","Home","Auto","Personal"]
        )

        loan_type = st.selectbox(
            "Loan Type",
            ["Secured","Unsecured"]
        )

        loan_to_income_ratio = loan_amount/income if income else 0

        st.metric(
            "Loan-to-Income Ratio",
            f"{loan_to_income_ratio:.2f}"
        )

        predict_button = st.button(
            "🔍 Assess Credit Risk",
            use_container_width=True
        )

# =====================================================
# RIGHT COLUMN
# =====================================================

with right:

    st.markdown("## 📊 Prediction Summary")


    if predict_button:

        probability, credit_score, rating = predict(
            age,
            income,
            loan_amount,
            loan_tenure_months,
            avg_dpd_per_delinquency,
            delinquency_ratio,
            credit_utilization_ratio,
            num_open_accounts,
            residence_type,
            loan_purpose,
            loan_type
        )

        # -------------------------
        # Metric Cards
        # -------------------------

        st.markdown("### 📊 Key Metrics")

        c1, c2, c3 = st.columns(3)

        with c1:
           st.metric(
            label="Probability of Default",
            value=f"{probability:.2%}",
            delta="Lower is Better"
             )
    
        with c2:
           st.metric(
           label="Credit Score",
           value=f"{int(credit_score)}"
             )

        with c3:

          if probability < 0.30:
            st.metric("Risk Category", "🟢 LOW")
 
          elif probability < 0.60:
           st.metric("Risk Category", "🟡 MEDIUM")

          else:
           st.metric("Risk Category", "🔴 HIGH")

        st.write("")

        # -------------------------
        # Gauge Chart
        # -------------------------

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=probability*100,

            number={
                "suffix":"%",
                "font":{"size":42}
            },

            title={
                "text":"Probability of Default",
                "font":{"size":20}
            },

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"royalblue"
                },

                "steps":[

                    {
                        "range":[0,30],
                        "color":"#22C55E"
                    },

                    {
                        "range":[30,60],
                        "color":"#FACC15"
                    },

                    {
                        "range":[60,100],
                        "color":"#EF4444"
                    }

                ]
            }

        ))

        fig.update_layout(
            height=320,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.divider()

        st.markdown("### 📈 Score Breakdown")

        score = max(300, min(int(credit_score), 900))

        score_percent = (score - 300) / 600

        st.progress(
            score_percent,
            text=f"Credit Score : {score} / 900"
          )

        # -------------------------
        # Recommendation
        # -------------------------

        st.markdown("### 🏦 Lending Recommendation")

        rating_lower = rating.lower()

        if "low" in rating_lower:

            st.success(
                "✅ **APPROVE**\n\nThe applicant demonstrates a low probability of default."
            )

        elif "medium" in rating_lower:

            st.warning(
                "🟡 **MANUAL REVIEW**\n\nThe application requires additional verification."
            )

        else:

            st.error(
                "❌ **REJECT**\n\nThe applicant presents a high probability of default."
            )

        st.divider()

        # -------------------------
        # Applicant Summary
        # -------------------------

        st.markdown("### 👤 Applicant Summary")

        summary1, summary2 = st.columns(2)

        with summary1:

            st.write(f"**Age:** {age}")

            st.write(f"**Income:** ₹{income:,.0f}")

            st.write(f"**Loan Amount:** ₹{loan_amount:,.0f}")

            st.write(f"**Loan Tenure:** {loan_tenure_months} Months")

            st.write(f"**Loan-to-Income Ratio:** {loan_to_income_ratio:.2f}")

        with summary2:

            st.write(f"**Residence:** {residence_type}")

            st.write(f"**Purpose:** {loan_purpose}")

            st.write(f"**Loan Type:** {loan_type}")

            st.write(f"**Credit Utilization:** {credit_utilization_ratio}%")

            st.write(f"**Open Accounts:** {num_open_accounts}")

    else:
 
        st.info("👈 Fill in the applicant details and click **Assess Credit Risk** to generate a prediction.")

        st.divider()

        st.markdown("### 🚦 Key Risk Indicators")

        risk_flags = []

        if loan_to_income_ratio > 3:
           risk_flags.append("High Loan-to-Income Ratio")

        if credit_utilization_ratio > 60:
           risk_flags.append("High Credit Utilization")

        if delinquency_ratio > 40:
            risk_flags.append("High Delinquency Ratio")

        if avg_dpd_per_delinquency > 30:
            risk_flags.append("Frequent Delinquencies")

        if len(risk_flags) == 0:

          st.success("✅ No major risk indicators detected.")

        else:

          for item in risk_flags:

             st.warning(item)

        st.divider()

        st.markdown("### 💰 Financial Snapshot")

        a, b, c = st.columns(3)

        with a:
          st.metric("Income", f"₹{income:,.0f}")

        with b:
          st.metric("Loan Amount", f"₹{loan_amount:,.0f}")

        with c:
          st.metric("LTI Ratio", f"{loan_to_income_ratio:.2f}")

st.markdown("---")

st.caption(
    "CreditLens • Intelligent Credit Risk Assessment Platform | Built with Python, Streamlit & Scikit-Learn"
)