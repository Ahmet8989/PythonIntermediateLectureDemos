import numpy as np
import pandas as pd

data = np.random.randint(10, 100, 75).reshape(15, 5)

df = pd.DataFrame(data, columns = ["Column1", "Column 2", "Column 3", "Column 4", "Column 5"])
print(df)

result = df.columns
print(result)

for column in df.columns:
    print(f"{column}\n")

result2 = df.head()
result3 = df.head(10)
result4 = df.tail()
result5 = df.tail(10)
result6 = df["Column 3"].head()
result7 = df[["Column1", "Column 3"]].head()
result8 = df[5:15][["Column1", "Column 3"]].head()
result9 = df[5:15][["Column1", "Column 3"]].tail()
result10 = df > 50
result11 = df[result10]
result12 = df["Column1"] > 50
result13 = df[result12]
result14 = df[result12][["Column1", "Column 3"]]
result15 = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
result16 = df[(df["Column1"] > 50) | (df["Column 3"] > 50)]
result17 = df.query("Column1 > 50 & Column1 % 2 == 0")
print(result17)