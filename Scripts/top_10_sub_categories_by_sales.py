import pandas as pd
import matplotlib.pyplot as plt     

df = pd.read_csv("Data/Sales_Data_Cleaned.csv") 

#Top 10 sub-categories by sales
top_sub_categories = df.groupby("Sub-Category")["Sales"].sum().sort_values( ascending=False).head(10)
print("\nTop 10 Sub-Categories by Sales:")
print(top_sub_categories)

# Plot the results
plt.figure(figsize=(10, 6))
top_sub_categories.plot(kind='bar')
plt.title('Top 10 Sub-Categories by Sales')
plt.xlabel('Sub-Category')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Chart saved successfully!")
