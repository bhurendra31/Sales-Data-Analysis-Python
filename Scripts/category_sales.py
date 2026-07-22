import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv") 

#Total sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)

# Plot the results
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales (USD)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.savefig("category_sales.png")

#print in png format
print("Chart saved as category_sales.png")
