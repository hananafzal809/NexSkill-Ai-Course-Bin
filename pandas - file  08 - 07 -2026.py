import pandas as pd 

data = (100,108,23,78)

series = pd.Series (data, index=["A","B","C","D"])
print(series)

data = (True, False ,True)

series = pd. Series (data)
print(series)

