import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'Return': np.random.normal(0, 0.02, 500),
    'Volume': np.random.randint(1000, 10000, 500),
    'Volatility': np.random.uniform(0.01, 0.1, 500),
    'RSI': np.random.uniform(30, 70, 500),
    'Regime': np.random.choice(['Bull', 'Bear', 'High Vol'], 500)
})
sns.set_style("whitegrid") 
plt.figure(figsize=(8,5))
sns.histplot(
    df['Return'],
    kde=True
)
plt.title("Return Distribution")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(8,6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()
sns.pairplot(
    df[
        ['Return',
         'Volume',
         'Volatility',
         'RSI']
    ]
)
plt.suptitle("Pairplot for Non-linear behavior & Clusters", y=1.02)
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Regime',
    y='Return',
    data=df
)
plt.title("Return by Market Regime")
plt.xlabel("Regime")
plt.ylabel("Return")
plt.show()