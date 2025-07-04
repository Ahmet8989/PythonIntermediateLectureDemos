import numpy as np
import pandas as pd

pandasSeries = pd.Series()
print(type(pandasSeries))
print(pandasSeries)

numbers = [40, 20, 30, 50, 60, 70]
letters = ['a', 'b', 'c', 'd', 'e', 'f']
singleItem = 5
mixItems = [40, 20, 30, 'd', 'e', 'f']
pandasSeries2 = pd.Series(numbers)
pandasSeries3 = pd.Series(letters)
pandasSeries4 = pd.Series(singleItem)
pandasSeries5 = pd.Series(mixItems)
indexes = [0, 1, 2, 3, 4, 5]
pandasSeries6 = pd.Series(singleItem, indexes)
pandasSeries7 = pd.Series(numbers, letters)
dictionaryOne = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e' : 50, 'f' : 60}
randomNumbersOne = np.random.randint(10, 100, 6)
pandasSeries8 = pd.Series(dictionaryOne)
pandasSeries9 = pd.Series(randomNumbersOne)

print(f"Pandas Series 2..: \n{pandasSeries2}")
print("==========")
print(f"Pandas Series 3..: \n{pandasSeries3}")
print("==========")
print(f"Pandas Series 4..: \n{pandasSeries4}")
print("==========")
print(f"Pandas Series 5..: \n{pandasSeries5}")
print("==========")
print(f"Pandas Series 6..: \n{pandasSeries6}")
print("==========")
print(f"Pandas Series 7..: \n{pandasSeries7}")
print("==========")
print(f"Pandas Series 8..: \n{pandasSeries8}")
print("==========")
print(f"Pandas Series 9..: \n{pandasSeries9}")
print("==========")


result = pandasSeries7[0]
result2 = pandasSeries7[-1]
result3 = pandasSeries7['a']
result4 = pandasSeries7[:3]
result5 = pandasSeries7[-3:]
result6 = pandasSeries7[['a', 'd', 'e']]
result7 = pandasSeries7.ndim
result8 = pandasSeries7.dtype
result9 = pandasSeries7.shape
result10 = pandasSeries7.sum()
result11 = pandasSeries7.max()
result12 = pandasSeries7.min()
result13 = pandasSeries7.argmax()
result14 = pandasSeries7.argmin()
result15 = pandasSeries7 + 50
result16 = pandasSeries7 + pandasSeries7 + pandasSeries7
result17 = np.sqrt(pandasSeries7)
result18 = pandasSeries7 > 50
result19 = pandasSeries7[result18]

print(f"Result..: {result}")
print("==========")
print(f"Result 2..: {result2}")
print("==========")
print(f"Result 3..: {result3}")
print("==========")
print(f"Result 4..: {result4}")
print("==========")
print(f"Result 5..: {result5}")
print("==========")
print(f"Result 6..: {result6}")
print("==========")
print(f"Result 7..: {result7}")
print("==========")
print(f"Result 8..: {result8}")
print("==========")
print(f"Result 9..: {result9}")
print("==========")
print(f"Result 10..: {result10}")
print("==========")
print(f"Result 11..: {result11}")
print("==========")
print(f"Result 12..: {result12}")
print("==========")
print(f"Result 13..: {result13}")
print("==========")
print(f"Result 14..: {result14}")
print("==========")
print(f"Result 15..: {result15}")
print("==========")
print(f"Result 16..: {result16}")
print("==========")
print(f"Result 17..: {result17}")
print("==========")
print(f"Result 18..: {result18}")
print("==========")
print(f"Result 19..: {result19}")
print("==========")

opel2018 = pd.Series([40, 20, 30, 50], ["astra", "corsa", "mokka", "insignie"])
opel2019 = pd.Series([70, 20, 30, 60], ["astra", "corsa", "Grandland", "insignie"])
total = opel2018 + opel2019
print(f"Total..: \n{total}")
print("==========")
print(f"Total (Astra)..: {total['astra']}")