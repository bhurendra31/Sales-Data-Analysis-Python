import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/Sales_Data_Cleaned.csv")

# Calculate Total Sales
total_sales = df["Sales"].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# Calculate Total Orders
num_orders = df.shape[0]
print(f"Total Orders: {num_orders}")

#Calculate Total Customers
num_customers = df["Customer ID"].nunique()
print(f"Total Customers: {num_customers}")

# Calculate Total Categories
total_categories = df["Category"].nunique()
print(f"Total Categories: {total_categories}")

# Calculate Total Products
total_products = df["Product Name"].nunique()
print(f"Total Products: {total_products}")

#Calculate average Sales per Order
average_sales_per_order = total_sales / num_orders
print(f"Average Sales per Order: ${average_sales_per_order:,.2f}")

#Calculate average Sales per Customer
average_sales_per_customer = total_sales / num_customers    
print(f"Average Sales per Customer: ${average_sales_per_customer:,.2f}")
