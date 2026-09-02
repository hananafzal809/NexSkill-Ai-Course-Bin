import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import matplotlib.pyplot as plt

ticker = "AAPL" 
data = yf.download(ticker, start="2018-01-01", end="2026-01-01")
data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
data['Volatility'] = data['Returns'].rolling(window=20).std() * np.sqrt(252)
data = data.dropna()
