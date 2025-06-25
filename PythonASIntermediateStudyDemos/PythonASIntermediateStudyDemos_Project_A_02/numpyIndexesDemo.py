import numpy as np

myNumpyArray = np.arange(0, 15)

result = myNumpyArray[5]
result2 = myNumpyArray[5:9]
myNumpyArray[5:9] = -7
result3 = myNumpyArray
print(result)
print("==========")
print(result2)
print("==========")
print(result3)
print("==========")
anotherNumpyArray = np.arange(0, 24)
exampleNumpyArray = np.arange(0, 24)
result4 = anotherNumpyArray[4:9]
result5 = exampleNumpyArray.copy()[4:9]
print(result4)
print("==========")
print(result5)
print("==========")
result4[:] = 700
result5[:] = 700
print(result4)
print("==========")
print(anotherNumpyArray)
print("==========")
print(result5)
print("==========")
print(exampleNumpyArray)
print("==========")

# matrix

myListOne = [[50, 20, 30], [40, 50, 60], [50, 60, 70]]
myMatrixArray = np.array(myListOne)
print(myMatrixArray)
result6 = myMatrixArray[0]
result7 = myMatrixArray[0][0]
result8 = myMatrixArray[0, 0]
result9 = myMatrixArray[0:, 2]
result10 = myMatrixArray[2:, 2:]

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

newList = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
newArray = np.array(newList)
print(newArray)
print("==========")
result11 = newArray[[0, 2, 3]]
print(f"Result 11..: {result11}")

# numpy operations

newArray2 = np.random.randint(1, 100, 20)
print(f"New array 2..: {newArray2}")
print("==========")
result12 = (newArray2 > 24)
print(f"Result 12..: {result12}")
print("==========")
result13 = newArray2[result12]
print(f"Result 13..: {result13}")
print("==========")
newArray3 = np.arange(0, 23)
result14 = (newArray3 + newArray3)
print(f"Result 14..: {result14}")
print("==========")
result15 = (newArray3 * newArray3)
print(f"Result 15..: {result15}")
print("==========")
result16 = np.sqrt(result15)
print(f"Result 16..: {result16}")
print("==========")
result17 = np.max(result15)
print(f"Result 17..: {result17}")
print("==========")
result18 = np.min(result15)
print(f"Result 18..: {result18}")
print("==========")
