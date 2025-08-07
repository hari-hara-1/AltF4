import tkinter as tk
from tkinter import ttk

class CreditScoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alternative Credit Scoring - Data Entry")
        self.root.geometry("600x700")
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
        self.create_label_entry("grade_or_cgpa", 12)

        # Submit button
        submit_btn = tk.Button(self.root, text="Submit", command=self.submit_data)
        submit_btn.grid(row=13, column=1, pady=20)

    def create_label_entry(self, label, row):
        tk.Label(self.root, text=label).grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, pady=5)
        self.form_data[label] = entry

    def create_dropdown(self, label, options, row):
        tk.Label(self.root, text=label).grid(row=row, column=0, sticky='w', padx=10, pady=5)
        var = tk.StringVar()
        dropdown = ttk.Combobox(self.root, textvariable=var, values=options, state="readonly")
        dropdown.grid(row=row, column=1, pady=5)
        self.form_data[label] = var

    def create_checkbox(self, label, row):
        var = tk.BooleanVar()
        cb = tk.Checkbutton(self.root, text=label, variable=var)
        cb.grid(row=row, column=1, sticky='w', padx=10, pady=5)
        self.form_data[label] = var

    def submit_data(self):
        collected_data = {}
        for key, widget in self.form_data.items():
            if isinstance(widget, tk.Entry):
                collected_data[key] = widget.get()
            elif isinstance(widget, tk.StringVar):
                collected_data[key] = widget.get()
            elif isinstance(widget, tk.BooleanVar):
                collected_data[key] = widget.get()
        print("\nCollected Form Data:")
        for k, v in collected_data.items():
            print(f"{k}: {v}")
        # Here you can insert to MySQL or use the data for scoring

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = CreditScoringApp(root)
    root.mainloop()
