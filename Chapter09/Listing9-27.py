import pandas as pd

# Load the data
df = pd.read_csv("Chapter9/data/ticket_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Check sales by ticket type
ticket_distribution = df["ticket_type"].value_counts()
print("Ticket type distribution:")
print(ticket_distribution)

# Check ticket type proportions by show
ticket_by_show = df.groupby(["show_name", "ticket_type"]).size()
show_proportions = ticket_by_show.groupby(level=0).apply(lambda x: x / x.sum())
print("=== Ticket type proportions by show ===")
print(show_proportions)

# Check missing data patterns by show
missing_by_show = df.groupby("show_name").apply(
    lambda x: x.isnull().sum().sum() / (len(x) * len(x.columns))
)
print("=== Missing data rate by show ===")
print(missing_by_show)