import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Adobe (ADBE) From 1986 To Dec-2024.csv')

df['Date'] = pd.to_datetime(df['Date'])
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 7)

plt.figure()
plt.plot(df['Date'], df['Close'], color='blue')
plt.title('Adobe ADBE Stock - Close Price 1986 to 2024')
plt.xlabel('Year')
plt.ylabel('Close Price $')
plt.show()
df_last5 = df[df['Date'] >= '2020-01-01'] 
plt.figure()
plt.plot(df_last5['Date'], df_last5['Close'], color='red')
plt.title('Adobe Stock - Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Close Price $')
plt.show()

plt.figure()
plt.plot(df['Date'], df['Volume'], color='orange')
plt.title('Adobe Stock - Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

plt.figure()
plt.fill_between(df['Date'], df['Low'], df['High'], color='gray', alpha=0.3, label='High-Low Range')
plt.plot(df['Date'], df['Close'], color='green', label='Close Price')
plt.title('Adobe Stock - Price Range')
plt.xlabel('Date')
plt.ylabel('Price $')
plt.legend()
plt.show()