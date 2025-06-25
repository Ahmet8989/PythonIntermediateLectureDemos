import numpy as np

result = np.zeros((3, 3))

result2 = np.ones((9, 9))
result3 = np.linspace(0, 20, 6) # it generates array on desired interval and desired number of elements with equal spaces

# eye -> generates identity matrix

result4 = np.eye(3)

# random

result5 = np.random.randn(4)
result6 = np.random.randn(4, 4)
result7 = np.random.randint(1, 10)
result8 = np.random.randint(1, 25, 5)

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

