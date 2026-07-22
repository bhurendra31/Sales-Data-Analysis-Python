#load dataset
import pandas as pd
df = pd.read_csv("Data/Sales_Data.csv")
    
#check Missing values
print("Missing Values:")
print(df.isnull().sum())    

#Fill Null values in Postal Code with 0
df["Postal Code"] = df["Postal Code"].fillna(0)
print(df.isnull().sum())

#Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)      

#Convert Ship Date to datetime
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)    

#Save cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)    

print("\n Cleaned dataset saved as 'sales_data_cleaned.csv'")

