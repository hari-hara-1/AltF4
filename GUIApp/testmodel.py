import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import joblib
from GUIApp.evaluatemodel import evaluate_credit_score  # Your evaluation function

# Define the feature names directly
feature_names = [
    "age",
    "num_occupants",
    "cash_inflow",
    "avg_bank_balance",
    "bill_payment_consistency_Sometimes",
    "bill_payment_consistency_Usually",
    "bill_payment_consistency_Rarely",
    "bnpl_used_True",
    "rent_amount",
    "location_type_Urban",
    "location_type_Semi-Urban",
    "education_level_Graduate",
    "education_level_Postgraduate",
    "education_level_12th",
    "education_level_Diploma",
    "income_type_Salaried",
    "income_type_Informal",
    "income_type_Gig",
    "grade_or_cgpa",
    "housing_type_Rented",
    "housing_type_PG/Hostel",
    "age_to_employment_ratio"
]

# Load model
model = joblib.load("credit_score_model.pkl")

# Define test input
sample_input = {
    "age": 29,
    "num_occupants": 3,
    "cash_inflow": 45000,
    "avg_bank_balance": 80000,
    "bill_payment_consistency": "Usually",
    "bnpl_used": True,
    "rent_amount": 12000,
    "location_type": "Urban",
    "education_level": "Graduate",
    "income_type": "Salaried",
    "grade_or_cgpa": 7.5,
    "housing_type": "Rented",
    "age_to_employment_ratio": 0.5
}

# Run evaluation
evaluate_credit_score(sample_input, model)
