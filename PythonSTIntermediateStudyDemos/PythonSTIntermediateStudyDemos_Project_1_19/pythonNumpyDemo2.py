import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])
result = numbers[5]
result2 = numbers[-1]
result3 = numbers[0:3]
result4 = numbers[3:]
result5 = numbers[::]
result6 = numbers[::-1]
numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])
result7 = numbers2[2]
result8 = numbers2[0,2]
result9 = numbers2[2][2]
result10 = numbers2[:,2]
result11 = numbers2[:,0:2]

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
print(f"Result 11..: \n{result11}")
print("==========")

arrayOne = np.arange(1, 10)
result12 = arrayOne # Reference Copy
result13 = arrayOne.copy() # Value Copy
print(f"Result 12..: {result12}")
print("==========")
print(f"Result 13..: {result13}")
print("==========")
arrayOne[5] = 35
print(f"Result 12..: {result12}")
print("==========")
print(f"Result 13..: {result13}")
print("==========")
