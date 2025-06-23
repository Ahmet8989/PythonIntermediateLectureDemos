class SuperHero():

    specialPower = "Super strength"

    def __init__(self, name, age, occupation):
        self.superHeroName = name
        self.superHeroAge = age
        self.superHeroOccupation = occupation
        print("Init is called")

    def sayHello(self):
        print(f"Hello, my name is {self.superHeroName}, i am {self.superHeroAge} years old, i am a {self.superHeroOccupation}. My super power is {self.specialPower}.")

superman = SuperHero("Clark Kent / Journalist", 34, "Journalist")
superman.sayHello()

class Dog():

    yearMultiplier = 7

    def __init__(self, age = 5):
        self.age = age

    def transformHumanAge(self):
        return (self.age * Dog.yearMultiplier)

defaultDog = Dog()
myDog = Dog(3)

print(f"Default dog {defaultDog.age} years old.")
print("===============")
print(f"My dog {myDog.age} years old.")
print(defaultDog.transformHumanAge())