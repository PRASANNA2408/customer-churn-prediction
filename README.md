# 📊 Customer Churn Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services.

The project includes the complete machine learning workflow, from data preprocessing and exploratory data analysis (EDA) to model development, evaluation, and deployment using Streamlit.

---

## 🚀 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This project predicts the probability of customer churn using historical customer data and provides business recommendations based on the prediction.

---

## 🎯 Business Problem

The objective is to build a classification model capable of predicting whether a customer is likely to leave the telecom company.

Early prediction enables businesses to:

- Improve customer retention
- Reduce revenue loss
- Identify high-risk customers
- Design targeted retention strategies

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains customer information including:

- Customer demographics
- Internet services
- Phone services
- Billing information
- Contract details
- Customer tenure
- Churn status

---

## ⚙️ Project Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Model Evaluation
8. Model Comparison
9. Model Deployment using Streamlit

---

## 📁 Project Structure

```text
customer_churn_prediction/
│
├── app/
│   ├── app.py
│   └── prediction.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│
├── models/
│
├── notebooks/
│
├── results/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🤖 Machine Learning Models

The following classification models were developed and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The best-performing model was deployed using Streamlit for real-time predictions.

---

## 📈 Model Performance

The deployed Logistic Regression model achieved:

| Metric | Value |
|---------|--------|
| Accuracy | **80.38%** |
| Problem Type | Binary Classification |

---

## 🌐 Streamlit Web Application

The web application allows users to:

- Enter customer details
- Predict customer churn
- View churn probability
- View customer risk level
- View business recommendations
- Identify top churn risk factors

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/PRASANNA2408/customer-churn-prediction.git
```

Navigate to the project

```bash
cd customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app/app.py
```

---

## 🔮 Future Improvements

- Hyperparameter optimization
- SHAP explainability
- Cloud deployment
- API integration
- Deep Learning model comparison

---

## 👨‍💻 Author

**Prasanna Venkataramanan**

If you found this project useful, feel free to ⭐ the repository.