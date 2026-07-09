# # ===============================================
# # Q4. Urban Mobility & Traffic Flow Optimization
# # ===============================================

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime, timedelta
# import random

# random.seed(42)
# np.random.seed(42)

# num_vehicles = 100
# points_per_vehicle = 300

# rows = []

# start_lat = 28.6139
# start_lon = 77.2090
# start_time = datetime(2024, 1, 1, 6, 0, 0)

# for vehicle in range(1, num_vehicles + 1):

#     lat = start_lat + random.uniform(-0.05, 0.05)
#     lon = start_lon + random.uniform(-0.05, 0.05)
#     current_time = start_time + timedelta(minutes=random.randint(0, 120))

#     for i in range(points_per_vehicle):

#         speed = max(5, np.random.normal(35, 12))

#         lat += np.random.normal(0, 0.0004)
#         lon += np.random.normal(0, 0.0004)

#         rows.append([
#             f"TX{vehicle:03d}",
#             current_time,
#             round(lat, 6),
#             round(lon, 6),
#             round(speed, 2)
#         ])

#         current_time += timedelta(seconds=30)

# df = pd.DataFrame(
#     rows,
#     columns=[
#         "VehicleID",
#         "Timestamp",
#         "Latitude",
#         "Longitude",
#         "Speed"
#     ]
# )

# df.to_csv("taxi_gps_dataset.csv", index=False)

# gps = pd.read_csv("taxi_gps_dataset.csv")

# gps["Timestamp"] = pd.to_datetime(gps["Timestamp"])

# gps = gps.sort_values(["VehicleID", "Timestamp"])

# gps["Prev_Latitude"] = gps.groupby("VehicleID")["Latitude"].shift(1)
# gps["Prev_Longitude"] = gps.groupby("VehicleID")["Longitude"].shift(1)
# gps["Prev_Time"] = gps.groupby("VehicleID")["Timestamp"].shift(1)

# R = 6371

# lat1 = np.radians(gps["Prev_Latitude"])
# lon1 = np.radians(gps["Prev_Longitude"])
# lat2 = np.radians(gps["Latitude"])
# lon2 = np.radians(gps["Longitude"])

# dlat = lat2 - lat1
# dlon = lon2 - lon1

# a = (
#     np.sin(dlat / 2) ** 2
#     + np.cos(lat1) * np.cos(lat2)
#     * np.sin(dlon / 2) ** 2
# )

# c = 2 * np.arcsin(np.sqrt(a))

# gps["Distance_km"] = R * c

# gps["TimeDiff_hr"] = (
#     gps["Timestamp"] - gps["Prev_Time"]
# ).dt.total_seconds() / 3600

# gps["Calculated_Speed"] = (
#     gps["Distance_km"] / gps["TimeDiff_hr"]
# )

# gps["Calculated_Speed"] = gps["Calculated_Speed"].replace(
#     [np.inf, -np.inf],
#     np.nan
# )

# gps["Calculated_Speed"] = gps["Calculated_Speed"].fillna(0)

# gps["Grid_Lat"] = gps["Latitude"].round(3)
# gps["Grid_Lon"] = gps["Longitude"].round(3)

# gps = gps.dropna().reset_index(drop=True)

# print("Dataset Shape")
# print(gps.shape)

# print()

# print(gps.head())

# print()

# print(gps.describe())

# speed_bins = [0, 20, 40, np.inf]

# traffic_labels = [
#     "Gridlock",
#     "Slow",
#     "Free-Flow"
# ]

# gps["Traffic_Category"] = np.digitize(
#     gps["Calculated_Speed"],
#     speed_bins
# )

# traffic_map = {
#     1: "Gridlock",
#     2: "Slow",
#     3: "Free-Flow"
# }

# gps["Traffic_Category"] = gps["Traffic_Category"].map(
#     traffic_map
# )


# gps["Acceleration"] = (
#     gps.groupby("VehicleID")["Calculated_Speed"]
#     .transform(
#         lambda x: np.append(
#             np.diff(x),
#             np.nan
#         )
#     )
# )


# grid_analysis = (
#     gps.groupby(
#         [
#             "Grid_Lat",
#             "Grid_Lon"
#         ]
#     )
#     .agg(
#         Average_Speed=(
#             "Calculated_Speed",
#             "mean"
#         ),

#         Total_Vehicles=(
#             "VehicleID",
#             "count"
#         ),

#         Average_Acceleration=(
#             "Acceleration",
#             "mean"
#         )
#     )
#     .reset_index()
# )


# grid_analysis["Congestion_Index"] = (
#     grid_analysis["Total_Vehicles"]
#     /
#     (grid_analysis["Average_Speed"] + 1)
# )


# hour_analysis = (
#     gps.assign(
#         Hour=gps["Timestamp"].dt.hour
#     )
#     .groupby("Hour")
#     .agg(
#         Average_Speed=(
#             "Calculated_Speed",
#             "mean"
#         ),

#         Vehicle_Count=(
#             "VehicleID",
#             "count"
#         )
#     )
#     .reset_index()
# )


