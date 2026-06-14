import yfinance as yf
import pandas as pd
import sqlite3
# add the Asset
ticker = "BTC-USD"

print(f"Opening connection to global markets for {ticker}... ")
# 
raw_data = yf.download(ticker, period="2y", interval="1d")

df = pd.DataFrame()

df["Close_Price"] = raw_data['Close']

print("Forging the 5-day and 20-day Moving Averages ...")
df['Short_MA'] = df['Close_Price'].rolling(window=5).mean()
df['Long_MA'] = df['Close_Price'].rolling(window=20).mean()

df_clean = df.dropna()

print("Locking data into SQLite Vault ....")

conn = sqlite3.connect("cryptopulse.db")

df_clean.to_sql('market_history', conn, if_exists='replace', index= True)
conn.close()

print(f"Success! {len(df_clean)} days of real {ticker} history safely stored.")