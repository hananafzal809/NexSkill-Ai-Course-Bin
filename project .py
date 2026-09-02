import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOAD
ticker = 'AAPL'
data = yf.download(ticker, start="2018-01-01", end="2026-01-01")
data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
data['Volatility'] = data['Returns'].rolling(window=20).std() * np.sqrt(252)
data['Volume_Change'] = data['Volume'].pct_change()

data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()
data['Trend'] = (data['MA50'] / data['MA200']) -1
data = data.dropna()
features = data[['Returns', 'Volume_Change', 'Volatility']].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)