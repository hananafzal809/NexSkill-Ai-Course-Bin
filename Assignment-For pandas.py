import pandas as pd

df = pd.read_csv("ASSIGNMENTS/RealEstate-USA.csv", delimiter=";",parse_dates=[6], date_format={'bed': '%Y-%m-%d'})
print(df)

print("df - datatypes" , df.dtypes)
print("df.info():    " , df.info())

print('last three rows:')
print(df.tail(3))

print('first three rows:')
print(df.head(3))

print("summary of statistics of dataframe using describe() method:" , df.describe())

print("continuing the rows and columns of the dataframe using shape() method:" , df.shape())
print()

city = df['city']

print("access the name column: df : ")
print(city)
print()

city_state = df[['city', 'state']]
print("access multiple columns: df : ")
print(city_state)
print()

second_row = df.loc[1]
print("#selecting a single row using .loc")
print(second_row)
print()

second_row2 = df.loc[[1,3]]
print("#selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df.loc[[1,5]]
print("#selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df.loc[df['agency'] == 'gateway properties']
print("#conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df.loc[:1,'city']
print("#selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df.loc[:,['city','state']]
print("#selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df.loc[:1,'bath':'city']
print("#selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df.loc[df['agency'] == 'gateway properties','bath':'city']
print("#combined row and column selection using .loc")
print(second_row8)
print()

print("# case 2 : using .loc with index_col - starts here")
df_index_col = pd.read_csv('Week4/zameencom-property-data-By-Kaggle-short.csv',delimiter=";",parse_dates=[6], date_format={'bed': '%d-%m-%Y'} , index_col='house_size')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row = df_index_col.loc[103378]
print("#Selecting a single row using .loc")
print(second_row)
print()

second_row2 = df_index_col.loc[[103378, 103379]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

second_row3 = df_index_col.loc[103378:109906]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

second_row4 = df_index_col.loc[df_index_col['city'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

second_row5 = df_index_col.loc[:109906,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()

second_row6 = df_index_col.loc[:109906,['city','state']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

second_row7 = df_index_col.loc[:109906,'bath':'city']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

second_row8 = df_index_col.loc[df_index_col['city'] == 'Gateway Properties','bath':'city']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

print("# Case 3 : Using .iloc - starts here")

second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

print("Next Run")

df.loc[len(df.index)] = [103378,for_sale,179000,4,3,0.46,1850806,San,Sebastian,Puerto,Rico,612,2520,]
print("Modified DataFrame - add a new row:")
print(df)
print()

df.drop(1, axis=0, inplace=True)

df.drop(index=2, inplace=True)

df.drop([3, 5], axis=0, inplace=True)

print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('street', axis=1, inplace=True)

df.drop(columns='house_size', inplace=True)

df.drop(['bath', 'city'], axis=1, inplace=True)

print("Modified DataFrame -  delete street ,house_size , bath , city , column :")
print(df)

df.rename(columns= {'acre_lot': 'acre_lotChanged'}, inplace=True)

df.rename(mapper= {'status': 'status_Changed', 'bath':'bath_Changed'}, axis=1, inplace=True)

print("Modified DataFrame  - Rename Labels :")
print(df)

df.rename(index={0: 7}, inplace=True)

df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)

print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)

selected_rows = df.query('city == \'Gateway Properties\' or price > 11000000')

print(selected_rows.to_string())
print(len(selected_rows))

sorted_df = df.sort_values(by='price')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['price', 'zip_code'])

print("Sorting by 'price' (ascending) and then by 'zip_code' (ascending):\n")
print(df1.to_string(index=False))

grouped = df.groupby('zip_code')['price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)

df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

data = [2, 4, 6, 8]

array1 = pd.array(data)
print(array1)

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()