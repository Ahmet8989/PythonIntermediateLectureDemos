import numpy as np

pythonListOne = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = type(pythonListOne)

result2 = np.array(pythonListOne)
result3 = type(result2)

multiDimensionalListOne = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
multiDimensionalnpArrayOne = result2.reshape(3,3)

result4 = result2.ndim
result5 = multiDimensionalnpArrayOne.ndim

result6 = result2.shape
result7 = multiDimensionalnpArrayOne.shape

print(f"Result..: {result}")
print("==========")
print(f"Result 2..: {result2}")
print("==========")
print(f"Result 3..: {result3}")
print("==========")
print(f"MultiDimensional List One..: {multiDimensionalListOne}")
print("==========")
print(f"MultiDimensional npArray One..: \n{multiDimensionalnpArrayOne}")
print("==========")
print(f"Result 4..: {result4}")
print("==========")
print(f"Result 5..: {result5}")
print("==========")
print(f"Result 6..: {result6}")
print("==========")
print(f"Result 7..: {result7}")
print("==========")
