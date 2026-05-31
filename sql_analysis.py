import pandas as pd
import sqlite3

# Load Excel file
df = pd.read_excel("Dataset for Data Analytics (3).xlsx")

# Create SQLite database in memory
conn = sqlite3.connect(":memory:")

# Store data as SQL table
df.to_sql("orders", conn, index=False, if_exists="replace")

# 1. SELECT query
print("\n===== SELECT QUERY =====")
query1 = """
SELECT OrderID, Product, TotalPrice
FROM orders
LIMIT 10;
"""
print(pd.read_sql(query1, conn))

# 2. WHERE query
print("\n===== WHERE QUERY =====")
query2 = """
SELECT *
FROM orders
WHERE TotalPrice > 2000;
"""
print(pd.read_sql(query2, conn).head())

# 3. ORDER BY query
print("\n===== ORDER BY QUERY =====")
query3 = """
SELECT Product, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;
"""
print(pd.read_sql(query3, conn))

# 4. GROUP BY + COUNT
print("\n===== GROUP BY COUNT =====")
query4 = """
SELECT Product,
COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
ORDER BY TotalOrders DESC;
"""
print(pd.read_sql(query4, conn))

# 5. GROUP BY + SUM
print("\n===== GROUP BY SUM =====")
query5 = """
SELECT Product,
SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;
"""
print(pd.read_sql(query5, conn))

# 6. GROUP BY + AVG
print("\n===== GROUP BY AVG =====")
query6 = """
SELECT Product,
AVG(TotalPrice) AS AvgRevenue
FROM orders
GROUP BY Product
ORDER BY AvgRevenue DESC;
"""
print(pd.read_sql(query6, conn))

conn.close()

print("\nPROJECT 3 COMPLETED SUCCESSFULLY")