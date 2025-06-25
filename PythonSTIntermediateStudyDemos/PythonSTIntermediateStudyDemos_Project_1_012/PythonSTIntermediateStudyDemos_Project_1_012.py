def outer(numOne):
    print("Outer function called")
    def inner_increment(numOne):
        print("Inner function called")
        return numOne + 1
    numTwo = inner_increment(numOne)
    print(f"Num one..: {numOne}, num two..: {numTwo}")
outer(15)

def factorial(number):

    if not isinstance(number, int):
        raise TypeError("You must be enter an integer number")

    if not (number >= 0):
        raise ValueError("You must be enter an integer number greater than 0")

    def innerFactorial(number):
        if(number <= 1):
            return 1

        return number * innerFactorial(number - 1)

    return innerFactorial(number)

try:
    result = factorial(6)
    print(result)
except Exception as ex:
    print(ex)