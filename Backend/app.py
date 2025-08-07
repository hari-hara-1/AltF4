from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Configure your MySQL connection here
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Root$2000',
    database='credit_scoring_db'
)

@app.route('/profile', methods=['POST'])
def insert_profile():
    data = request.json
    with conn.cursor() as cur:
        sql = """
        INSERT INTO user_financial_profile (
            cash_inflow, avg_bank_balance, location_type,
            income_type, age_to_employment_ratio, housing_type,
            rent_amount, num_occupants, bill_payment_consistency,
            bnpl_used, bnpl_repayment_ratio, education_level, grade_or_cgpa
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data.get('cash_inflow'),
            data.get('avg_bank_balance'),
            data.get('location_type'),
            data.get('income_type'),
            data.get('age_to_employment_ratio'),
            data.get('housing_type'),
            data.get('rent_amount'),
            data.get('num_occupants'),
            data.get('bill_payment_consistency'),
            data.get('bnpl_used'),
            data.get('bnpl_repayment_ratio'),
            data.get('education_level'),
            data.get('grade_or_cgpa')
        )
        cur.execute(sql, params)
        conn.commit()
        user_id = cur.lastrowid
    return jsonify({'message': 'User profile stored', 'user_id': user_id})

if __name__ == '__main__':
    app.run(debug=True)