# day_analysis = (
#     gps.assign(
#         Day=gps["Timestamp"].dt.day_name()
#     )
#     .groupby("Day")
#     ["Calculated_Speed"]
#     .mean()
# )


# day_order = [
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# ]


# day_analysis = day_analysis.reindex(day_order)


# print("Traffic Category Count")
# print(
#     gps["Traffic_Category"].value_counts()
# )


# print("\nMost Congested Areas")
# print(
#     grid_analysis
#     .sort_values(
#         "Congestion_Index",
#         ascending=False
#     )
#     .head(10)
# )


# print("\nPeak Congestion Hours")
# print(
#     hour_analysis
#     .sort_values(
#         "Average_Speed"
#     )
#     .head(10)
# )


# print("\nAcceleration Statistics")
# print(
#     gps["Acceleration"].describe()
# )


# grid_analysis.to_csv(
#     "grid_congestion_analysis.csv",
#     index=False
# )


# hour_analysis.to_csv(
#     "hourly_traffic_analysis.csv",
#     index=False
# )


# day_analysis.to_csv(
#     "daily_speed_analysis.csv"
# )


# print("\nFiles Created:")
# print("grid_congestion_analysis.csv")
# print("hourly_traffic_analysis.csv")
# print("daily_speed_analysis.csv")

# plt.figure(figsize=(10,8))

# scatter = plt.scatter(
#     grid_analysis["Grid_Lon"],
#     grid_analysis["Grid_Lat"],
#     c=grid_analysis["Congestion_Index"],
#     s=grid_analysis["Total_Vehicles"] * 2,
#     cmap="RdYlGn_r",
#     alpha=0.7
# )

# plt.colorbar(
#     scatter,
#     label="Congestion Index"
# )

# plt.xlabel("Longitude")
# plt.ylabel("Latitude")

# plt.title(
#     "Urban Traffic Congestion Hotspots"
# )

# plt.grid(True)

# plt.show()



# days = day_analysis.index.tolist()

# speed_values = day_analysis.values.tolist()

# speed_values.append(speed_values[0])

# angles = np.linspace(
#     0,
#     2*np.pi,
#     len(days),
#     endpoint=False
# )

# angles = np.concatenate(
#     [
#         angles,
#         [angles[0]]
#     ]
# )


# fig = plt.figure(
#     figsize=(8,8)
# )

# ax = plt.subplot(
#     111,
#     polar=True
# )


# ax.plot(
#     angles,
#     speed_values,
#     linewidth=2,
#     color="blue"
# )


# ax.fill(
#     angles,
#     speed_values,
#     alpha=0.25,
#     color="blue"
# )


# ax.set_xticks(
#     angles[:-1]
# )


# ax.set_xticklabels(
#     days
# )


# ax.set_title(
#     "Average Taxi Speed Across Days"
# )


# plt.show()



# plt.figure(figsize=(10,5))

# plt.plot(
#     hour_analysis["Hour"],
#     hour_analysis["Average_Speed"],
#     marker="o"
# )

# plt.xlabel(
#     "Hour of Day"
# )

# plt.ylabel(
#     "Average Speed (km/h)"
# )

# plt.title(
#     "Traffic Speed Variation During Day"
# )

# plt.grid(True)

# plt.show()



# print("\nFinal Traffic Summary")

# print("--------------------")

# print(
#     "Total Vehicles:",
#     gps["VehicleID"].nunique()
# )


# print(
#     "Total GPS Records:",
#     len(gps)
# )


# print(
#     "Average Speed:",
#     round(
#         gps["Calculated_Speed"].mean(),
#         2
#     ),
#     "km/h"
# )


# print(
#     "Maximum Speed:",
#     round(
#         gps["Calculated_Speed"].max(),
#         2
#     ),
#     "km/h"
# )


# print(
#     "Minimum Speed:",
#     round(
#         gps["Calculated_Speed"].min(),
#         2
#     ),
#     "km/h"
# )


# print(
#     "\nMost Common Traffic Condition:"
# )

# print(
#     gps["Traffic_Category"]
#     .mode()[0]
# )


# gps.to_csv(
#     "final_processed_taxi_data.csv",
#     index=False
# )


# print(
#     "\nFinal dataset saved as final_processed_taxi_data.csv"
# )

# # =======================================================================
# # Q5. Telecommunications Customer Churn & Predictive Feature Engineering
# # =======================================================================

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from pandas.api.types import is_numeric_dtype

# np.random.seed(42)


# num_customers = 1000


# df = pd.DataFrame({

#     "CustomerID": [
#         f"CUST{i:04d}" for i in range(1, num_customers + 1)
#     ],

#     "Gender": np.random.choice(
#         ["Male", "Female"],
#         num_customers
#     ),

#     "SeniorCitizen": np.random.choice(
#         [0, 1],
#         num_customers,
#         p=[0.8, 0.2]
#     ),

#     "Tenure": np.random.randint(
#         1,
#         73,
#         num_customers
#     ),

#     "ContractType": np.random.choice(
#         [
#             "Month-to-month",
#             "One year",
#             "Two year"
#         ],
#         num_customers
#     ),

