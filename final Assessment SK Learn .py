import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.metrics import classification_report, accuracy_score
def create_features(ticker):
    df = yf.download(ticker, start="2020-01-01", end="2024-01-01")
    df['MA20'] = df['Close'].rolling(20).mean()
    df['MA50'] = df['Close'].rolling(50).mean()
    df['Volatility_20D'] = df['Close'].pct_change().rolling(20).std() * np.sqrt(252)
    df['Return'] = df['Close'].pct_change()
    df['Tomorrow_Up'] = np.where(df['Return'].shift(-1) > 0, 1, 0)
    df['Tomorrow_Return'] = df['Return'].shift(-1)
    df['Future_5D_Return'] = df['Close'].pct_change(5).shift(-5)
    df['Future_20D_Return'] = df['Close'].pct_change(20).shift(-20)
    df.dropna(inplace=True)
    return df
tickers = ['ADBE', 'MSFT', 'ORCL', 'CRM']
for ticker in tickers:
    print(f"\n================= {ticker} ==================")
    df = create_features(ticker)
    features = ['MA20', 'MA50', 'Volatility_20D', 'Return']
    X = df[features]
    y_class = df['Tomorrow_Up']
    tscv = TimeSeriesSplit(n_splits=5) 
    models = {
        'LogisticRegression': LogisticRegression(),
        'RandomForest': RandomForestClassifier(),
        'GradientBoosting': GradientBoostingClassifier(),
        'ExtraTrees': ExtraTreesClassifier()
    }
    for name, model in models.items():
        pipe = Pipeline([
            ('scaler', StandardScaler()),
            ('model', model)
        ])
        scores = []
        for train_index, test_index in tscv.split(X):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y_class.iloc[train_index], y_class.iloc[test_index]
            pipe.fit(X_train, y_train)
            y_pred = pipe.predict(X_test)
            scores.append(accuracy_score(y_test, y_pred))
        print(f"{name} Accuracy: {np.mean(scores):.4f}")
        if name in ['RandomForest', 'GradientBoosting', 'ExtraTrees']:
            pipe.fit(X, y_class)
            importances = pipe.named_steps['model'].feature_importances_
            print(f"{name} Feature Importance: {dict(zip(features, importances.round(3)))}")