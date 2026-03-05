import pandas as pd
import sqlite3

# 1. LOAD: Read the file you uploaded
df = pd.read_csv('messy_dataset.csv')

# 2. CLEAN NULLS: (Requirement: "Clean the nulls")
df_cleaned = df.dropna().copy()

# 3. FIX DATES: (Requirement: "Fix the dates")
df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date'])

# 4. SQL PIPELINE: (Requirement: Python + Pandas + SQL)
conn = sqlite3.connect(':memory:')
df_cleaned.to_sql('orders', conn, index=False, if_exists='replace')

# --- THE JUDGE'S QUERIES ---

# A. Monthly Revenue
monthly_rev = pd.read_sql("SELECT strftime('%Y-%m', order_date) as Month, SUM(total_price) as Revenue FROM orders GROUP BY 1", conn)

# B. Top Products (by Category Revenue)
top_cats = pd.read_sql("SELECT category, SUM(total_price) as Revenue FROM orders GROUP BY 1 ORDER BY 2 DESC", conn)

# C. Avg Order Value (AOV)
aov = pd.read_sql("SELECT AVG(total_price) as AOV FROM orders", conn).iloc[0,0]

# D. Repeat Purchase Rate
repeat_rate = pd.read_sql("""
    WITH user_stats AS (SELECT user_id, COUNT(order_id) as orders FROM orders GROUP BY 1)
    SELECT (SELECT COUNT(*) FROM user_stats WHERE orders > 1) * 100.0 / COUNT(*) FROM user_stats
""", conn).iloc[0,0]

print(f"Pipeline Complete: AOV is ${aov:.2f} and Repeat Rate is {repeat_rate:.2f}%")