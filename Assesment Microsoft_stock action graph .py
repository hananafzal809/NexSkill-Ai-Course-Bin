import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Microsoft_stock_action.csv')
df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(12, 6))
# Dividends ka graph
plt.plot(df['Date'], df['Dividends'], label='Dividends', marker='o')
plt.plot(df['Date'], df['Stock Splits'], label='Stock Splits', marker='x', color='orange')
plt.title('Microsoft Stock Action: Dividends vs Stock Splits')
plt.xlabel('Date')
plt.ylabel('Amount / Split Ratio')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()