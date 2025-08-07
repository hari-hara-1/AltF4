CREATE DATABASE IF NOT EXISTS credit_scoring_db;
USE credit_scoring_db;

CREATE TABLE user_financial_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cash_inflow DECIMAL(12,2),
    avg_bank_balance DECIMAL(12,2),
    location_type VARCHAR(30),
    income_type VARCHAR(20),
    age_to_employment_ratio DECIMAL(4,2),
    housing_type VARCHAR(20),
    rent_amount DECIMAL(10,2) NULL,
    num_occupants INT NULL,
    bill_payment_consistency DECIMAL(3,2) NULL,
    bnpl_used BOOLEAN,
    bnpl_repayment_ratio DECIMAL(3,2) NULL,
    education_level VARCHAR(30),
    grade_percentage DECIMAL(4,2) NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    
);
alter table user_financial_profile rename column grade_or_cgpa to grade_percentage;
select * from user_financial_profile;