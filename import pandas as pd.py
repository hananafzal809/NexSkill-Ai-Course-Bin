import pandas as pd
import seaborn as sns
from sklearn. linear_model import LinearRegression
from sklearn.linear_model  import Lasso
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
import matplotlib.pyplot as plt 
from sklearn.linear_model import HuberRegressor
df = pd.read_csv("housing.csv")
print(df)
sns. scatterplot(data=df,x='population',y='households',color='pink',alpha=0.5)
plt.title('good graph')
plt.show()

x= df['housing_median_age'].values.reshape(-1,1)
y=df['median_income'].values.reshape(-1,1)
seed = 42
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=seed)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
Regression = LinearRegression()
Regression.fit(x, y)
print(Regression.intercept_)
print(Regression.coef_)

Regression.predict([[1000]])
y_pred=model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
Lasso_model = Lasso(alpha=0.5,random_state=seed)
Lasso_model.fit(x_train,y_train)

y_pred=Lasso_model.predict(x_test)
Huber_model = HuberRegressor(epsilon=1.35)
Huber_model.fit(x_train,y_train)
y_pred=Huber_model.predict(x_train)
mse=mean_squared_error(y_train,y_pred)
mae=mean_absolute_error(y_train,y_pred)
r2= r2_score(y_train,y_pred)

