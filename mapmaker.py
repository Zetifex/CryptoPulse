import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt

print("Mile Stone 3: Mapmaker")

#fetch the data from the Vault to use it
conn = sqlite3.connect('cryptopulse.db')
#command the sql to extract the specific data from the sql
sql_query = "SELECT * FROM market_history"
#pandas to read the data
df = pd.read_sql(sql_query,conn)
conn.close

#Now use to plot the data
plt.figure(figsize=(12,6))

# Draw lines a;pha shows the transparency
plt.plot(df['Close_Price'], label = 'Raw Daily Price', color = 'gray', alpha=0.5)
plt.plot(df['Short_MA'], label = '5-Day Momentum (Fast)', color = 'blue', linewidth = 2)
plt.plot(df['Long_MA'], label = '10-Day Momentum (Slow)', color = 'red', linewidth = 2)
# ADD label and Legends
plt.title("CryptoPulse: Asset Trend & Moving Averages")
plt.xlabel("Days(Time)")
plt.ylabel("Price(USD)")
plt.legend()
plt.grid(True)
# To save figures
plt.savefig("market_map.png")
print("Map successfully drawn and saved as 'market_map.png")