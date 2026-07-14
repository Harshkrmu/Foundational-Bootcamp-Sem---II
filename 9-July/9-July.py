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

# # =======================================================
# # Q6. Supply Chain Logistics & Inventory Risk Assessment
# # =======================================================

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # -------------------------------------------------------------------------
# # 0. SETUP & MOCK DATA GENERATION
# # -------------------------------------------------------------------------
# # Seed for reproducibility
# np.random.seed(42)

# # Generate a 60-day timeline for 2 different SKUs across 2 Warehouses
# dates = pd.date_range(start="2026-01-01", periods=60, freq="D")
# skus = ["SKU_1001", "SKU_1002"]
# warehouses = ["WH_EAST", "WH_WEST"]

# inventory_records = []
# forecast_records = []

# for sku in skus:
#     for wh in warehouses:
#         # Establish structural baselines for this specific inventory pair
#         safety_stock = np.random.choice([30, 50, 75])
#         lead_time = np.random.choice([2, 4, 5])
#         current_stock = safety_stock * 1.5  # Start with healthy stock

#         for dt in dates:
#             # 1. Generate Forecast Data
#             # Demand fluctuates dynamically (simulating volatile consumer patterns)
#             base_demand = np.random.randint(5, 25)
#             # Add a weekend spike or drop simulation
#             if dt.dayofweek in [5, 6]:
#                 base_demand = int(base_demand * np.random.choice([0.6, 1.4]))

#             forecast_records.append(
#                 {
#                     "Date": dt,
#                     "SkuID": sku,
#                     "WarehouseID": wh,
#                     "ForecastedDemand": base_demand,
#                 }
#             )

#             # 2. Generate Daily Inventory Snapshot Logs
#             # Simulate daily inventory depletion by demand
#             current_stock -= base_demand

#             # Simulate random inventory replenishment arrivals
#             if np.random.rand() > 0.75:
#                 # Reorder quantity arrives
#                 current_stock += np.random.choice([40, 60, 80])

#             daily_reorder_qty = np.random.choice([20, 40])

#             inventory_records.append(
#                 {
#                     "Date": dt,
#                     "SkuID": sku,
#                     "WarehouseID": wh,
#                     "CurrentStock": int(current_stock),
#                     "SafetyStockLevel": safety_stock,
#                     "DailyReorderQuantity": daily_reorder_qty,
#                     "LeadTimeDays": lead_time,
#                 }
#             )

# # Construct DataFrames
# inventory_df = pd.DataFrame(inventory_records)
# forecast_df = pd.DataFrame(forecast_records)

# print("--- Initial Data Profiles ---")
# print(f"Inventory Logs Shape: {inventory_df.shape}")
# print(f"Forecast Table Shape: {forecast_df.shape}\n")


# # -------------------------------------------------------------------------
# # TASK 1: PANDAS - MERGE, ROLLING WINDOWS & STOCKOUT RISK FLAG
# # -------------------------------------------------------------------------
# # Merge inventory snapshot table with the historical sales forecast table
# # We merge on Date, SkuID, and WarehouseID to maintain data granularity
# merged_df = pd.merge(
#     inventory_df, forecast_df, on=["Date", "SkuID", "WarehouseID"], how="inner"
# )

# # Sort values to ensure rolling windows calculate chronologically per item/location group
# merged_df = merged_df.sort_values(by=["SkuID", "WarehouseID", "Date"]).reset_index(
#     drop=True
# )

# # Compute 7-day and 30-day moving averages of demand grouped by Sku and Warehouse
# merged_df["Demand_7D_MA"] = (
#     merged_df.groupby(["SkuID", "WarehouseID"])["ForecastedDemand"]
#     .transform(lambda x: x.rolling(window=7, min_periods=1).mean())
# )

# merged_df["Demand_30D_MA"] = (
#     merged_df.groupby(["SkuID", "WarehouseID"])["ForecastedDemand"]
#     .transform(lambda x: x.rolling(window=30, min_periods=1).mean())
# )

# # Create a Boolean flag for "Stockout Risk"
# # True if Current Stock drops to or below the designated Safety Stock Level
# merged_df["StockoutRisk"] = (
#     merged_df["CurrentStock"] <= merged_df["SafetyStockLevel"]
# )


