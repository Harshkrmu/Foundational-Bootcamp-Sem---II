'''
# student report designer
student_name = input("Enter your name : ")
roll_number = int(input("Enter your Roll No. : "))
age = int(input("Enter your age : "))
program = input("Enter your program : ")
cgpa = float(input("Enter your CGPA : "))
courses = int(input("Enter Number of completed courses : "))

rem_courses = 40 - courses
comp_percent = (courses/40)*100

print("\n========STUDENT REPORT========")
print(f"Name        : {student_name}")
print(f"Roll Number : {roll_number}")
print(f"Age         : {age}")
print(f"Program     : {program}")
print(f"CGPA        : {cgpa}\n")
print(f"Completed Courses : {courses}")
print(f"Remaining Courses : {rem_courses}")
print(f"Degree Completion : {comp_percent}\n")
if cgpa >= 8.5:
    print("🎉🎉🎉Eligible for Degree🎉🎉🎉")
else:
    print("👎👎👎Not Eligible for Degree👎👎👎")
print("==============================")
'''
'''
# Monthly expense calculator
month_budg = int(input("Enter your Monthly Budget : "))
food_exp = int(input("Enter your Monthly Food Expense : "))
travel_exp = int(input("Enter your Monthly Travel Expense : "))
internet_bill = int(input("Enter your Monthly Internet Bill : "))
entertain_exp = int(input("Enter your Monthly Entertainment Expense : "))
misce_exp = int(input("Enter your Monthly Miscellaneous Expense : "))
total = food_exp + travel_exp + internet_bill + entertain_exp + misce_exp
rem_bal = month_budg - total
perc_spent = (total/month_budg)*100

print("\n==========TOTAL MONTHLY EXPENSE==========")
print(f"Monthly Budget : {month_budg}\n\n")
print(f"Total Expense  : {total}")
print(f"Balance Left   : {rem_bal}")
print(f"Spent          : {perc_spent:.2f}%\n")
if perc_spent > 80:
    print("Your Spending exceeds 80% of Monthly Budget")
print("==========================================")
'''
'''
# Grade Calculator
math = int(input("Enter your Mathematics marks : "))
phy = int(input("Enter your Physics marks : "))
chem = int(input("Enter your Chemistry marks : "))
eng = int(input("Enter your English marks : "))
comp_sci = int(input("Enter your Computer Science marks : "))
total = math + phy + chem + eng + comp_sci
perc = (total/500)*100
print("\n===GRADE CALCULATOR===")
print(f"Total Marks : {total}/500")
if perc >= 80 :
    print("A")
elif perc >= 70 :
    print("B")
elif perc >= 60 :
    print("C")
elif perc >= 50 :
    print("D")
else:
    print("E")
print("======================")
'''
'''
# Digital Shopping Cart
n = int(input("Enter No. of Products : "))
l=[]
d={}
for i in range(n):
    p=[]
    prod_name = input(f"Enter {i+1} product name : ")
    quantity = int(input(f"Enter {i+1} product quantity : "))
    price = int(input(f"Enter {i+1} product price : "))
    item_total = quantity * price
    p.extend([prod_name,quantity,price,item_total])
    d[i+1] = p
    l.append(item_total)
sub_tot = sum(l)
gst = int((18/100)*sub_tot)
total = int(sub_tot + gst)
print("======DIGITAL SHOPPING CART======\n")
for i in d:
    print(f"{d[i][0]} {d[i][1]}x{d[i][2]} = {d[i][3]}\n")
print(f"\nSubTotal    : {sub_tot}")
print(f"GST         : {gst}")
print(f"TOTAL       : {total}\n")
if total > 50000 :
    print("Discount Applied 10%\n")
    print(f"Final Bill  : {int(total-((10/100)*total))}\n")
if total > 25000 and total < 50000:
    print("Discount Applied 5%\n")
    print(f"Final Bill  : {int(total-((5/100)*total))}\n")
if total < 25000:
    print("No Discount Applied as Total is less than 25000")
print("=====================================")
'''
'''
# Student Performance Dashboard

def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter Marks for Subject {i} out of 100 : "))
    marks.append(mark)

attendance = float(input("Enter Attendance Percentage: "))
assignment = float(input("Enter Assignment Score (out of 100): "))

academic_percentage = sum(marks) / 5

if attendance >= 75:
    attendance_status = "Eligible"
else:
    attendance_status = "Low Attendance"

internal_assessment = assignment * 0.20

final_score = (academic_percentage * 0.80) + internal_assessment

grade = calculate_grade(final_score)

if final_score >= 40:
    result = "PASS"
else:
    result = "FAIL"

if final_score >= 75 and attendance >= 80:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

if final_score >= 90:
    rank = "Top Performer"
elif final_score >= 75:
    rank = "Good Performer"
else:
    rank = "Average"

if academic_percentage >= 75:
    distinction = "Yes"
else:
    distinction = "No"

print("\n" + "=" * 40)
print("      STUDENT PERFORMANCE DASHBOARD")
print("=" * 40)

print("Student Name :", name)
print("Roll Number  :", roll)

print("\nMarks Summary")
for i in range(5):
    print(f"Subject {i+1}: {marks[i]}")

print("\nAverage :", round(academic_percentage, 2))
print("Grade   :", grade)

print("\nAttendance :", attendance, "%")
print("Status     :", attendance_status)

print("\nPerformance Index :", round(final_score, 2))

print("\nResult :", result)

print("\nBonus Features")
print("Scholarship Eligibility :", scholarship)
print("Rank Category           :", rank)
print("Distinction Certificate :", distinction)

print("=" * 40)
''' 