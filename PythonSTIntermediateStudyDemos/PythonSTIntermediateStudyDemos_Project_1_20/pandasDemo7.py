import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index = ['a', 'b', 'e', 'f', 'h'], columns = ['Column1', 'Column2', 'Column3'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)

# If there are Nan values exist, we can use drop method

result = df.drop('Column1', axis = 1)
result2 = df.drop('h', axis = 0)
result3 = df.drop(['c', 'd', 'g'], axis = 0)

# We can detect Nans with isnull()

result4 = df.isnull()
result5 = df.isnull().sum()
result6 = df['Column3'].isnull().sum()
result7 = df.notnull()

newColumn = [np.nan, 55, np.nan, 45, 75, 85, 65, np.nan]
df['Column4'] = newColumn

result8 = df[df['Column1'].isnull()]['Column1']
result9 = df[df['Column1'].notnull()]['Column1']
result10 = df.dropna() # Default -> deletes rows with Nans
result11 = df.dropna(axis = 1) # Deletes columns with Nans

result12 = df.dropna(how='any') # Deletes row even single Nan exists
result13 = df.dropna(how='all') # Deletes eow all item in the row is Nan
result14 = df.dropna(subset = ['Column1', "Column4"]) # Deletes row if Column1 or Column4 has Nan

result15 = df.dropna(thresh = 2)
result16 = df.dropna(thresh = 4)
result17 = df.fillna(value = 'No input')
result18 = df.fillna(value = 1)

def findAverage(df):
    dfValueSum = df.sum().sum()
    dfItemAmount = df.size
    dfNanItemAmount = df.isnull().sum().sum()
    return (dfValueSum / (dfItemAmount - dfNanItemAmount))

result19 = df.fillna(value = findAverage(df))
print(result19)