def compute_tax(salary):
    if salary <= 2000:
        tax_rate = 0
    elif salary > 2000 and salary <= 4000:
        tax_rate = 0.15
    elif salary > 4000 and salary <= 7000:
        tax_rate = 0.20
    elif salary > 7000 and salary <= 10000:
        tax_rate = 0.25
    elif salary > 10000 and salary <= 14000:
        tax_rate = 0.30 
    else:   
        tax_rate = 0.35
    tax = salary * tax_rate
    return tax       
salary = float(input("Enter your salary: "))
tax = compute_tax(salary)
if salary < 0:
    print("salary cannot be negative")
else:
    print(f"The tax on an salary of {salary} is {tax}")
