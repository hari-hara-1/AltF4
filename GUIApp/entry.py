import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class CreditScoringApp(tk.Toplevel):
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'Root$2000'
    DB_NAME = 'credit_scoring_db'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = self
        self.title("Alternative Credit Scoring - Data Entry")
        self.geometry("1000x1000")
        self.form_data = {}
        self.create_widgets()

    def create_widgets(self):
        # Fields
        self.create_label_entry("cash_inflow", 0)
        self.create_label_entry("avg_bank_balance", 1)
        self.create_dropdown("location_type", ["Urban", "Rural", "Semi-Urban"], 2)
        self.create_dropdown("income_type", ["Salaried", "Gig", "Informal"], 3)
        self.create_label_entry("age_to_employment_ratio", 4)
        self.create_dropdown("housing_type", ["Owned", "Rented", "PG"], 5)
        self.create_label_entry("rent_amount", 6)
        self.create_label_entry("num_occupants", 7)
        self.create_label_entry("bill_payment_consistency", 8)
        self.create_checkbox("bnpl_used", 9)
        self.create_label_entry("bnpl_repayment_ratio", 10)
        self.create_dropdown("education_level", ["None", "12th", "Diploma", "Graduate", "Postgraduate", "PhD"], 11)
        self.create_label_entry("grade_percentage", 12)

        # Submit button
        submit_btn = tk.Button(self.root, text="Submit", command=self.submit_data, fg="black")
        submit_btn.grid(row=13, column=5, pady=20)

    def create_label_entry(self, label, row):
        tk.Label(self.root, text=label).grid(row=row, column=5, sticky='w', padx=10, pady=5)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=6, pady=5)
        self.form_data[label] = entry

    def create_dropdown(self, label, options, row):
        tk.Label(self.root, text=label).grid(row=row, column=5, sticky='w', padx=10, pady=5)
        var = tk.StringVar(value=options[0])
        dropdown = ttk.Combobox(self.root, textvariable=var, values=options, state="readonly")
        dropdown.grid(row=row, column=6, pady=5)
        # Store both var and dropdown to prevent garbage collection
        self.form_data[label] = var
        self.form_data[label + "_widget"] = dropdown

    def create_checkbox(self, label, row):
        var = tk.BooleanVar()
        cb = tk.Checkbutton(self.root, text=label, variable=var)
        cb.grid(row=row, column=6, sticky='w', padx=10, pady=5)
        self.form_data[label] = var

    def submit_data(self):
        collected_data = {}
        for key, widget in self.form_data.items():
            if isinstance(widget, tk.Entry):
                collected_data[key] = widget.get().strip()
            elif isinstance(widget, tk.StringVar):
                collected_data[key] = widget.get().strip()
            elif isinstance(widget, tk.BooleanVar):
                collected_data[key] = int(widget.get())

        education = collected_data.get("education_level", "").strip()
        if not education or len(education) > 30:
            messagebox.showerror("Input Error", f"Invalid education level: '{education}'")
            return
        collected_data["education_level"] = education  # Overwrite with trimmed version

        # Debug print for safety
        print(f"Education level: '{education}' (length: {len(education)})")

        try:
            conn = mysql.connector.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME
            )
            cursor = conn.cursor()

            query = """
                INSERT INTO user_financial_profile (
                    cash_inflow, avg_bank_balance, location_type, income_type,
                    age_to_employment_ratio, housing_type, rent_amount, num_occupants,
                    bill_payment_consistency, bnpl_used, bnpl_repayment_ratio,
                    education_level, grade_percentage
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                collected_data["cash_inflow"],
                collected_data["avg_bank_balance"],
                collected_data["location_type"],
                collected_data["income_type"],
                collected_data["age_to_employment_ratio"],
                collected_data["housing_type"],
                collected_data["rent_amount"],
                collected_data["num_occupants"],
                collected_data["bill_payment_consistency"],
                collected_data["bnpl_used"],
                collected_data["bnpl_repayment_ratio"],
                collected_data["education_level"],
                collected_data["grade_percentage"]
            )

            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Data inserted into database successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()