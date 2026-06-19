'''
#Calculator for 2 entries
print("/////-----CALCULATOR-----/////")
a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
n = 1
while n == 1:
    print("//--OPERATIONS--//")
    print("//-- 1. Addition(+) --//")
    print("//-- 2. Subtraction(-) --//")
    print("//-- 3. Multiplication(*) --//")
    print("//-- 4. Division(/) --//")
    print("//-- 5. Floor Division(//) --//")
    print("//-- 6. Exponent Power(**) --//")
    op = int(input("CHOOSE YOUR OPERATION NO : "))
    if op == 1 :
        print("Answer : ",a+b)
    elif op == 2 :
        print("Answer : ",a-b)
    elif op == 3 :
        print("Answer : ",a*b)
    elif op == 4 :
        print("Answer : ",a/b)
    elif op == 5 :
        print("Answer : ",a//b)
    elif op == 6 :
        print("Answer : ",a**b)
    else:
        print("//--Please Enter Operation No Correctly--//")
    x = input("Do you want to continue [y/n] : ")
    if x.lower() == 'n':
        n = 0
print("/////-----THANK YOU FOR USING OUR CALCULATOR-----/////")
'''
'''
# Simple Calculator with Multiple Inputs

def calculate(nums, choice):
    result = nums[0]

    for i in range(1, len(nums)):
        if choice == 1:
            result += nums[i]
        elif choice == 2:
            result -= nums[i]
        elif choice == 3:
            result *= nums[i]
        elif choice == 4:
            if nums[i] == 0:
                return "Error: Division by zero!"
            result /= nums[i]
        elif choice == 5:
            if nums[i] == 0:
                return "Error: Modulus by zero!"
            result %= nums[i]
        elif choice == 6:
            result **= nums[i]

    return result


while True:
    n = int(input("Enter number of values: "))

    numbers = []
    for i in range(n):
        numbers.append(float(input(f"Enter value {i+1}: ")))

    print("\n1.Addition\n2.Subtraction")
    print("3.Multiplication\n4.Division")
    print("5.Modulus\n6.Exponentiation")

    choice = int(input("Enter choice (1-6): "))

    if 1 <= choice <= 6:
        print("Result =", calculate(numbers, choice))
    else:
        print("Invalid Choice!")

    if input("\nContinue? (y/n): ").lower() == 'n':
        break

print("\n----- THANK YOU FOR USING OUR CALCULATOR -----")
'''
'''
# Function to calculate and display salary details
def Calculate_salary(emp_id, name, basic_salary):
    hra = basic_salary * 20/100
    da = basic_salary * 15/100
    tax = basic_salary * 10/100

    gross_salary = basic_salary + hra + da
    net_salary = gross_salary - tax

    print("\n\t----- Employee Salary Details -----")
    print("Employee ID :", emp_id)
    print("Employee Name :", name)
    print("Basic Salary :", basic_salary)
    print("Gross Salary :", gross_salary)
    print("Net Salary :", net_salary)
    print("-----------------------------------\n")

# Number of employees
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    # Function call
    Calculate_salary(emp_id, name, basic_salary)
'''
'''
def greet(name,greeting="Hello"):
    #return a greeting string
    print(f"{greeting},{name}")
msg = greet("Alice")
print(msg)
print(greet("Bob","Hi"))
'''
'''
# Simple ATM System

balance = 1000
history = []

def check_balance():
    print("\nCurrent Balance: ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        history.append(f"Deposited ₹{amount}")
        print("Money Deposited Successfully!")
    else:
        print("Invalid Amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid Amount!")
    elif amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        history.append(f"Withdrawn ₹{amount}")
        print("Money Withdrawn Successfully!")

def transaction_history():
    print("\nTransaction History:")
    
    if len(history) == 0:
        print("No Transactions Yet!")
    else:
        for t in history:
            print(t)

while True:
    print("\n\tATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transaction_history()

    elif choice == "5":
        print("Thank You for Using ATM!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
'''