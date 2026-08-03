import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
df = pd.read_csv("housing.csv")
print(df)
df=pd.read_csv("iris.csv")
print(df)
sns= sns.scatterplot(data=df,x="PetalWidthCm",y="Species",color="green",alpha=0.5)
plt.title("abdul hanan")
plt.show()