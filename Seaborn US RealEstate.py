import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})


sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

sns. lineplot(x='x',y='y',data=data)
plt.show()


df = pd.read_csv('RealEstate-USA.csv',delimiter=",",index_col="brokered_by")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)
sns.set_theme(style='darkgrid')

g=sns.displot(data=dffilter, x="price",y="city")
g.figure.suptitle("sns.displot(data=dffiler,x=price,y=city)")
g.figure.show()
read=input("wait for me....")

g = sns.kdeplot(data=dffilter, x="price",y="zip_code")
g.figure.suptitle("sns.kdepolt(data=dffiler,x=price,y=zip_code)")
g.figure.show()
read=input("wait for me.....")










