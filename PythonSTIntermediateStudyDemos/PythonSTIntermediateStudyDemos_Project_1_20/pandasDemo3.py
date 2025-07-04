import pandas as pd
import numpy as np

dataOne = np.random.randn(3, 3)
indexListOne = ["A", "B", "C"]
columnListOne = ["Column 1", "Column 2", "Column 3"]
df = pd.DataFrame(dataOne, columns = columnListOne, index = indexListOne)
print(df)

result = df["Column 1"]
result2 = type(df["Column 1"])
result3 = df[["Column 1", "Column 3"]]
# loc["row", "column"]
result4 = df.loc["A"]
result5 = type(df.loc["A"])
result6 = df.loc[:, ["Column 1"]]
result7 = df.loc[:, ["Column 1", "Column 3"]]
result8 = df.loc["A":"C", "Column 1" : "Column 3"]
result9 = df.iloc[1]

print()
print(f"Result..: \n{result}")
print()
print()
print(f"Result 2..: \n{result2}")
print()
print()
print(f"Result 3..: \n{result3}")
print()
print()
print(f"Result 4..: \n{result4}")
print()
print()
print(f"Result 5..: \n{result5}")
print()
print()
print(f"Result 6..: \n{result6}")
print()
print()
print(f"Result 7..: \n{result7}")
print()
print()
print(f"Result 8..: \n{result8}")
print()
print()
print(f"Result 9..: \n{result9}")
print()

result10 = df.loc["A", "Column 3"]
df["Column 4"] =  pd.Series(np.random.randn(3), ["A", "B", "C"])
print(result10)
print()
print(df)
print()
df["Column 5"] = df["Column 2"] + df["Column 3"]
print(df)
print()
result11 = df.drop("Column 5", axis = 1)
print(result11)
print()