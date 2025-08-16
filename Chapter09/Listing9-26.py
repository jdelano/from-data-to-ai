import pandas as pd
# Load the data
df = pd.read_csv("Chapter09/data/ticket_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# ACCURACY - Check for impossible values
print("=== ACCURACY CHECKS ===")
negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_dates = (df["date"] > current_date).sum()
oversold_shows = (df["seats_sold"] > 500).sum()  # Theater capacity is 500
print(f"Negative prices: {negative_prices}")
print(f"Future dates: {future_dates}")
print(f"Oversold shows: {oversold_shows}")

# CONSISTENCY - Check standardization
print("=== CONSISTENCY CHECKS ===")
unique_ticket_types = df["ticket_type"].unique()
unique_show_count = df["show_name"].nunique()
print("Unique ticket types:", unique_ticket_types)
print("Unique show name formats:", unique_show_count)

# VALIDITY - Business logic checks
print("=== VALIDITY CHECKS ===")
student_tickets = df["ticket_type"] == "Student"
student_prices = df[student_tickets]["price"]
adult_tickets = df["ticket_type"] == "Adult"
adult_mean_price = df[adult_tickets]["price"].mean()
expensive_student_tickets = (student_prices > adult_mean_price).sum()
print(f"Expensive student tickets: {expensive_student_tickets}")

# COMPLETENESS - Missing values
print("=== COMPLETENESS CHECKS ===")
missing_values = df.isnull().sum()
completeness_rate = df.notnull().mean().mean() * 100
print(missing_values)
print(f"Overall completeness rate: {completeness_rate:.1f}%")

# TIMELINESS - Date range verification
print("=== TIMELINESS CHECKS ===")
min_date = df["date"].min()
max_date = df["date"].max()
print(f"Date range: {min_date} to {max_date}")

# UNIQUENESS - Duplicate detection
print("=== UNIQUENESS CHECKS ===")
duplicate_ids = df["transaction_id"].duplicated().sum()
duplicate_bookings = df.duplicated(subset=["seat_number", "show_name", "date"]).sum()
print(f"Duplicate transaction IDs: {duplicate_ids}")
print(f"Duplicate bookings (same seat/show/date): {duplicate_bookings}")