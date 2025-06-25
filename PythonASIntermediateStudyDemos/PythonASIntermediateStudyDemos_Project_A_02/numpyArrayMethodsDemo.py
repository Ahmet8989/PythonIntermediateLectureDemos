import numpy as np

# numpy array methods

myNumpyArray = np.arange(60)
myRandomArray = np.random.randint(0, 100, 20)

result = myNumpyArray.reshape(6, 10)
result2 = myNumpyArray.max()
result3 = myRandomArray.max()
result4 = myNumpyArray.min()
result5 = myRandomArray.min()
result6 = myNumpyArray.argmin() # shows the index of min element
result7 = myNumpyArray.argmax() # shows the index of max element
result8 = myNumpyArray.shape

print(result)
print("==========")
print(result2)
print("==========")
print(result3)
print("==========")
print(result4)
print("==========")
print(result5)
print("==========")
print(result6)
print("==========")
print(result7)
print("==========")
print(result8)
print("==========")
