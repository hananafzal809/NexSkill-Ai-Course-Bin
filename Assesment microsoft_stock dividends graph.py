import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Microsoft_stock_dividends.csv')
df['Date'] = pd.to_datetime(df['Date'])
# 3. Graph banao
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Dividends'], color='green', marker='o', linewidth=2)
plt.title('Microsoft Dividends History 2003 - 2009')
plt.xlabel('Year')
plt.ylabel('Dividend Amount ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()