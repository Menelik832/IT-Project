def tax_determiner(income):
    if income <= 2000:
        tax_rate = 0
    elif income > 2000 and income <= 4000:
        tax_rate = 0.15
    elif income > 4000 and income <= 7000:
        tax_rate = 0.20
    elif income > 7000 and income <= 10000:
        tax_rate = 0.25
    elif income > 10000 and income <= 14000:
        tax_rate = 0.30 
    else:   
        tax_rate = 0.35
    tax = income * tax_rate
    return tax       
income = float(input("Enter your income: "))
tax = tax_determiner(income)
if income < 0:
    print("Income cannot be negative")
else:
    print(f"The tax on an income of {income} is {tax}")
