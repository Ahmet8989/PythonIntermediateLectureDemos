class Animal():
    def __init__(self):
        print("Animal - Class - Init - Function - Called")

    def method5(self):
        print("Animal - Class - Function - Method5 - Called")

    def method6(self):
        print("Animal - Class - Function - Method6 - Called")

class Cat(Animal):
    def __init__(self):
        print("Cat - Class - Init - Function - Called")
        Animal.__init__(self)

    def sayHello(self):
        print("Miyaaav")

    # Override
    def method5(self):
        print("Cat - Class - Function - Method5 - Called")

myAnimal = Animal()
print("==========")
myCat = Cat()
myCat.method5()