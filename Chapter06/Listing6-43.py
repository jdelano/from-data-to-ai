import pandas as pd

# Sample data with numbers stored as text with symbols
financials = pd.DataFrame({
    "product": ["Widget A", "Widget B", "Widget C", "Widget D"],
    "price": ["$19.99", "$125.50", "$2,499.00", "$45.00"],
    "discount": ["10%", "15%", "20%", "5%"],
    "units": ["1,250", "850", "2,100", "3,075"]
})

# Remove symbols and convert to proper numeric types
financials["price_clean"] = pd.to_numeric(
    financials["price"].str.replace("$", "").str.replace(",", "")
)
financials["discount_clean"] = pd.to_numeric(
    financials["discount"].str.replace("%", "")
) / 100  # Convert percentages to decimal
financials["units_clean"] = pd.to_numeric(
    financials["units"].str.replace(",", "")
)

# Now we can perform calculations
financials["discount_price"] = financials["price_clean"] * (1 - financials["discount_clean"])
print("Data with discount prices:")
print(financials)