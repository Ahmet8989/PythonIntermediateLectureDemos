def additionOne(a, b):
    return a + b
def subtractionOne(a, b):
    return a -b
def multiplicationOne(a, b):
    return a * b
def divisionOne(a, b):
    return a / b
def operationOne(f1, f2, f3, f4, operationName, d, v):
    if (operationName == "additionOne"):
        print(additionOne(d, v))
    elif (operationName == "subtractionOne"):
        print(subtractionOne(d, v))
    elif (operationName == "multiplicationOne"):
        print(multiplicationOne(d, v))
    elif (operationName == "divisionOne"):
        print(divisionOne(d, v))
    else:
        print("Invalid operation")

operationOne(additionOne, subtractionOne, multiplicationOne, divisionOne, "multiplicationOne", 5, 7)