import numpy as np
import pandas as pd 

myDictionary = {"Jane" : 50, "Jonathan" : 20, "James" : 30, "Julia" : 40}
result = pd.Series(myDictionary)
print(result)
print("==========")

myAges = [50, 20, 30, 40]
myNames = ["Jane", "Jonathan", "James", "Julia"]

result2 = pd.Series(myAges)
result3 = pd.Series(myAges, myNames)
result4 = pd.Series(data=myAges, index=myNames)
numpyArrayOne = np.array(myAges)
result5 = pd.Series(numpyArrayOne)

print(f"Result 2..: \n{result2}")
print("==========")
print(f"Result 3..: \n{result3}")
print("==========")
print(f"Result 4..: \n{result4}")
print("==========")
print(f"Result 5..: \n{result5}")
print("==========")