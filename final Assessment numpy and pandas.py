# Full-Stack AI Bootcamp - Final Assessment
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

print("=== Data Load ho raha hai ===")
df = yf.download('AAPL', start='2022-01-01', end='2024-01-01')
df = df.dropna()
print(df.head())
# 1. LOG RETURNS
returns = np.log(
   df['Close'] / df['Close'].shift(1))
returns = returns.dropna() 
print("\n=== Log Returns ===")
print(returns.head())
# 2. ANNUALIZED VOLATILITY
annual_volatility = (
    returns.std() * np.sqrt(252)
)
annual_volatility=(
    returns.std()*np.sqrt(252)
).iloc[0]
print("\n=== Annualized Volatility ===")
print(f"Annual Volatility: {annual_volatility:.4f} yaani {annual_volatility*100:.2f}%")
# 3. DRAWDOWN CALCULATIONS
cum_return = np.cumprod(1 + returns)  
running_max = np.maximum.accumulate(cum_return)  
drawdown = (
    cum_return - running_max
) / running_max
max_drawdown = drawdown.min()
print("\n=== Drawdown ===")
print(f"Max Drawdown: {max_drawdown.iloc[0]:.4f} yaani {max_drawdown.iloc[0]*100:.2f}%")
plt.figure(figsize=(10,4))
plt.plot(drawdown, label='Drawdown', color='red')
plt.title('AAPL Drawdown 2022-2024')
plt.xlabel('Date')
plt.ylabel('Drawdown %')
plt.legend()
plt.grid()
plt.savefig('drawdown_plot.png')  
plt.show()
# 4. MONTE CARLO SIMULATIONS
np.random.seed(42)  
simulations = np.random.normal(
    returns.mean(),   
    returns.std(),   
    10000             
)
print("\n=== Monte Carlo Simulation ===")
print(f"Mean of 10000 simulated returns: {simulations.mean():.6f}")
print(f"Std of 10000 simulated returns: {simulations.std():.6f}")
var_5 = np.percentile(simulations, 5)
print(f"5% VaR: {var_5:.6f} yaani {var_5*100:.2f}% loss ho sakta hai")
plt.figure(figsize=(8,4))
plt.hist(simulations, bins=50, color='blue', alpha=0.7)
plt.title('Monte Carlo Simulated Returns Distribution')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.axvline(var_5, color='red', linestyle='--', label='5% VaR')
plt.legend()
plt.savefig('monte_carlo_plot.png')
plt.show()