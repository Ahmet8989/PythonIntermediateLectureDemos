class Person():
    # Class attributes
    adress = "No information"


    # Constructor
    # Self parameter represents the object derived from the class
    def __init__(self, name, year):
        # Object attributes
        self.name = name
        self.birthyear = year
        print("Init method worked")

    # instance methods
    def intro(self):
        print("Hello There.. I am " + self.name)

    def calculateAges(self):
        return 2023 - self.birthyear

# object (instance)

p1 = Person("Jane", 1998)

# Accessing object attributes
print(type(p1))
print(f"Name..: {p1.name}")
print(f"Birthyear..: {p1.birthyear}")
print(f"Address..: {p1.adress}")

# Updating
p1.adress = "London"

print("=========")
# Accessing object attributes
print(type(p1))
print(f"Name..: {p1.name}")
print(f"Birthyear..: {p1.birthyear}")
print(f"Address..: {p1.adress}")
print(f"My age..: {p1.calculateAges()}")
p1.intro()

class Circle():

    # class object attribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def calculatePerimeter(self):
        return (2 * self.pi * self.radius)
    
    def calculateArea(self):
        return (self.pi * self.radius * self.radius)

c1 = Circle() # radius equals 1
c5 = Circle(6) # radius equals 6


print(f"PerimeterOne..: {c1.calculatePerimeter()}")
print(f"AreaOne..: {c1.calculateArea()}")
print(f"PerimeterFive..: {c5.calculatePerimeter()}")
print(f"AreaFive..: {c5.calculateArea()}")