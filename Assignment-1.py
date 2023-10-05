#Name:Jazim.J
#Reg.No:192210471

#Question 1:

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

#Sample output:

Enter your income: 165000
Tax payable: 1500.0
> 

#Question 2:

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

#Sample output:

Enter the current date (dd/mm/yyyy): 05/10/2023
Enter your date of birth (dd/mm/yyyy): 27/02/2004
Your age is 19 years.

#Question 3:

number = input("Enter a 5-digit number: ")

if len(number) != 5 or not number.isdigit():
    print("Please enter a valid 5-digit number.")
else:
    for i in range(len(number)):
        formatted_number = number[i:]
        print(f"{formatted_number:>{5-i}}")

#Sample output:

Enter a 5-digit number:12345
12345       1
 2345	    12
  345	    123
   45	    1234
    5	    12345

#Question 4:

# Get employee information
employee_name = input("Enter the employee's name: ")
hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours worked: "))
overtime_hours = float(input("Enter the total overtime hours worked: "))

# Calculate total weekly pay
regular_pay = hourly_wage * regular_hours
overtime_pay = hourly_wage * 1.5 * overtime_hours
total_weekly_pay = regular_pay + overtime_pay

# Print the employee's total weekly pay
print(f"{employee_name}'s total weekly pay is: ${total_weekly_pay:.2f}")

#Sample output:

Enter the employee's name: Jazim
Enter the hourly wage: 4500
Enter the total regular hours worked: 6
Enter the total overtime hours worked: 2
Jazim's total weekly pay is: $40500.00

#Question 5:

# Function to calculate GCD using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD
result = gcd(num1, num2)

# Display the GCD
print(f"The GCD of {num1} and {num2} is {result}")

#Sample output:

Enter the first number: 64
Enter the second number: 23
The GCD of 64 and 23 is 1




