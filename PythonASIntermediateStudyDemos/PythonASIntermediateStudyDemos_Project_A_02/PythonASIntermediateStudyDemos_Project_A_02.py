import numpy as np

# numpy array

listOne = [40, 50, 60]

result = np.array(listOne)

listTwo = [[50, 20, 30], [40, 50, 60], [60, 70, 80]]

result2 = np.array(listTwo)

# arange

result3 = np.arange(0, 10)

result4 = np.arange(0, 15, 3)

# zeros 
result5 = np.zeros(6)

print(result)
print("==========")
print(result2)
print("==========")
print(result3)
print("==========")
print(result4)
print("==========")
print(result5)