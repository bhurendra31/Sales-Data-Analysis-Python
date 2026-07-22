import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

#region-wise total sales
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("Region-wise Total Sales:")
print(region_sales)

#bar chart for region-wise total sales
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar", color="lightgreen")
plt.title("Region-wise Total Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

