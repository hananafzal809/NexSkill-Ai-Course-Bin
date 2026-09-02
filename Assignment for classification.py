import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("iris.csv")
print(df)
sns.scatterplot(data=df,x="SepalWidthCm",y="PetalLengthCm",color="yellow",alpha=0.5)
plt.title("grph")
plt.show()
y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
target_names = ['class 0', 'class 1', 'class 2']
x=df[['SepalWidthCm','PetalLengthCm']].values
y=df['Species'].values
print(classification_report(y_true, y_pred, target_names=target_names))
from sklearn.model_selection import train_test_split
seed = 42

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=seed)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x,y)

y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))
model= LogisticRegression(max_iter=200)
model= classification_report(y_test,y_pred)
print (model)

classification=LogisticRegression()
model= LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

classification=SGDClassifier
model= SGDClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_train)