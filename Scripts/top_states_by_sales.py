import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

# Top states by sales
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top 10 states by sales:")
print(top_states)

# Plot the results
plt.figure(figsize=(10, 6))
top_states.plot(kind='bar')
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Total Sales (USD)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  
print("Chart saved successfully!")