#     "InternetService": np.random.choice(
#         [
#             "DSL",
#             "Fiber optic",
#             "No"
#         ],
#         num_customers
#     ),

#     "PaymentMethod": np.random.choice(
#         [
#             "Electronic check",
#             "Mailed check",
#             "Bank transfer",
#             "Credit card"
#         ],
#         num_customers
#     ),

#     "MonthlyCharges": np.round(
#         np.random.uniform(
#             20,
#             120,
#             num_customers
#         ),
#         2
#     ),

#     "StreamingTV": np.random.choice(
#         ["Yes", "No"],
#         num_customers
#     ),

#     "OnlineSecurity": np.random.choice(
#         ["Yes", "No"],
#         num_customers
#     )

# })


# df["TotalCharges"] = (
#     df["Tenure"] *
#     df["MonthlyCharges"]
# ).round(2)


# churn_score = (
#     (df["Tenure"] < 12).astype(int)
#     +
#     (df["ContractType"] == "Month-to-month").astype(int)
#     +
#     (df["MonthlyCharges"] > 90).astype(int)
# )


# df["Churn"] = np.where(
#     churn_score >= 2,
#     "Yes",
#     np.where(
#         np.random.random(num_customers) < 0.2,
#         "Yes",
#         "No"
#     )
# )


# df.to_csv(
#     "telecom_churn.csv",
#     index=False
# )


# df = pd.read_csv(
#     "telecom_churn.csv"
# )


# print("Dataset Preview")
# print(df.head())


# print("\nDataset Information")
# print(df.info())


# print("\nMissing Values")
# print(df.isnull().sum())



# for col in df.columns:

#     if is_numeric_dtype(df[col]):

#         df[col] = df[col].fillna(
#             df[col].median()
#         )

#     else:

#         df[col] = df[col].fillna(
#             df[col].mode()[0]
#         )



# df["Tenure_Group"] = pd.qcut(
#     df["Tenure"],
#     q=4,
#     labels=[
#         "Low",
#         "Medium",
#         "High",
#         "Very High"
#     ]
# )



# charges = df["TotalCharges"].values


# Q1 = np.percentile(
#     charges,
#     25
# )


# Q3 = np.percentile(
#     charges,
#     75
# )


# IQR = Q3 - Q1


# lower_limit = Q1 - (1.5 * IQR)


# upper_limit = Q3 + (1.5 * IQR)


# outliers = df[
#     (df["TotalCharges"] < lower_limit)
#     |
#     (df["TotalCharges"] > upper_limit)
# ]


# print("\nOutlier Count:")
# print(len(outliers))


# print("\nOutlier Samples")
# print(outliers.head())



# churned = df[
#     df["Churn"] == "Yes"
# ]


# retained = df[
#     df["Churn"] == "No"
# ]



# numeric_features = [
#     "Tenure",
#     "MonthlyCharges",
#     "TotalCharges",
#     "SeniorCitizen"
# ]


# for col in df.select_dtypes(
#     include=np.number
# ).columns:

#     if col not in numeric_features:

#         numeric_features.append(col)



# numeric_features = numeric_features[:9]



# fig, axes = plt.subplots(
#     3,
#     3,
#     figsize=(15, 12)
# )


# axes = axes.flatten()


# for i, col in enumerate(numeric_features):

#     axes[i].hist(
#         churned[col],
#         bins=20,
#         alpha=0.5,
#         color="red",
#         label="Churned"
#     )


#     axes[i].hist(
#         retained[col],
#         bins=20,
#         alpha=0.5,
#         color="green",
#         label="Retained"
#     )


#     axes[i].set_title(
#         col + " Distribution"
#     )


#     axes[i].set_xlabel(
#         col
#     )


#     axes[i].set_ylabel(
#         "Number of Customers"
#     )


#     axes[i].legend()



# for j in range(
#     len(numeric_features),
#     9
# ):

#     fig.delaxes(
#         axes[j]
#     )


# plt.suptitle(
#     "Customer Feature Distribution: Churned vs Retained",
#     fontsize=16
# )


# plt.tight_layout()

# plt.show()



# box_features = [
#     "Tenure",
#     "MonthlyCharges",
#     "TotalCharges"
# ]


# fig, axes = plt.subplots(
#     1,
#     3,
#     figsize=(15, 5)
# )



# for i, col in enumerate(box_features):

#     axes[i].boxplot(
#         [
#             churned[col],
#             retained[col]
#         ],
#         labels=[
#             "Churned",
#             "Retained"
#         ]
#     )


#     axes[i].set_title(
#         col
#     )


# plt.suptitle(
#     "Churn vs Retained Boxplots"
# )


# plt.show()



# df_encoded = pd.get_dummies(
#     df,
#     drop_first=True
# )



# df_encoded.to_csv(
#     "telecom_feature_matrix.csv",
#     index=False
# )



# print("\nFinal Feature Matrix Shape:")
# print(df_encoded.shape)


# print("\nChurn Percentage:")

# print(
#     round(
#         (len(churned) / len(df)) * 100,
#         2
#     ),
#     "%"
# )


# print("\nFiles Created:")
# print("telecom_churn.csv")
# print("telecom_feature_matrix.csv")