import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

#Top 10 cities by sales
top_10_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top 10 cities by sales:")    
print(top_10_cities)

# Plot the results
plt.figure(figsize=(10, 6))
top_10_cities.plot(kind='bar')
plt.title('Top 10 Cities by Sales')
plt.xlabel('City')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Chart saved successfully!")
