# # Custom Sorter

# numbers = [
#     {'Name':'Harsh','GPA':8.9},
#     {'Name':'Yash','GPA':7.8},
#     {'Name':'Tanish','GPA':9.6},
#     {'Name':'Sameer Sir','GPA':9.5},
#     {'Name':'Dr. Feroz','GPA':6.7}
# ]

# sorted_3 = sorted(numbers,key = lambda x: x['GPA'],reverse=True)[:3]

# print("TOP 3 Students : ")
# for i in sorted_3:
#     print(i)

#-----------------------------------------------------------------------------------------------------------------------

# # Data Pipeline

# from functools import reduce

# numbers = list(range(1,21))

# result = reduce(lambda a,b : a+b, map(lambda x : x**2, filter(lambda x : x % 2 != 0, numbers)))
# print(f"SUM : {result}")

#-----------------------------------------------------------------------------------------------------------------------

# # Mini Calculator Factory

# def make_operator(op):
#     if op == '+':
#         return lambda a,b : a + b
#     elif op == '-':
#         return lambda a,b : a - b 
#     elif op == '*':
#         return lambda a,b : a * b
#     elif op == '/':
#         return lambda a,b : a / b
#     else:
#         return 'Invalid Operator'
    
# add = make_operator("+")
# sub = make_operator("-")
# mul = make_operator("*")
# div = make_operator("/")

# print("Addition       : ",add(10,5))
# print("Subtraction    : ",sub(10,5))
# print("Multiplication : ",mul(10,5))
# print("Division       : ",div(10,5))

#-----------------------------------------------------------------------------------------------------------------------

# # Safe Input Validator

# class NegativeNumberError(Exception):
#     pass

# def get_positive_int():
#     while True:
#         try:
#             num = int(input("Enter a positive integer: "))
#             if num <= 0:
#                 raise NegativeNumberError("Number must be greater than 0!")
#             return num
#         except ValueError:
#             print("Invalid input! Enter only integers.")
#         except NegativeNumberError as e:
#             print(e)

# print("Valid number entered!!!! : ",get_positive_int())

#-----------------------------------------------------------------------------------------------------------------------

# # Robust File Processor

# import csv

# def process_csv(filepath):
#     file = None
#     try:
#         file = open(filepath, "r")
#         reader = csv.reader(file)
#         headers = next(reader)
#         sums = [0] * len(headers)
#         count = 0
#         for row in reader:
#             if len(row) != len(headers):
#                 raise csv.Error("Malformed row found!")

#             for i in range(len(row)):
#                 sums[i] += float(row[i])
#             count += 1

#         print("\nColumn Averages:")

#         for i in range(len(headers)):
#             print(headers[i], "=", sums[i] / count)

#     except FileNotFoundError:
#         print("File not found!")

#     except PermissionError:
#         print("Permission denied!")

#     except csv.Error as e:
#         print("CSV Error:", e)

#     finally:
#         if file:
#             file.close()
#             print("\nFile closed successfully.")

# process_csv("19-June.csv")

#-----------------------------------------------------------------------------------------------------------------------

# # Bank Account Simulator

# class InvalidAmountError(Exception):
#     pass

# class InsufficientFundsError(Exception):
#     pass

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             raise InvalidAmountError("Deposit amount must be positive!")

#         self.balance += amount
#         print("Deposited :", amount)

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise InvalidAmountError("Withdrawal amount must be positive!")

#         if amount > self.balance:
#             raise InsufficientFundsError("Not enough balance!")

#         self.balance -= amount
#         print("Withdrawn :", amount)

#     def show_balance(self):
#         print("Current Balance :", self.balance)

# acc = BankAccount(1000)

# while True:
#     try:
#         print("\n1. Deposit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Exit\n")

#         choice = int(input("Enter choice: "))

#         if choice == 1:
#             amt = float(input("Enter amount: "))
#             acc.deposit(amt)
#         elif choice == 2:
#             amt = float(input("Enter amount: "))
#             acc.withdraw(amt)
#         elif choice == 3:
#             acc.show_balance()
#         elif choice == 4:
#             print("Thank You!")
#             break
#         else:
#             print("Invalid Choice!")

#     except InvalidAmountError as e:
#         print("Error:", e)

#     except InsufficientFundsError as e:
#         print("Error:", e)

#     except ValueError:
#         print("Enter valid numeric input!")

#-----------------------------------------------------------------------------------------------------------------------