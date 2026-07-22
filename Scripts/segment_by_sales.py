import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

#sales by segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)     
print("Segment-wise Total Sales:")
print(segment_sales)

#bar chart for segment-wise total sales
plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar", color="lightblue")
plt.title("Segment-wise Total Sales")
plt.xlabel("Segment")
plt.ylabel("Total Sales (USD)")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
print("Segment-wise total sales chart displayed successfully!")