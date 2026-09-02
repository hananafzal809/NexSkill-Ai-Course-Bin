import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import matplotlib.pyplot as plt

# 1. DATA LOAD
ticker = "SPY" 
data = yf.download(ticker, start="2018-01-01", end="2026-01-01")
data['Future_Return'] = data['Close'].shift(-1) / data['Close'] - 1
data['Target'] = np.where(data['Future_Return'] > 0, 1, 0)
# 3. FEATURES
data['Return'] = data['Close'].pct_change()
data['MA5'] = data['Close'].rolling(5).mean()
data['MA20'] = data['Close'].rolling(20).mean()
data['Volatility'] = data['Return'].rolling(20).std()
data['RSI'] = 100 - (100 / (1 + (data['Return'].rolling(14).apply(lambda x: x[x>0].sum()) / abs(data['Return'].rolling(14).apply(lambda x: x[x<0].sum())))))
data = data.dropna()
features = ['Return', 'MA5', 'MA20', 'Volatility', 'RSI']
X = data[features]
y = data['Target']
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]
scaler_rf = StandardScaler()
X_train_rf = scaler_rf.fit_transform(X_train)
X_test_rf = scaler_rf.transform(X_test)
rf = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42)
rf.fit(X_train_rf, y_train)
rf_pred = rf.predict(X_test_rf)
rf_acc = accuracy_score(y_test, rf_pred)
gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=4, random_state=42)
gb.fit(X_train_rf, y_train)
gb_pred = gb.predict(X_test_rf)
gb_acc = accuracy_score(y_test, gb_pred)
scaler_lstm = MinMaxScaler()
X_train_lstm = scaler_lstm.fit_transform(X_train)
X_test_lstm = scaler_lstm.transform(X_test)
def create_sequences(X, y, seq_len=20):
    Xs, ys = [], []
    for i in range(len(X) - seq_len):
        Xs.append(X[i:i+seq_len])
        ys.append(y.iloc[i+seq_len])
    return np.array(Xs), np.array(ys)
seq_len = 20
X_train_seq, y_train_seq = create_sequences(X_train_lstm, y_train, seq_len)
X_test_seq, y_test_seq = create_sequences(X_test_lstm, y_test, seq_len)
lstm = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train_seq.shape[1], X_train_seq.shape[2])),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])
lstm.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
lstm.fit(X_train_seq, y_train_seq, epochs=20, batch_size=32, verbose=1, validation_split=0.1)
lstm_pred_prob = lstm.predict(X_test_seq)
lstm_pred = (lstm_pred_prob > 0.5).astype(int).flatten()
lstm_acc = accuracy_score(y_test_seq, lstm_pred)
# 7. BACKTEST: Sharpe Ratio + Max Drawdown
def backtest_strategy(signals, returns):
    # signals: 1=Buy/Hold, 0=Cash
    strategy_returns = signals * returns
    cumulative = (1 + strategy_returns).cumprod()
    sharpe = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std()
    roll_max = cumulative.cummax()
    drawdown = cumulative/roll_max - 1.0
    max_dd = drawdown.min()
    return sharpe, max_dd, cumulative
test_returns = data['Return'].iloc[split:]
rf_signals = pd.Series(rf_pred, index=test_returns.index)
gb_signals = pd.Series(gb_pred, index=test_returns.index)
lstm_signals = pd.Series(lstm_pred, index=test_returns.index[seq_len:])
lstm_returns_aligned = test_returns.iloc[seq_len:]
rf_sharpe, rf_dd, rf_cum = backtest_strategy(rf_signals, test_returns)
gb_sharpe, gb_dd, gb_cum = backtest_strategy(gb_signals, test_returns)
lstm_sharpe, lstm_dd, lstm_cum = backtest_strategy(lstm_signals, lstm_returns_aligned)
results = pd.DataFrame({
    'Model': ['Random Forest', 'Gradient Boosting', 'LSTM'],
    'Accuracy': [rf_acc, gb_acc, lstm_acc],
    'Sharpe Ratio': [rf_sharpe, gb_sharpe, lstm_sharpe],
    'Max Drawdown': [rf_dd, gb_dd, lstm_dd]
})
print("\n=== Final Comparison ===")
print(results.round(4))
plt.figure(figsize=(12,6))
plt.plot(rf_cum.index, rf_cum.values, label='Random Forest')
plt.plot(gb_cum.index, gb_cum.values, label='Gradient Boosting')
plt.plot(lstm_cum.index, lstm_cum.values, label='LSTM')
plt.plot(test_returns.index, (1+test_returns).cumprod(), label='Buy & Hold', linestyle='--', color='black')
plt.title(f'{ticker} Strategy Cumulative Returns')
plt.ylabel('Growth of $1')
plt.legend()
plt.show()