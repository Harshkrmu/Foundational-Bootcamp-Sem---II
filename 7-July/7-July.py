import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# data  =  {'A':  [1 ,  2 ,  3],'B':  [4 ,  5 ,  6]}
# df  =  pd. DataFrame ( data)
# print( df  +  2)
# print( df  -  2)
# print( df  *  2)
# print( df  /  2)

# print( df  >  2)
# print( df  ==  4)

# data  =  {'A':  [ True ,  False ,  True ],'B':  [ False ,  False , True ]}
# df  =  pd. DataFrame ( data)

# print( df & df)
# print( df  |  df)
# print(~ df)

# data  =  {'A':  [1 ,  2 ,  3],  'B':  [4 ,  5 ,  6]}
# df  =  pd. DataFrame ( data) 
# s  =  pd. Series ([1 ,  2 ,  3])

# print( df. add (s,  axis =0))
# print( df. add (s,  axis =1))

# data  =  {'A':  [1 ,  2 ,  3],  'B':  [4 ,  5 ,  6]}
# df  =  pd. DataFrame ( data)
# print(df.apply(lambda  x:  x  *  2))
# print(df.map(lambda  x:  x  *  2))


# # Matplotlib

# data = {
#     'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
#     'Sales': [2500, 4000, 6000, 2300, 6070, 4500, 1000]   
# }

# df = pd.DataFrame(data)

# plt.plot(df['Month'], df['Sales'], marker = 'o')
# plt.title('Monthly Sales')
# plt.xlabel('Month')
# plt.ylabel('Sales')
# plt.grid(True)
# plt.show()

# data = {
#     'Region': ['North', 'South', 'East', 'West'],
#     'Sales': [25000, 15000, 10000, 34000]   
# }

# df = pd.DataFrame(data)

# plt.bar(df['Region'], df['Sales'], color = 'skyblue')
# plt.title('Sales by Region')
# plt.xlabel('Region')
# plt.ylabel('Sales')
# plt.grid(axis = 'y' )
# plt.show()

# dates = pd.date_range(start='2025-01-01' , periods = 6, freq='ME')
# revenue = np.random.randint(2000, 5000, size=6)

# df = pd.DataFrame({'Date': dates, 'Revenue': revenue})

# plt.plot(df['Date'], df['Revenue'], marker='o', linestyle='-', color='green')
# plt.title('Monthly Revenue')
# plt.xlabel('Date')
# plt.ylabel('Revenue')
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Bar Graph

# values = [5, 6, 3, 7, 2]
# names = ["A","B","C","D","E"]
# plt.bar(names, values, color="green")
# plt.show()

# # Horizontal Bar Graph

# values = [5,6,3,7,2]
# names = ["A","B","C","D","E"]
# plt.barh(names, values, color="yellowgreen")
# plt.show()

# # Pie Chart

# cars =['AUDI','BMW','FORD','TESLA','JAGUAR','MERCEDES']
# data =[23, 17, 35, 29, 12, 41]

# fig =plt.figure(figsize=(10, 7))
# plt.pie(data, labels=cars)
# plt.show()

# # Boxplot()

# np.random.seed(15)
# dataSet = np.random.normal(100, 25, 200)
# print(dataSet)
# figure = plt.figure(figsize =(10, 8))
# plt.boxplot(dataSet)
# plt.show()

# # Histogram

# ages=[2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
# range = (0, 100)
# bins = 10

# plt.hist(ages, bins, range, color='green',histtype='bar',rwidth=0.8)
# plt.xlabel('age')
# plt.ylabel('No. of people')
# plt.title('My histogram')
# plt.show()

# # Line Graph

# x = np.array([1,2,3,4])
# y = x*2
# plt.plot(x,y)
# plt.show

# # Scatter Plot

# x_axis_value =[6, 7, 9, 8, 2,16, 3, 6,4,14,13, 4,1]
# y_axis_value =[98, 87, 84, 86, 99, 85,102, 89, 96, 78, 77, 83, 81]
# plt.scatter(x_axis_value, y_axis_value)
# plt.show()

# # Multiple Subplots using plt.subplots

# fig, ax = plt.subplots(3, 3)

# for i in ax:
#     for j in i:
#         j.plot(np.random.randint(0, 5, 5),np.random.randint(0, 5, 5))
# plt.show()

# fig, ax = plt.subplots(2, 2)
# x = np.linspace(0, 10, 1000)

# ax[0, 0].plot(x, np.sin(x),'r-.')
# ax[0, 1].plot(x, np.cos(x),'g--')
# ax[1, 0].plot(x, np.tan(x),'y-')
# ax[1, 1].plot(x, np.sinc(x),'c.-')
# plt.show()

# # Activity 

# # -----------------------------
# # LEVEL 1: BAR CHART
# # -----------------------------

# bird_species = ['Sparrow', 'Pigeon', 'Crow', 'Parrot', 'Myna']
# sightings = [120, 95, 150, 70, 110]

# df1 = pd.DataFrame({
#     'Species': bird_species,
#     'Sightings': sightings
# })

# # Sort from highest to lowest
# df1 = df1.sort_values(by='Sightings', ascending=False)

# plt.figure(figsize=(8,5))
# plt.bar(df1['Species'], df1['Sightings'], color='skyblue')
# plt.title("Bird Species Sightings")
# plt.xlabel("Bird Species")
# plt.ylabel("Total Sightings")
# plt.show()

# # Most common species
# most_common = df1.iloc[0]['Species']
# print("Most Common Species:", most_common)

# # -----------------------------
# # LEVEL 2: LINE GRAPH
# # -----------------------------

# time = ['6 AM', '8 AM', '10 AM', '12 PM', '2 PM', '4 PM', '6 PM']

# bird_activity = [90, 80, 65, 40, 35, 55, 85]
# human_traffic = [15, 30, 60, 95, 100, 70, 25]

# plt.figure(figsize=(9,5))

# plt.plot(time, bird_activity, marker='o', linewidth=2,label='Bird Activity')

# plt.plot(time, human_traffic, marker='s', linewidth=2,label='Human Foot Traffic')

# plt.title("Bird Activity vs Human Foot Traffic")
# plt.xlabel("Time of Day")
# plt.ylabel("Activity Level")
# plt.legend()
# plt.grid(True)
# plt.show()


# # -----------------------------
# # LEVEL 3: SCATTER PLOT
# # -----------------------------

# np.random.seed(42)

# tree_density = np.random.randint(50, 300, 20)
# species_diversity = np.random.uniform(1, 10, 20)

# zones = pd.DataFrame({
#     'Tree Density': tree_density,
#     'Species Diversity': species_diversity
# })

# plt.figure(figsize=(8,6))
# plt.scatter(
#     zones['Tree Density'],
#     zones['Species Diversity'],
#     color='green',
#     s=80
# )

# plt.title("Tree Density vs Species Diversity")
# plt.xlabel("Tree Density")
# plt.ylabel("Species Diversity Index")
# plt.grid(True)
# plt.show()

# # -----------------------------
# # EXTENSION: BUBBLE CHART
# # -----------------------------

# tree_age = np.random.randint(10, 80, 20)

# plt.figure(figsize=(8,6))
# plt.scatter(
#     zones['Tree Density'],
#     zones['Species Diversity'],
#     s=tree_age * 10,
#     alpha=0.6,
#     color='orange'
# )

# plt.title("Bubble Chart: Tree Density vs Species Diversity")
# plt.xlabel("Tree Density")
# plt.ylabel("Species Diversity Index")
# plt.grid(True)
# plt.show()