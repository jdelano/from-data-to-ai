import pandas as pd
# Load the data
df = pd.read_csv("Chapter9/data/ticket_sales.csv")
df["date"] = pd.to_datetime(df["date"]) 

# Test: No show should sell more than seats available
max_seats = 500 
seats_sold_per_show = df.groupby(["show_name", "date"])["seats_sold"].sum()
assert (seats_sold_per_show <= max_seats).all(), "Some shows sold more tickets than seats!"

# Test: Each transaction ID should be unique
assert not df["transaction_id"].duplicated().any(), "Duplicate transaction IDs found!"

# Test: All prices should be within reasonable bounds
assert (df["price"] >= 0).all(), "Negative ticket prices found!"
assert (df["price"] <= 200).all(), "Unreasonably high ticket prices found!"