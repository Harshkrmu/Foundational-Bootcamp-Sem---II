# # Student Performance Analyzer

# def student_report(name, marks):
#     print("\n----- Student Report -----")
#     print(f"Name  : {name}")
#     print(f"Marks : {marks}")
#     print("--------------------------\n")

# def add_bonus(marks):
#     print(f"Inside Function Marks : {marks+5}")
#     print(f"Outside Function Marks : {marks}\n")

# def sum_marks(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_marks(n-1)

# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def apply_operations(func,value):
#     if ch == 1:
#         print(f"\nResult : {square(x)}")
#     if ch == 2:
#         print(f"\nResult : {cube(x)}")

# name = input("Enter your name : ")
# marks = int(input("Enter your marks : "))
# student_report(name, marks)
# add_bonus(marks)
# n = int(input("Enter a number for recursive sum : "))
# print(f"Recursive Sum : {sum_marks(n)}\n")
# print("Choose Operation:\n1. Square\n2. Cube\n")
# ch = int(input("Enter Choice : "))
# x = int(input("Enter Value : "))
# apply_operations(ch,x)
# print("----------------------------------------")

# try:
#     n = int(input("Entrer a number : "))
# except ValueError:
#     print("HAAHAHAHAHA!!!!")

# import random as ran
# sec = ran.randint(1, 10)
# attempts = 3
# while attempts > 0:
#     try:
#         x = int(input("Enter your Guess (1-10): "))

#         if x == sec:
#             print("\nCorrect Answer!!!")
#             break
#         else:
#             attempts -= 1

#             if attempts > 0:
#                 print(f"\nWrong Answer!!!")
#                 print(f"-----TRY AGAIN-----")
#                 print(f"No. of attempts remaining: {attempts}\n")
#             else:
#                 print("\nGame Over!!!!!")
#                 print("-----You exceeded the maximum number of attempts-----")
#                 print(f"The correct number was: {sec}")

#     except ValueError:
#         print("Invalid Input!!! Please enter an integer.")