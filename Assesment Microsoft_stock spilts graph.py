import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Microsoft_stock_spilts.csv')

df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(12, 6))
plt.bar(df['Date'], df['Stock Splits'], color='orange', width=200)
plt.title('Microsoft Stock Splits History')
plt.xlabel('Date of Split')
plt.ylabel('Split Ratio')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
for i, v in enumerate(df['Stock Splits']):
    plt.text(df['Date'][i], v + 0.05, f"{v}x", ha='center')

plt.tight_layout()
plt.show()