# # -------------------------------------------------------------------------
# # TASK 2: NUMPY - MULTI-TIER PRIORITY ASSIGNMENT VIA NP.SELECT
# # -------------------------------------------------------------------------
# # Define logic boundaries for restocking order priorities
# conditions = [
#     (merged_df["CurrentStock"] <= 0),  # Tier 1: Absolute Stockout
#     (merged_df["CurrentStock"] <= merged_df["SafetyStockLevel"])
#     & (merged_df["LeadTimeDays"] >= 4),  # Tier 2: Low safety buffer + high lead time
#     (merged_df["CurrentStock"] <= merged_df["SafetyStockLevel"]),  # Tier 3: Encroaching safety buffer
# ]

# choices = ["CRITICAL", "HIGH", "MEDIUM"]

# # Execute conditions; any row not meeting the criteria defaults to 'LOW' priority
# merged_df["RestockPriority"] = np.select(conditions, choices, default="LOW")


# # -------------------------------------------------------------------------
# # TASK 3: MATPLOTLIB - STEP-PLOT VISUALIZATION
# # -------------------------------------------------------------------------
# # Isolate a specific SKU and Warehouse slice for clean visualization plotting
# viz_df = merged_df[
#     (merged_df["SkuID"] == "SKU_1001") & (merged_df["WarehouseID"] == "WH_EAST")
# ].copy()

# plt.figure(figsize=(14, 7))

# # 1. Plot step-line showing daily stock variations
# plt.step(
#     viz_df["Date"],
#     viz_df["CurrentStock"],
#     where="mid",
#     color="#1f77b4",
#     linewidth=2.5,
#     label="Current Stock Level",
# )

# # 2. Add horizontal dashed line indicating the safety stock threshold
# safety_threshold_val = viz_df["SafetyStockLevel"].iloc[0]
# plt.axhline(
#     y=safety_threshold_val,
#     color="#ff7f0e",
#     linestyle="--",
#     linewidth=1.8,
#     label=f"Safety Stock Threshold ({safety_threshold_val})",
# )

# # 3. Add zero-baseline line to anchor the eye during stockout visual dips
# plt.axhline(y=0, color="black", linestyle=":", alpha=0.4)

# # 4. Filter data to locate specific points where stock dipped below zero
# stockout_events = viz_df[viz_df["CurrentStock"] < 0]

# # Highlight stockout dates with red marker flags
# plt.scatter(
#     stockout_events["Date"],
#     stockout_events["CurrentStock"],
#     color="#d62728",
#     marker="v",
#     s=120,
#     zorder=5,
#     label="Stockout Infraction (Stock < 0)",
# )

# # Polish Visual Aesthetics
# plt.title(
#     "SKU_1001 Stock Trajectory & Risk Vulnerability (WH_EAST)",
#     fontsize=14,
#     weight="bold",
#     pad=15,
# )
# plt.xlabel("Timeline", fontsize=11, labelpad=10)
# plt.ylabel("Inventory Quantity (Units)", fontsize=11, labelpad=10)
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="none")

# # Clean formatting for date labels on X-axis
# plt.gcf().autofmt_xdate()
# plt.tight_layout()

# # Display the final plot
# plt.show()

# # -------------------------------------------------------------------------
# # PREVIEW DATA OUTPUT
# # -------------------------------------------------------------------------
# print("--- Processed Output Preview (First 10 records for SKU_1001 @ WH_EAST) ---")
# columns_to_show = [
#     "Date",
#     "CurrentStock",
#     "SafetyStockLevel",
#     "ForecastedDemand",
#     "Demand_7D_MA",
#     "StockoutRisk",
#     "RestockPriority",
# ]
# print(viz_df[columns_to_show].head(10).to_string(index=False))

# # =====================================================================
# # Q7. Healthcare Electronic Health Records (EHR) Longitudinal Analysis
# # =====================================================================

# import io
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# csv_data = """PatientID,VisitDate,Systolic_BP,Diastolic_BP,Cholesterol,BloodSugar
# PAT_001,2024-01-10,120,80,190,95
# PAT_001,2024-02-15,125,82,,98
# PAT_001,2024-04-20,132,85,210,105
# PAT_001,2024-07-11,,88,,115
# PAT_001,2024-09-05,145,92,230,
# PAT_001,2025-01-15,155,95,245,130
# PAT_001,2025-05-22,162,100,,145
# PAT_002,2024-01-15,150,95,260,180
# PAT_002,2024-03-01,142,90,,160
# PAT_002,2024-05-20,135,85,220,130
# PAT_002,2024-08-12,128,82,200,110
# PAT_002,2024-11-05,,80,,95
# PAT_002,2025-03-18,122,78,185,90
# PAT_003,2024-02-01,118,75,175,85
# PAT_003,2024-05-14,120,,180,
# PAT_003,2024-08-22,,,178,90
# PAT_003,2024-11-30,122,78,,88
# PAT_003,2025-04-05,115,74,170,82"""

