import pandas as pd
import matplotlib.pyplot as plt 

# read cleaned data
df = pd.read_csv("Data/sales_data_cleaned.csv")

#Ship mode analysis
ship_mode_sales = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)       
print("Sales by Ship Mode:")
print(ship_mode_sales)

# Plot the results
plt.figure(figsize=(10, 6))
ship_mode_sales.plot(kind='bar')
plt.title('Sales by Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  
print("Chart saved successfully!")