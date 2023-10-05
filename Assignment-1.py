//Name:Jazim.J
//Reg.No:192210471

Question 1:

def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = (income - 150000) * 0.10
    elif income <= 500000:
        tax = (150000 * 0.10) + ((income - 300000) * 0.20)
    else:
        tax = (150000 * 0.10) + (200000 * 0.20) + ((income - 500000) * 0.30)
    return tax

income = float(input("Enter your income: "))
tax = calculate_tax(income)
print(f"Tax payable: {tax}")

sample output:

Enter your income: 165000
Tax payable: 1500.0
> 

Question 2:

from datetime import datetime

def calculate_age(birthdate, current_date):
    birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
    current_date = datetime.strptime(current_date, "%d/%m/%Y")
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    return age

current_date = input("Enter the current date (dd/mm/yyyy): ")
birthdate = input("Enter your date of birth (dd/mm/yyyy): ")

age = calculate_age(birthdate, current_date)
print(f"Your age is {age} years.")

Sample output:

Enter the current date (dd/mm/yyyy): 05/10/2023
Enter your date of birth (dd/mm/yyyy): 27/02/2004
Your age is 19 years.