# df = pd.read_csv(io.StringIO(csv_data))
# df["VisitDate"] = pd.to_datetime(df["VisitDate"])
# df = df.sort_values(by=["PatientID", "VisitDate"]).reset_index(drop=True)

# df_filled = df.copy()
# filled_cols = ["Systolic_BP", "Diastolic_BP", "Cholesterol", "BloodSugar"]
# df_filled[filled_cols] = df.groupby("PatientID")[filled_cols].ffill(limit=2)

# baseline_metrics = df_filled.groupby("PatientID").agg(
#     Max_Systolic=("Systolic_BP", "max"),
#     Min_Systolic=("Systolic_BP", "min"),
#     Avg_Systolic=("Systolic_BP", "mean"),
#     Std_Systolic=("Systolic_BP", "std")
# )

# print("=== 1. HISTORICAL PATIENT BASELINES ===")
# print(baseline_metrics.to_string(), "\n")

# def calculate_bp_slope(patient_df):
#     valid_data = patient_df.dropna(subset=["VisitDate", "Systolic_BP"])
#     if len(valid_data) < 2:
#         return 0.0
#     days_elapsed = (valid_data["VisitDate"] - valid_data["VisitDate"].min()).dt.days.values
#     systolic_values = valid_data["Systolic_BP"].values
#     slope, _ = np.polyfit(days_elapsed, systolic_values, 1)
#     return slope

# slopes = df_filled.groupby("PatientID").apply(lambda x: calculate_bp_slope(x), include_groups=False)

# print("=== 2. PATIENT LONGITUDINAL TRAJECTORIES ===")
# for pid, slope in slopes.items():
#     trend = "⚠️ CRITICAL WORSENING" if slope > 0.05 else ("IMPROVING" if slope < -0.05 else "STABLE")
#     print(f"Patient: {pid} | Slope: {slope:+.4f} mmHg/day ({trend})")
# print("\n")

# unique_patients = df_filled["PatientID"].unique()
# fig, axes = plt.subplots(len(unique_patients), 1, figsize=(11, 9), sharex=True)

# for i, patient_id in enumerate(unique_patients):
#     ax = axes[i]
#     p_data = df_filled[df_filled["PatientID"] == patient_id].sort_values("VisitDate")
#     p_data_sbp = p_data.dropna(subset=["Systolic_BP"])
#     p_data_dbp = p_data.dropna(subset=["Diastolic_BP"])
    
#     ax.plot(p_data_sbp["VisitDate"], p_data_sbp["Systolic_BP"], marker='o', color='black', linewidth=2, label="Systolic BP")
#     ax.plot(p_data_dbp["VisitDate"], p_data_dbp["Diastolic_BP"], marker='s', color='dimgray', linestyle='--', label="Diastolic BP")
    
#     ax.axhspan(140, 180, color='crimson', alpha=0.12, label="Hypertension Stage 2 (>=140)")
#     ax.axhspan(120, 140, color='darkorange', alpha=0.12, label="Elevated / Stage 1 (120-140)")
#     ax.axhspan(60, 120, color='forestgreen', alpha=0.08, label="Normal Range (<120)")
    
#     p_slope = slopes[patient_id]
#     status_str = "⚠️ RISK FLAG: WORSENING" if p_slope > 0.05 else "STABLE / RESPONDING TO INTERVENTION"
    
#     ax.set_title(f"Patient: {patient_id}  |  Calculated Slope: {p_slope:+.4f} mmHg/day  |  Status: {status_str}", fontsize=10, weight='bold', pad=8)
#     ax.set_ylabel("Pressure (mmHg)", fontsize=9)
#     ax.set_ylim(55, 185)
#     ax.grid(True, linestyle=':', alpha=0.5)
    
#     ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
#     ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# plt.xlabel("Longitudinal Timeline (Timeline of Hospital Encounters)", fontsize=10, labelpad=10)
# axes[0].legend(loc="upper left", bbox_to_anchor=(1.01, 1.05), borderaxespad=0, frameon=True)
# plt.tight_layout()
# plt.show()