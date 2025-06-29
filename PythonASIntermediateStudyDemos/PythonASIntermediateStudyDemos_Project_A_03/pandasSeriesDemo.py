import numpy as np
import pandas as pd

result = pd.Series(["Jane", "Jonathan", "Jessica"], [1, 2, 3])

competationResultOne = pd.Series([10, 5, 1], ["Jane", "Jonathan", "Jessica"])
competationResultTwo = pd.Series([20, 10, 8], ["Jane", "Jonathan", "Jessica"])
result2 = competationResultTwo["Jane"]
result3 = competationResultOne + competationResultTwo
diffrentSeries = pd.Series([40, 20, 30, 50], ['a', 'b', 'd', 'e'])
diffrentSeries2 = pd.Series([40, 20, 30, 70], ['f', 'b', 'd', 'g'])


print(f"Result..: \n{result}")
print("==========")
