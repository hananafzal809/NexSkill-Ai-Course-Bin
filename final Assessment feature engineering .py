import pandas as pd
import numpy as np
import yfinance as yf
ticker= ("AAPL")
df= yf.download(ticker,start="2020-01-01",end="2024-01-01")
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA100'] = df['Close'].rolling(window=100).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()
df['Volatility_5D'] = df['Close'].pct_change().rolling(window=5).std() * np.sqrt(252)
df['Volatility_10D'] = df['Close'].pct_change().rolling(window=10).std() * np.sqrt(252)
df['Volatility_20D'] = df['Close'].pct_change().rolling(window=20).std() * np.sqrt(252)
df['Volatility_60D'] = df['Close'].pct_change().rolling(window=60).std() * np.sqrt(252)
df['HL_Range'] = (df['High'] - df['Low']) / df['Close']
df['Gap'] = (df['Open'] - df['Close'].shift(1))
delta = df['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))
exp1 = df['Close'].ewm(span=12, adjust=False).mean()
exp2 = df['Close'].ewm(span=26, adjust=False).mean()
df