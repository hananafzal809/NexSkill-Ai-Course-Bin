import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Microsoft_stock_info.csv', header=None, names=['Metric', 'Value'])

metrics_to_plot = ['profitMargins', 'grossMargins', 'operatingMargins', 'ebitdaMargins', 'revenueGrowth']
df_plot = df[df['Metric'].isin(metrics_to_plot)]

df_plot['Value'] = df_plot['Value'].astype(float)

# 4. Bar Graph banao
plt.figure(figsize=(10, 6))
plt.bar(df_plot['Metric'], df_plot['Value'], color=['blue', 'green', 'orange', 'red', 'purple'])
plt.title('Microsoft Key Financial Metrics')
plt.xlabel('Metrics')
plt.ylabel('Percentage / Ratio')
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(df_plot['Value']):
    plt.text(i, v + 0.01, f"{v:.2%}", ha='center')

plt.tight_layout()
plt.show()