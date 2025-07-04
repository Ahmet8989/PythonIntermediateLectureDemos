import numpy as np
import pandas as pd

df = pd.DataFrame()
print(df)
df = pd.DataFrame([1, 2, 3, 4])
print(df)
print()
listOne = [["Jessica", 50], ["Jane", 60], ["John", 70], ["James", 80]]
df = pd.DataFrame(listOne, [1, 2, 3, 4], ["Students", "Grades"])
print(df)
print()
print()
dictionaryOne = {"Names" : ["Jessica", "Jane", "John", "James"], "Grades" : [50, 60, 70, 80]}
df = pd.DataFrame(dictionaryOne, index=["101", "102", "103", "104"])
print(df)
print()
dictionaryList = [
    {"Name" : "Jessica", "Grade" : 50},
    {"Name" : "Jane", "Grade" : 60},
    {"Name" : "John", "Grade" : 70},
    {"Name" : "James", "Grade" : 80}
]
df = pd.DataFrame(dictionaryList, index=["101", "102", "103", "104"])
print(df)
print()


seriesOne = pd.Series([4, 2, 3, 5])
seriesTwo = pd.Series([9, 5, 6, 7])
seriesThree = pd.Series([9, 6, 7, 8])

data = dict(apples = seriesOne, oranges = seriesTwo, grapes = seriesThree)
dataFrameOne = pd.DataFrame(data)
print(dataFrameOne)
