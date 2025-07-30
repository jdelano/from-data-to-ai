#https://raw.githubusercontent.com/jpwhite3/northwind-SQLite3/main/dist/northwind.db
import sqlite3
import pandas as pd
connection = sqlite3.connect("northwind.db")  # Connect to the SQLite database

query = (
    "SELECT * "
    "FROM Customers"
) 

df = pd.read_sql(query, connection)  # Execute the query and load the result into a DataFrame
print(df.head())  # Display the first few rows of the DataFrame
connection.close()  # Close the database connection


