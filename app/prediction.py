"""
Prediction Module

This module is responsible for:

1. Loading the trained machine learning model
2. Loading the fitted StandardScaler
3. Loading the feature column names
4. Preparing customer input data
5. Predicting customer churn
"""

import joblib
import pandas as pd

from pathlib import Path

# -------------------------------------------------------
# Project Directories
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"

# -------------------------------------------------------
# Load Trained Objects
# -------------------------------------------------------

def load_model():

    model = joblib.load(
        MODEL_DIR / "logistic_regression.pkl"
    )

    scaler = joblib.load(
        MODEL_DIR / "scaler.pkl"
    )

    feature_columns = joblib.load(
        MODEL_DIR / "feature_columns.pkl"
    )

    return model, scaler, feature_columns

if __name__ == "__main__":

    model, scaler, feature_columns = load_model()

    print("Model Loaded Successfully")

    print(feature_columns)

# -------------------------------------------------------
# Prepare Customer Input
# -------------------------------------------------------

def prepare_input(customer_data):

    # Load trained objects
    _, scaler, feature_columns = load_model()

    # Create empty dataframe with training columns
    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # -----------------------------
    # Numerical Features
    # -----------------------------

    input_df["SeniorCitizen"] = 1 if customer_data["Senior Citizen"] == "Yes" else 0

    input_df["tenure"] = customer_data["Tenure"]

    input_df["MonthlyCharges"] = customer_data["Monthly Charges"]

    input_df["TotalCharges"] = customer_data["Total Charges"]

    # -----------------------------
    # Binary Features
    # -----------------------------

    input_df["gender_Male"] = 1 if customer_data["Gender"] == "Male" else 0

    input_df["Partner_Yes"] = 1 if customer_data["Partner"] == "Yes" else 0

    input_df["Dependents_Yes"] = 1 if customer_data["Dependents"] == "Yes" else 0

    input_df["PhoneService_Yes"] = 1 if customer_data["Phone Service"] == "Yes" else 0

    input_df["PaperlessBilling_Yes"] = (
        1 if customer_data["Paperless Billing"] == "Yes" else 0
    )

    # -----------------------------
    # Multiple Lines
    # -----------------------------

    if customer_data["Multiple Lines"] == "No phone service":
        input_df["MultipleLines_No phone service"] = 1

    elif customer_data["Multiple Lines"] == "Yes":
        input_df["MultipleLines_Yes"] = 1

    # -----------------------------
    # Internet Service
    # -----------------------------

    if customer_data["Internet Service"] == "Fiber optic":
        input_df["InternetService_Fiber optic"] = 1

    elif customer_data["Internet Service"] == "No":
        input_df["InternetService_No"] = 1

    # -----------------------------
    # Online Security
    # -----------------------------

    if customer_data["Online Security"] == "No internet service":
        input_df["OnlineSecurity_No internet service"] = 1

    elif customer_data["Online Security"] == "Yes":
        input_df["OnlineSecurity_Yes"] = 1

    # -----------------------------
    # Online Backup
    # -----------------------------

    if customer_data["Online Backup"] == "No internet service":
        input_df["OnlineBackup_No internet service"] = 1

    elif customer_data["Online Backup"] == "Yes":
        input_df["OnlineBackup_Yes"] = 1

    # -----------------------------
    # Device Protection
    # -----------------------------

    if customer_data["Device Protection"] == "No internet service":
        input_df["DeviceProtection_No internet service"] = 1

    elif customer_data["Device Protection"] == "Yes":
        input_df["DeviceProtection_Yes"] = 1

    # -----------------------------
    # Tech Support
    # -----------------------------

    if customer_data["Tech Support"] == "No internet service":
        input_df["TechSupport_No internet service"] = 1

    elif customer_data["Tech Support"] == "Yes":
        input_df["TechSupport_Yes"] = 1

    # -----------------------------
    # Streaming TV
    # -----------------------------

    if customer_data["Streaming TV"] == "No internet service":
        input_df["StreamingTV_No internet service"] = 1

    elif customer_data["Streaming TV"] == "Yes":
        input_df["StreamingTV_Yes"] = 1

    # -----------------------------
    # Streaming Movies
    # -----------------------------

    if customer_data["Streaming Movies"] == "No internet service":
        input_df["StreamingMovies_No internet service"] = 1

    elif customer_data["Streaming Movies"] == "Yes":
        input_df["StreamingMovies_Yes"] = 1

    # -----------------------------
    # Contract
    # -----------------------------

    if customer_data["Contract"] == "One year":
        input_df["Contract_One year"] = 1

    elif customer_data["Contract"] == "Two year":
        input_df["Contract_Two year"] = 1

    # -----------------------------
    # Payment Method
    # -----------------------------

    if customer_data["Payment Method"] == "Credit card (automatic)":
        input_df["PaymentMethod_Credit card (automatic)"] = 1

    elif customer_data["Payment Method"] == "Electronic check":
        input_df["PaymentMethod_Electronic check"] = 1

    elif customer_data["Payment Method"] == "Mailed check":
        input_df["PaymentMethod_Mailed check"] = 1

    # -----------------------------
    # Scale Numerical Features
    # -----------------------------

    numerical_columns = [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    input_df[numerical_columns] = scaler.transform(
        input_df[numerical_columns]
    )

    return input_df

# -------------------------------------------------------
# Predict Customer Churn
# -------------------------------------------------------

def predict_churn(customer_data):

    # Load trained objects
    model, _, _ = load_model()

    # Prepare customer input
    input_df = prepare_input(customer_data)

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Prediction probability
    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability