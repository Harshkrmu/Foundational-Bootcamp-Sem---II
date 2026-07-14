# # Library Fine Calculator

# i = 0
# ind_name = []
# ind_fine = []
# High_fine = 0
# while i < 1:
#     fine = 0
#     name = input("Enter your Name : ")
#     ind_name.append(name)
#     Day_l = int(input("How many days Late : "))
#     if Day_l <= 5 :
#         fine = 5*Day_l
#         ind_fine.append(fine)
#     elif Day_l <=10 :
#         fine = 10*Day_l
#         ind_fine.append(fine)
#     else:
#         fine = 20*Day_l
#         ind_fine.append(fine)
    
#     if fine > High_fine:
#         High_fine = fine

#     x = input("\nContinue[C] / Exit[E] : ").lower()
#     if x != 'c' :
#         i = 1

# avg = sum(ind_fine)/len(ind_fine)

# for i in range(len(ind_fine)):
#     print(f"Name : {ind_name[i]}")
#     print(f"Fine : {ind_fine[i]}\n")
 
# print(f"Total Fine : {sum(ind_fine)}")
# print(f"Highest Fine : {max(ind_fine)}")
# print(f"Average Fine : {avg:.2f}")

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

# name = input("Enter your name : ")
# marks = int(input("Enter your marks : "))
# student_report(name, marks)
# add_bonus(marks)
# n = int(input("Enter a number for recursive sum : "))
# print(f"Recursive Sum : {sum_marks(n)}\n")
# print("Choose Operation:\n1. Square\n2. Cube")
# ch = int(input("Enter Choice : "))
# x = int(input("Enter Value : "))
# if ch == 1:
#     print(f"\nResult : {square(x)}")
# if ch == 2:
#     print(f"\nResult : {cube(x)}")