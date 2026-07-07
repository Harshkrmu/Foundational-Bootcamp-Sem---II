import pandas as pd
import numpy as np

# df = pd.read_csv("19-June.csv")
# print(df)

# df.to_csv('19-June.csv', index= False)
# print(df)

# data  =  {
#     'Name':  ['John',  'Anna',  'Peter',  'Linda'], 
#     'Age':  [28 ,  24 ,  35 ,  32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
#          }
# df = pd.DataFrame(data)
# print( df)

# print(df['Name'])

# df['Salary'] = [70000 , 80000 , 120000 , 90000]
# print(df)

# print(df.describe())

# df_sorted = df.sort_values(by='Age')
# print(df_sorted)

# df_filtered = df[df['Age'] > 30]
# df_filtered = df['Age'][df['Age'] > 30] 
# df_filtered = df[df['Age'] > 30][['Age']]
# df_filtered = df[['Age']][df['Age'] > 30]
# print(df_filtered)

# print(df.loc[1:3])
# print(df.iloc[2])
# print(df.iloc[1:3])

# # Problem 5

# np.random.seed(42)

# students = 100

# names = [f"Student_{i}" for i in range(1, students + 1)]

# df = pd.DataFrame({
#     "Roll": range(1, students + 1),
#     "Name": names,
#     "Python": np.random.randint(35, 101, students),
#     "Java": np.random.randint(35, 101, students),
#     "ML": np.random.randint(35, 101, students),
#     "Cloud": np.random.randint(35, 101, students),
#     "Attendance": np.random.randint(60, 101, students)
# })

# print("Student Data:\n")
# print(df.head())

# df["Total"] = df[["Python", "Java", "ML", "Cloud"]].sum(axis=1)

# df["Percentage"] = df["Total"] / 400 * 100

# def grade(percent):
#     if percent >= 90:
#         return "A+"
#     elif percent >= 80:
#         return "A"
#     elif percent >= 70:
#         return "B"
#     elif percent >= 60:
#         return "C"
#     elif percent >= 40:
#         return "D"
#     else:
#         return "F"

# df["Grade"] = df["Percentage"].apply(grade)

# df["Rank"] = df["Total"].rank(method="dense", ascending=False).astype(int)

# top10 = df.sort_values(by="Total", ascending=False).head(10)

# print("\nTop 10 Students")
# print(top10[["Roll", "Name", "Total", "Percentage", "Rank"]])

# below40 = (
#     (df[["Python", "Java", "ML", "Cloud"]] < 40)
#     .sum(axis=1) >= 2
# )

# print("\nStudents below 40 marks in at least two subjects")
# print(df[below40][["Roll", "Name", "Python", "Java", "ML", "Cloud"]])

# subjects = ["Python", "Java", "ML", "Cloud"]

# print("\nDepartment Toppers")

# for sub in subjects:
#     topper = df.loc[df[sub].idxmax()]
#     print(f"{sub}: {topper['Name']} ({topper[sub]} Marks)")

# print("\nStudents with Attendance below 75%")
# print(df[df["Attendance"] < 75][["Roll", "Name", "Attendance"]])

# top10.to_csv("Topper_List.csv", index=False)

# print("\nTopper list exported successfully as 'Topper_List.csv'")

# # Problem 6

# np.random.seed(42)

# n = 500

# departments = ["IT", "HR", "Finance", "Marketing", "Sales"]

# df = pd.DataFrame({
#     "EmpID": np.arange(1001, 1001 + n),
#     "Department": np.random.choice(departments, n),
#     "Experience": np.random.randint(1, 31, n),      # 1-30 years
#     "Salary": np.random.randint(30000, 150001, n),  # ₹30,000 - ₹1,50,000
#     "Performance": np.random.randint(1, 6, n)       # Ratings 1-5
# })

# df.to_csv("employees.csv", index=False)

# df.to_excel("employees.xlsx", index=False)

# print("CSV and Excel files created successfully.")

# csv_data = pd.read_csv("employees.csv")
# excel_data = pd.read_excel("employees.xlsx")

# print("\nAre both files identical?")
# print(csv_data.equals(excel_data))

# print("\nAverage Salary Department-wise:")
# print(df.groupby("Department")["Salary"].mean())

# highest = df[df["Performance"] == df["Performance"].max()]
# print("\nHighest Performer(s):")
# print(highest)

# dept_avg = df.groupby("Department")["Salary"].transform("mean")

# above_avg = df[df["Salary"] > dept_avg]

# print("\nEmployees earning more than department average:")
# print(above_avg)

# filtered = df[(df["Experience"] > 15) & (df["Performance"] < 3)]

# print("\nEmployees with Experience >15 and Performance <3:")
# print(filtered)

# df["Bonus"] = np.where(df["Performance"] >= 4,
#                        df["Salary"] * 0.10,
#                        df["Salary"] * 0.05)

# print("\nDataset with Bonus column:")
# print(df.head())

# bonus_above = df[df["Bonus"] > 10000]

# bonus_above.to_csv("bonus_above_10000.csv", index=False)

# print("\nEmployees receiving Bonus above ₹10,000 exported successfully.")
# print(bonus_above)