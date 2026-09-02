import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
np.random.seed(42)
n = 500

data = {
    'Interest_Rate': np.random.uniform(2, 8, n),
    'Inflation': np.random.uniform(1, 6, n),
    'GDP_Growth': np.random.uniform(0, 5, n),
    'Oil_Price': np.random.uniform(50, 120, n),
    'Exchange_Rate': np.random.uniform(250, 300, n),  
    'Consumer_Confidence': np.random.uniform(40, 100, n),
    'Unemployment': np.random.uniform(3, 10, n)
}
df = pd.DataFrame(data)
df['Stock_Return'] = (
    -1.5 * df['Interest_Rate'] + 
    -0.8 * df['Inflation'] + 
    2.2 * df['GDP_Growth'] + 
    -0.3 * df['Oil_Price'] + 
    0.5 * df['Consumer_Confidence'] + 
    np.random.normal(0, 2, n)  # noise
)
print("Dataset Preview:")
print(df.head())
X = df.drop('Stock_Return', axis=1)
y = df['Stock_Return']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"\nModel R2 Score: {r2_score(y_test, y_pred):.3f}")
importances = model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)
print("\nFeature Importance Ranking:")
print(feature_importance_df)
plt.figure(figsize=(10,6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis')
plt.title('Market Factors - Feature Importance Ranking', fontsize=14)
plt.xlabel('Importance Score')
plt.ylabel('Market Factors')
plt.tight_layout()
plt.show()