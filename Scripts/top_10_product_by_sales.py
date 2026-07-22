import pandas as pd
import matplotlib.pyplot as plt 

# read cleaned data
df = pd.read_csv("Data/sales_data_cleaned.csv")

# Top 10 products by sales
top_10_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top 10 products by sales:")
print(top_10_products)

# Plot the results
plt.figure(figsize=(10, 6))
top_10_products.plot(kind='bar')
plt.title('Top 10 Products by Sales')
plt.xlabel('Product Name')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Chart saved successfully!")  