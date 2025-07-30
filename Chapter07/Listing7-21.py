import pandas as pd

# Starting data - note the one luxury house with extreme price
houses = pd.DataFrame({
    "nbhood": ["Downtown", "Suburbs", "Downtown", "Rural", "Downtown"],
    "price": [500000, 350000, 450000, 200000, 2500000],  # One extreme
    "sqft": [1200, 2000, 1100, 1800, 3500],
    "list_date": pd.to_datetime(["2024-01-15", "2024-02-20", 
                                  "2024-01-08", "2024-03-01", "2024-02-10"])
})

# Create dummy variables for neighborhood
houses_enc = pd.get_dummies(houses, columns=["nbhood"])

# Add binning for square footage with descriptive labels
houses_enc["size_category"] = pd.cut(houses_enc["sqft"], 
                                     bins=[0, 1500, 2500, 5000],
                                     labels=["Small", "Medium", "Large"])

# Handle the skewed price with reciprocal transform
houses_enc["price_reciprocal"] = 1 / houses_enc["price"]

# Engineer features from raw data
houses_enc["price_per_sqft"] = houses_enc["price"] / houses_enc["sqft"]
houses_enc["list_month"] = houses_enc["list_date"].dt.month
new_year = pd.Timestamp("2024-01-01")
houses_enc["days_listed"] = (houses_enc["list_date"] - new_year).dt.days

# Scale the numeric features
houses_enc["price_scaled"] = houses_enc["price"] / 100000  
houses_enc["sqft_scaled"] = houses_enc["sqft"] / 1000      

# Display key transformed columns
print(houses_enc[["price_scaled", "price_reciprocal", "size_category",
                  "price_per_sqft", "nbhood_Downtown", "nbhood_Rural"]])