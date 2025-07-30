import pandas as pd
# 1. Load data with clear source identification
df_sales = pd.read_csv("quarterly_sales.csv")
df_customers = pd.read_excel("customer_master.xlsx")

# 2. Preprocess each dataset
# Standardize column names
df_sales = df_sales.rename(columns={"Cust_ID": "CustomerID"})
df_customers = df_customers.rename(columns={"ID": "CustomerID"})

# Ensure consistent data types
df_sales["CustomerID"] = df_sales["CustomerID"].astype(str)
df_customers["CustomerID"] = df_customers["CustomerID"].astype(str)

# Filter to relevant time period
df_sales = df_sales[df_sales["Year"] >= 2023]

# 3. Harmonize categorical values
region_mapping = {"NE": "Northeast", "SE": "Southeast", "MW": "Midwest"}
df_sales["Region"] = df_sales["Region"].replace(region_mapping)

# 4. Execute merge with verification
df_integrated = pd.merge(df_sales, df_customers, 
                        on="CustomerID", 
                        how="left",
                        indicator=True)

# Check merge quality
print("Merge results:")
print(df_integrated["_merge"].value_counts())

# 5. Clean up post-merge
df_integrated = df_integrated.drop("_merge", axis=1)

# Resolve any conflicts (example: if both had Region columns)
df_integrated["Region"] = df_integrated["Region_sales"]  
df_integrated = df_integrated.drop(["Region_sales", "Region_customers"], axis=1)

# 6. Quality verification
print(f"Original sales records: ")
print(df_sales.info())
print(f"Integrated records:")
print(df_integrated.info())

# Spot check a known customer
sample_customer = df_integrated[df_integrated["CustomerID"] == "12345"]
print(f"Sample customer data: {sample_customer}")

# 7. Save the integrated dataset
df_integrated.to_csv("integrated_sales_customers.csv", index=False)
print("Integration complete!")