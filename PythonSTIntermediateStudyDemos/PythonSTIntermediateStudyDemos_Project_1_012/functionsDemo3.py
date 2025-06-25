import math
import time


def myDecorator(func):
    def wrapper():
        print("Operations before the function")
        func()
        print("Operations after the function")

    return wrapper()

def sayHello():
    print("Hello")

def sayGreetings():
    print("Greetings")

@myDecorator
def sayAnotherGreetings():
    print("Another greetings")

print("==========")

myDecorator(sayHello)
print("==========")
myDecorator(sayGreetings)
print("==========")

def calculateTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Completion of a function take " + str(finish - start) + " seconds.")

    return inner

@calculateTime
def takeExponent(a, b):
    print(math.pow(a, b))

@calculateTime
def findFactorial(number):
    print(math.factorial(number))

takeExponent(3, 4)
findFactorial(6)
