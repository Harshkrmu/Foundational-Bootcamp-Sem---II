'''
# Unit Conversion System
def length_converter(unit_ch,value):
    if unit_ch == 1:
        print(f"{value}cm = {value/100}m = {value/100000}km")
    elif unit_ch == 2:
        print(f"{value}m = {value*100}cm = {value/1000}km")
    elif unit_ch == 3:
        print(f"{value}km = {value*1000}m = {value*100000}cm")
    else:
        print("Invalid Choice")

def weight_converter(unit_ch,value):
    if unit_ch == 1:
        print(f"{value}mg = {value/1000}g = {value/1000000}kg")
    elif unit_ch == 2:
        print(f"{value}g = {value*1000}mg = {value/1000}kg")
    elif unit_ch == 3:
        print(f"{value}kg = {value*1000}g = {value*1000000}mg")
    else:
        print("Invalid Choice")

def liquid_converter(unit_ch,value):
    if unit_ch == 1:
        print(f"{value}ml = {value/1000}L")
    elif unit_ch == 2:
        print(f"{value}L = {value*1000}ml")
    else:
        print("Invalid Choice")

while True:
    print("=====Units=====")
    print("1. Length")
    print("2. Weight")
    print("3. Liquid")
    print("4. Exit")
    print("===============")

    choice = int(input("Enter your choice (1-4) : "))

    if choice == 4:
        print("=================================================")
        print(" Thank you for using our Unit Conversion System")
        print("=================================================")
        break

    value = int(input("Enter the value : "))

    if choice == 1:
        print("1. cm\t2. m\t3. km")
        unit_ch = int(input("Enter intial unit (1-3) : "))
        length_converter(unit_ch,value)

    elif choice == 2:
        print("1. mg\t2. mg\t3. kg")
        unit_ch = int(input("Enter intial unit (1-3) : "))
        weight_converter(unit_ch,value)
    
    elif choice == 3:
        print("1. ml\t2. L")
        unit_ch = int(input("Enter intial unit (1-2) : "))
        liquid_converter(unit_ch,value)
'''
'''
# Integer Finder
for i in range(5):
    num = int(input("Enter your integer : "))
    if num < 0 :
        print("Integer Negative")
    elif num == 0:
        print("Integer is Zero")
    else:
        print("Integer Positive")
'''
'''
# Leap Year or Not

year = int(input("Enter the year : "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is Not Leap Year")
'''
'''
# Simple ATM

correct = 1234
pin = int(input("Enter your 4 digit PIN : "))
if pin == correct:
    withdraw = float(input("Enter the withdrawal amount : "))
    if withdraw <=5000:
        print("Dispensing Cash.......")
    else:
        print("Limit Exceeded!!!")
else:
    print("Invalid PIN")
'''
'''
# BMI Calculator

height = float(input("Enter your Height in cm : "))
weight = float(input("Enter your Weight in kg : "))
bmi = weight / ((height/100)**2)
print(f"BMI : {bmi:.2f}")

if bmi < 18.5:
    print("Category : Underweight")
elif bmi < 25:
    print("Category : Normal weight")
elif bmi < 30:
    print("Category : Overweight")
else:
    print("Category : Obesity")

print("=======================================")    
print("Thank you for using our BMI Calculator")
print("=======================================")
'''
'''
temp = float(input("Enter the temperature in Celsius : "))
if temp < 0:
    print("Wear a Heavy Coat")
elif temp < 15:
    print("Wear a Jacket")
elif temp < 30:
    print("Comfortable Weather")
else:
    print("Wear Light Clothing adn stay hydrated")
'''
'''
# Loan Eligibility Checker

month_inc = float(input("Enter your monthly income : "))
exis_emi = float(input("Enter your existing EMI : "))

if month_inc < 30000:
    print("Income Too Low")
elif month_inc >= 30000 and (exis_emi < 0.4*month_inc):
    print("Eligible for Loan")
elif exis_emi >= 0.4*month_inc :
    print("High debt burden")
'''
'''
# Number Guessing Hint Program

sec_num = 42
guess = int(input("Enter your Guess Number : "))

if guess < sec_num:
    print("Too Low")
    print(f"You are below {sec_num-guess} the number")
elif guess == sec_num:
    print("Correct!!!!")
elif guess > sec_num:
    print("Too High")
    print(f"Your are above {guess-sec_num} the number")
'''
'''
# Student's performance

marks = int(input("Enter your marks : "))

if marks >= 40:
    print("Pass!!")
    if marks >= 90:
        print("Distinction")
    elif marks >= 75:
        print("First Division")
    elif marks >= 60:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail!!")
'''
'''
# Job Application Screener

age = int(input("Enter your age : "))
degree = input("Degree : ")
cgpa = float(input("Enter your cgpa : "))

if 21 < age < 40:
    if degree.upper() in ['MCA','BTECH'] and cgpa >= 7.0 :
        print("Interview Shortlisted")
    else:
        print("Either Degree or cgpa doesn't meet the criteria")
else:
    print("Your age does not meet the criteria")
'''
'''
# E-Commerce Discount Calculator

cart = float(input("Enter the original price of cart : "))

if cart > 5000:
    prem = input("Are you a premium user [y/n] : ")
    if prem.lower() == 'y':
        print(f"Original Price : {cart}")
        print(f"Discount 20% : {cart*0.2}")
        print(f"Final Price : {cart-(cart*0.2)}")
    else:
        print(f"Original Price : {cart}")
        print(f"Discount 15% : {cart*0.15}")
        print(f"Final Price : {cart-(cart*0.15)}")
else:
    print(f"Original Price : {cart}")
    print(f"Discount 5% : {cart*0.05}")
    print(f"Final Price : {cart-(cart*0.05)}")
'''
'''
# University Grading System

name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))

subjects = int(input("Enter Number of Subjects: "))

total_marks = 0
max_marks = subjects * 100

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks in Subject {i} (out of 100): "))
    total_marks += marks

attendance = float(input("Enter Attendance Percentage: "))

percentage = (total_marks / max_marks) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

if attendance >= 75:
    attendance_status = "Eligible"

else:
    attendance_status = "Not Eligible due to low attendance"

if percentage >= 50 and attendance >= 75:
    result = "PASS"

else:
    result = "FAIL"

print("\n=================== STUDENT RESULT ====================")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total_marks, "/", max_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Attendance:", attendance, "%")
print("Attendance Status:", attendance_status)
print("Final Result:", result)
print("=======================================================")
'''
'''
# Multi-Subject Report Card

subjects = ['Hindi','English','Maths','Science','Computer']
marks = []

for i in subjects:
    m = int(input(f"Enter {i} marks (out of 100) : "))
    marks.append(m)

perc = (sum(marks)/(len(marks)*100))*100

print(f"Total Marks : {sum(marks)}")
print(f"Percentage : {perc}")

failed = [subjects[i] for i in range(len(marks)) if marks[i]<33]
print(f"Failed Subjects are : {failed}")
'''