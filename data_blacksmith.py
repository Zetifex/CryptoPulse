import pandas as pd
import numpy as np
# the best way to produce random numbers or states for our data match exactly
print(np.random.seed(100))
# this generates 200 days and scale as daily swing and loc average daily drift
random_walk = np.random.normal(loc=0.1, scale=50.0, size=200)
# its a cumulative sum with baseline 1500
price_series= 1500 + np.cumsum(random_walk)
# The ledger which contains the dictionary with close price
df = pd.DataFrame({'Close_Price': price_series})
# ADDING REAL MOVING AVG
df['Short_MA'] = df['Close_Price'].rolling(window=5).mean()
df['Long_MA'] = df['Close_Price'].rolling(window=20).mean()
# Clean the rows to have new dataset
df_clean = df.dropna()
# test with print only first 5
print("=== Synthetic Market Data===")
print(df.head())

import sqlite3

print("Step 5(SQL)")
# this load data base
conn=sqlite3.connect('cryptopulse.db')
# Writes data frame pandas to SQL
df_clean.to_sql('market_history', conn, if_exists='replace', index=False)
# Write sql query to find the days where the price is greater than the 1500
sql_query="""
    SELECT * FROM market_history
    WHERE Short_MA > Long_MA
    """
#The question you ask from the data base
fetched_data = pd.read_sql(sql_query, conn)
print(f"SQL Query executed. Found {len(fetched_data)} days of Golden Cross momentum.")
conn.close