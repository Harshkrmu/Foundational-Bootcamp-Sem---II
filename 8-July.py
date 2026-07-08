# # =====================================================
# # Q1. Global Climate Change & Thermal Anomaly Tracking
# # =====================================================

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = pd.read_csv("GlobalWeatherRepository.csv")

# df["last_updated"] = pd.to_datetime(df["last_updated"])

# df["Quality_Flag"] = np.where(df["temperature_celsius"].isna(), "Bad", "Good")

# df = df.set_index(["country", "location_name", "last_updated"])

# df = df.reset_index()

# rolling = df["temperature_celsius"].rolling(24, min_periods=1).median()

# df["temperature_celsius"] = np.where(df["temperature_celsius"].isna(), rolling, df["temperature_celsius"])

# df["Year"] = df["last_updated"].dt.year

# df["Latitude_Band"] = pd.cut(df["latitude"], bins=[-90, -60, -30, 0, 30, 60, 90], labels=["S90-S60", "S60-S30", "S30-0", "0-30", "30-60", "60-90"])

# annual_temp = df.groupby("Year")["temperature_celsius"].mean()
# anomaly = annual_temp - df["temperature_celsius"].mean()

# heatmap = df.pivot_table(values="temperature_celsius", index="Latitude_Band", columns="Year", aggfunc=np.std)

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
# ax1.plot(annual_temp.index, anomaly, marker="o", color="red")
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Temperature Anomaly", color="red")
# ax3 = ax1.twinx()
# ax3.bar(annual_temp.index, annual_temp.values, alpha=0.4)
# ax3.set_ylabel("Average Temperature")
# ax1.set_title("Global Annual Temperature Anomaly")

# img = ax2.imshow(heatmap, cmap="coolwarm", aspect="auto")
# ax2.set_xticks(range(len(heatmap.columns)))
# ax2.set_xticklabels(heatmap.columns)
# ax2.set_yticks(range(len(heatmap.index)))
# ax2.set_yticklabels(heatmap.index)
# ax2.set_title("Temperature Standard Deviation by Latitude Band")

# plt.colorbar(img, ax=ax2)
# plt.tight_layout()
# plt.show()

# # ========================================================
# #  Q2. High-Frequency Financial Order Book Reconstitution
# # ========================================================

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df = pd.read_csv("orders.csv")

# df["Timestamp"] = pd.to_datetime(df["Timestamp"])
# df = df.sort_values("Timestamp")

# # -------------------------------
# # Step 2: Calculate VWAP
# # -------------------------------

# df["PV"] = df["Price"] * df["Volume"]
# df = df.set_index("Timestamp")
# result = []

# for ticker, group in df.groupby("Ticker"):
#     data = group.resample("5min")
#     summary = data.agg({
#         "Price": ["first", "max", "min", "last"],
#         "Volume": "sum",
#         "PV": "sum"
#     })

#     summary.columns = ["Open", "High", "Low", "Close", "Volume", "PV"]

#     summary["VWAP"] = summary["PV"] / summary["Volume"]

#     result.append((ticker, summary))

# # -------------------------------
# # Step 3: Bid-Ask Spread
# # -------------------------------

# print("\nBid-Ask Spread")

# for ticker, summary in result:

#     group = df[df["Ticker"] == ticker]

#     buy_price = group[group["Action"] == "Buy"]["Price"].mean()
#     sell_price = group[group["Action"] == "Sell"]["Price"].mean()

#     spread = sell_price - buy_price

#     print(f"{ticker} Spread = {spread:.2f}")

# # -------------------------------
# # Step 4: Market Depth using NumPy
# # -------------------------------

# print("\nMarket Depth")

# for ticker in df["Ticker"].unique():

#     group = df[df["Ticker"] == ticker]

#     prices = np.sort(group["Price"].unique())

#     levels = prices[:10]

#     print(f"\nTicker : {ticker}")

#     for price in levels:

#         depth = group[group["Price"] == price]["Volume"].sum()

#         print("Price:", price, "Volume:", depth)

# # -------------------------------
# # Step 5: Candlestick + VWAP + Volume
# # -------------------------------

# for ticker, summary in result:

#     fig, ax1 = plt.subplots(figsize=(12,6))

#     x = np.arange(len(summary))

#     # High-Low line
#     ax1.vlines(x, summary["Low"], summary["High"], color="black")

#     # Open-Close bars
#     colors = []

#     for i in range(len(summary)):
#         if summary["Close"].iloc[i] >= summary["Open"].iloc[i]:
#             colors.append("green")
#         else:
#             colors.append("red")

#     ax1.bar(
#         x,
#         summary["Close"] - summary["Open"],
#         bottom=summary["Open"],
#         color=colors,
#         width=0.5
#     )

#     # VWAP Line
#     ax1.plot(x, summary["VWAP"], color="blue", linewidth=2, label="VWAP")

#     ax1.set_title(f"{ticker} OHLC with VWAP")
#     ax1.set_ylabel("Price")

#     # Volume bars
#     ax2 = ax1.twinx()

#     ax2.bar(
#         x,
#         summary["Volume"],
#         color="gray",
#         alpha=0.3,
#         width=0.5,
#         label="Volume"
#     )

#     ax2.set_ylabel("Volume")

#     plt.xticks(x, summary.index.strftime("%H:%M"), rotation=45)

#     plt.tight_layout()
#     plt.show()