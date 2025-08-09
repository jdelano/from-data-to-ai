import sqlite3
import pandas as pd

# Connect to the Northwind database (SQLite format)
conn = sqlite3.connect("Chapter03/northwind.db")

df = pd.read_sql("""
    -- Clear and semantic: counting discontinued products
    SELECT CategoryID, COUNT(*) AS DiscontinuedProducts
    FROM Products
    WHERE Discontinued = 1
    GROUP BY CategoryID;
    """, conn
)

print(df)

df = pd.read_sql("""
    -- Less clear: what does summing Discontinued mean?
    SELECT CategoryID, SUM(Discontinued) AS
        DiscontinuedProducts
    FROM Products
    GROUP BY CategoryID;
    """, conn
)

print(df)
