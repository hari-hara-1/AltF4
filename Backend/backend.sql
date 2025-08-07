CREATE DATABASE IF NOT EXISTS credit_scoring_db;
USE credit_scoring_db;

CREATE TABLE user_financial_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cash_inflow DECIMAL(12,2),
    avg_bank_balance DECIMAL(12,2),
    location_type ENUM('Urban','Rural','Semi-Urban'),
    income_type ENUM('Salaried','Gig','Informal'),
    age_to_employment_ratio DECIMAL(4,2),
    housing_type ENUM('Owned','Rented','PG'),
    rent_amount DECIMAL(10,2) NULL,
    num_occupants INT NULL,
    bill_payment_consistency DECIMAL(3,2) NULL,
    bnpl_used BOOLEAN,
    bnpl_repayment_ratio DECIMAL(3,2) NULL,
    education_level ENUM('12th','Diploma','Grad','PostGrad'),
    grade_or_cgpa DECIMAL(4,2) NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);