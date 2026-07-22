import os
import pandas as pd
import matplotlib.pyplot as plt

# use actual filename in the workspace
df = pd.read_csv("Data/sales_data_cleaned.csv")

# Total sales month-wise
# parse using the known YYYY-MM-DD format; coerce invalid parses
df["order date"] = pd.to_datetime(df["Order Date"], format="%Y-%m-%d", errors="coerce")
df["Month"] = df["order date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()
print(monthly_sales)

#line chart for month-wise total sales
plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o", color="blue")
plt.title("Month-wise Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()

# ensure the output directory exists (workspace has Sales_Chart)
os.makedirs("Sales_Chart", exist_ok=True)
plt.savefig("Sales_Chart/monthly_sales_line.png")
print("Chart saved successfully!")
plt.show()
