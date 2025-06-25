def cube():

    result = []

    for i in range(5):
        result.append(i ** 3)

    return result

print(cube())
print("==========")
def cube2():
    for i in range(5):
        yield i ** 3

generatorOne = cube2()
iteratorOne = iter(generatorOne)
while True:
    try:
        element = next(iteratorOne)
        print(element)
    except StopIteration:
        break

