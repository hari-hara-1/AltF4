print("Hello, world!")
income= float(input("Enter your current income"))
spendings= float(input("Enter your average spendings"))
savings= 100*(income-spendings)/ income
stability= int(input("Enter the number corresponding to your job"))
cgpa= float
if( stability < 500):
    print("Candidate is NOT eligible for loan.")

else:
    print("Candidate is elligible for loan.")
print("Savings rate: ",savings," %")
