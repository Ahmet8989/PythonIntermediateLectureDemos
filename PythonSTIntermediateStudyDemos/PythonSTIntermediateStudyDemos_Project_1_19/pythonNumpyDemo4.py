import numpy as np

result = np.array([10, 15, 30, 45, 60])
print(type(result))
print(result)

result2 = np.arange(5, 15)
result3 = np.arange(50, 100, 5)

print(result2)
print(result3)

result4 = np.zeros(10)
result5 = np.ones(10)

print(result4)
print(result5)

result6 = np.linspace(0, 100, 5)
result7 = np.random.randint(10, 30, 5)
result8 = np.random.randn(10)

print(result6)
print(result7)
print(result8)

result9 = np.random.randint(10, 50, 15).reshape(3, 5)
print(result9)

matrixOne = np.random.randint(10, 50, 15).reshape(3, 5)
rowTotal = matrixOne.sum(axis=1)
columnTotal = matrixOne.sum(axis=0)
print(matrixOne)
print(rowTotal)
print(columnTotal)
print("==========")
print("==========")

result10 = matrixOne.max()
result11 = matrixOne.min()
result12 = matrixOne.mean()
result13 = matrixOne.argmax()
result14 = matrixOne.argmin()
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)

numpyArrayOne = np.arange(10, 20)
result15 = numpyArrayOne[0:3]
result16 = numpyArrayOne[::-1]
result17 = matrixOne[0]
result18 = matrixOne[2, 2]
result19 = matrixOne[:, 0]
print(result15)
print(result16)
print(f"Matrix One..: {matrixOne}")
print(result17)
print(result18)
print(result19)
result20 = np.power(matrixOne, 2)
result21 = (matrixOne % 2 == 0)
result22 = (matrixOne > 0)
result23 = (result21 & result22)
print(matrixOne[result23])
print(result21)
print(result20)
print(result22)
print(result23)
