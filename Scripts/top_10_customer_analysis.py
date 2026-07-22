import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

#Top 10 customers by sales
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Sales:")
print(top_customers)

# Plot the results
plt.figure(figsize=(10, 6)) 
top_customers.plot(kind='bar')
plt.title('Top 10 Customers by Sales')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Chart saved successfully!")