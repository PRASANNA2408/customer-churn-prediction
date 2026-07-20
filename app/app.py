"""
Customer Churn Prediction App

This Streamlit application predicts whether a telecom customer is likely to churn
using the trained Logistic Regression model.
"""

import streamlit as st

from prediction import predict_churn

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("📊 Customer Churn Prediction")

st.markdown("""
Welcome to the **Customer Churn Prediction System**.

This application uses a trained **Logistic Regression** model to predict whether
a telecom customer is likely to churn based on customer information.

The prediction is generated using the machine learning model developed during
this project.
""")

st.divider()

st.info(
    """
    👈 Fill in the customer details using the sidebar and click **Predict Churn**
    to estimate the likelihood of customer churn using the trained Machine Learning model.
    """
)

st.markdown("### 📌 Model Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Model",
        value="Logistic Regression"
    )

with col2:
    st.metric(
        label="Accuracy",
        value="80.38%"
    )

with col3:
    st.metric(
        label="Features",
        value="30"
    )

st.divider()
# -------------------------------------------------------
# Customer Input Section
# -------------------------------------------------------

st.sidebar.header("Customer Information")

st.sidebar.markdown(
    "Enter the customer details below to predict whether the customer is likely to churn."
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12
)
# -------------------------------------------------------
# Phone Services
# -------------------------------------------------------

st.sidebar.subheader("📞 Phone Services")

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

# -------------------------------------------------------
# Internet Services
# -------------------------------------------------------

st.sidebar.subheader("🌐 Internet Services")

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.sidebar.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

# -------------------------------------------------------
# Contract & Billing
# -------------------------------------------------------

st.sidebar.subheader("💳 Contract & Billing")

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0,
    step=0.01
)

total_charges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0,
    step=0.01
)

predict_button = st.sidebar.button(
    "Predict Churn"
)

if predict_button:

    customer_data = {
        "Gender": gender,
        "Senior Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure": tenure,
        "Phone Service": phone_service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Contract": contract,
        "Paperless Billing": paperless_billing,
        "Payment Method": payment_method,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }

    prediction, probability = predict_churn(customer_data)

    st.divider()

    st.header("📊 Prediction Result")

    if prediction == 1:

            st.error(
                "⚠️ High Risk: This customer is likely to churn."
            )

    else:

            st.success(
                "✅ Low Risk: This customer is likely to stay."
            )

    st.metric(
            label="Churn Probability",
            value=f"{probability:.2%}"
        )

    st.progress(float(probability))

    if probability < 0.30:

            st.success("🟢 Risk Level : LOW")

    elif probability < 0.70:

            st.warning("🟡 Risk Level : MEDIUM")

    else:

            st.error("🔴 Risk Level : HIGH")


        # -------------------------------------------------------
        # Customer Summary
        # -------------------------------------------------------

    st.divider()

    st.header("👤 Customer Summary")

    col1, col2 = st.columns(2)

    with col1:

            st.write(f"**Gender:** {gender}")
            st.write(f"**Senior Citizen:** {senior_citizen}")
            st.write(f"**Partner:** {partner}")
            st.write(f"**Dependents:** {dependents}")
            st.write(f"**Tenure:** {tenure} Months")

    with col2:

            st.write(f"**Contract:** {contract}")
            st.write(f"**Internet Service:** {internet_service}")
            st.write(f"**Payment Method:** {payment_method}")
            st.write(f"**Monthly Charges:** ${monthly_charges:.2f}")
            st.write(f"**Total Charges:** ${total_charges:.2f}")

        # -------------------------------------------------------
        # Business Recommendation
        # -------------------------------------------------------

    st.divider()

    st.header("💡 Business Recommendation")

    if probability < 0.30:

            st.success("""
        ### ✅ Low Risk Customer

        This customer shows strong loyalty indicators.

        **Recommended Action**

        - Continue regular engagement
        - Maintain current service quality
        - Offer loyalty rewards when appropriate
        """)

    elif probability < 0.70:

            st.warning("""
        ### 🟡 Medium Risk Customer

        This customer has a moderate likelihood of churn.

        **Recommended Action**

        - Monitor customer satisfaction
        - Offer personalized promotions
        - Encourage long-term contract renewal
        """)

    else:

            st.error("""
        ### 🔴 High Risk Customer

        This customer has a high probability of churning.

        **Recommended Action**

        - Contact the customer immediately
        - Offer retention discounts
        - Recommend a long-term contract
        - Provide premium technical support
        """)
            

        # -------------------------------------------------------
        # Top Risk Factors
        # -------------------------------------------------------

    st.divider()

    st.header("🔍 Top Risk Factors")

    risk_factors = []

        # Contract
    if contract == "Month-to-month":
            risk_factors.append("📌 Customer is on a Month-to-month contract.")

        # Tenure
    if tenure < 12:
            risk_factors.append("📌 Customer has a short tenure.")

        # Internet Service
    if internet_service == "Fiber optic":
            risk_factors.append("📌 Customer uses Fiber optic internet.")

        # Online Security
    if online_security == "No":
            risk_factors.append("📌 Customer does not have Online Security.")

        # Tech Support
    if tech_support == "No":
            risk_factors.append("📌 Customer does not have Tech Support.")

        # Payment Method
    if payment_method == "Electronic check":
            risk_factors.append("📌 Customer pays using Electronic check.")

        # Monthly Charges
    if monthly_charges > 80:
            risk_factors.append("📌 Customer has high monthly charges.")

        # Display Risk Factors
    if risk_factors:

            for factor in risk_factors:
                st.write(factor)

    else:

            st.success(
                "✅ No major churn risk factors detected for this customer."
            )