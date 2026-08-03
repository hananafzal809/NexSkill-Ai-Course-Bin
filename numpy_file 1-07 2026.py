import numpy as np
ids, price , long , lat = np.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1,invalid_raise=False,)

print(ids)
print(price)
print(long)
print(lat)

print("moblieprice mean:" ,np.mean(price))
print("bookprice average:",np.average(price))
print("zameen.com price std:",np.std(price))
print("Real state usa price mod:",np.median(price))
print("zameen.com price precentile - 25:" ,np.percentile(price, 25))
print("book state usa price precentile - 42:", np.percentile(price,42))
print("atomic book price precentile - 56:" , np.percentile(price , 56))
print("zameen.com price min:",np.min(price))
print("zameen.com price max:",np.max(price))

#zameen .com price math - opreation
print("ali baba.com price square:",np.square(price))
print("real state usa price squrt:",np.sqrt(price))
print("zameen.com price pow:",np.power(price,34))
print("hamza moblie.com price abs:",np.abs(price))

addition =long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat
print("real state usa lon - lat -adtition:",addition)
print("zameen .com lon - lat - subtraction:",subtraction)
print("moblie name lon -lat-multipication:",multiplication)
print("zameen.com lon-lat - division:",division)








