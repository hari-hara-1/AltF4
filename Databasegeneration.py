import pandas as pd
import numpy as np
import random

# Seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows in the dataset
n_rows = 500

# --- Helper Functions ---

def random_cash_inflow(income_type):
    if income_type == 'Salaried':
        return np.random.randint(20000, 80000)
    elif income_type == 'Gig':
        return np.random.randint(10000, 40000)
    else:  # Informal
        return np.random.randint(5000, 25000)

def avg_bank_balance(cash_inflow):
    return int(cash_inflow * np.random.uniform(0.1, 0.5))

def random_location():
    return random.choices(['Urban', 'Semi-Urban', 'Rural'], weights=[0.5, 0.3, 0.2])[0]

def random_income_type():
    return random.choices(['Salaried', 'Gig', 'Informal'], weights=[0.5, 0.3, 0.2])[0]

def age_to_employment_ratio_fixed(income_type):
    age = np.random.randint(21, 55)
    if income_type == 'Salaried':
        min_exp = 1
        max_exp = max(1, age - 20)
    elif income_type == 'Gig':
        min_exp = 0
        max_exp = max(1, age - 18)
    else:
        min_exp = 0
        max_exp = max(1, age - 16)
    experience = np.random.randint(min_exp, max_exp + 1)
    ratio = round(experience / age, 2)
    return age, ratio

def random_housing_type():
    return random.choices(['Owned', 'Rented', 'PG/Hostel'], weights=[0.4, 0.5, 0.1])[0]

def rent_info(housing_type):
    if housing_type == 'Rented':
        rent = np.random.randint(3000, 15000)
        occupants = np.random.randint(1, 6)
        return rent, occupants
    elif housing_type == 'PG/Hostel':
        return np.random.randint(2000, 8000), 1
    else:
        return 0, np.random.randint(2, 6)  # Owned

def bill_payment_consistency():
    return random.choices(['Always', 'Usually', 'Sometimes', 'Rarely'], weights=[0.5, 0.3, 0.15, 0.05])[0]

def bnpl_used():
    return random.choice([True, False])

def education_level_and_grade():
    level = random.choices(['10th', '12th', 'Diploma', 'Graduate', 'Postgraduate'], weights=[0.1, 0.2, 0.15, 0.4, 0.15])[0]
    if level in ['Graduate', 'Postgraduate']:
        grade = round(np.random.uniform(6.0, 9.5), 2)  # CGPA
    else:
        grade = round(np.random.uniform(50, 95), 1)  # Percentage
    return level, grade

def approve_loan(cash_inflow, avg_balance, bill_consistency, bnpl, education):
    score = 0
    score += 1 if cash_inflow > 25000 else 0
    score += 1 if avg_balance > 5000 else 0
    score += 1 if bill_consistency in ['Always', 'Usually'] else 0
    score += 1 if bnpl else 0
    score += 1 if education in ['Graduate', 'Postgraduate'] else 0
    return 1 if score >= 3 else 0

# --- Generate Dataset ---

data = []

for i in range(n_rows):
    income_type = random_income_type()
    cash = random_cash_inflow(income_type)
    balance = avg_bank_balance(cash)
    location = random_location()
    age, emp_ratio = age_to_employment_ratio_fixed(income_type)
    housing = random_housing_type()
    rent, occupants = rent_info(housing)
    bill_cons = bill_payment_consistency()
    bnpl = bnpl_used()
    education, grade = education_level_and_grade()
    approval = approve_loan(cash, balance, bill_cons, bnpl, education)

    data.append([
        f'U{i+1:04d}', cash, balance, location, income_type, age, emp_ratio, housing,
        rent, occupants, bill_cons, bnpl, education, grade, approval
    ])

columns = [
    'user_id', 'cash_inflow', 'avg_bank_balance', 'location_type', 'income_type',
    'age', 'age_to_employment_ratio', 'housing_type', 'rent_amount', 'num_occupants',
    'bill_payment_consistency', 'bnpl_used', 'education_level', 'grade_or_cgpa',
    'loan_approved'
]

df = pd.DataFrame(data, columns=columns)

# Save or show preview
df.to_csv("synthetic_credit_data.csv", index=False)
print(df.head())