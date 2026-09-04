import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Microsoft_stock_history.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Adj Close'], color='blue', linewidth=1.5)

plt.title('Microsoft Stock Price History - Adj Close')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()