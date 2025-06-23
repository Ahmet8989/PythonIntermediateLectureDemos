class Apple():
    def __init__(self, name):
        self.name = name

    def giveInfo(self):
        return f"{self.name} -> 100 calories"

class Banana():
    def __init__(self, name):
        self.name = name

    def giveInfo(self):
        return f"{self.name} -> 155 calories"

appleOne = Apple("Apple")
print(appleOne.giveInfo())
print("==========")
bananaOne = Banana("Banana")
print(bananaOne.giveInfo())
print("==========")
fruitBasket = [appleOne, bananaOne]
for fruit in fruitBasket:
    print(fruit.giveInfo())
print("==========")
def receiveInfo(fruit):
    print(fruit.giveInfo())

receiveInfo(appleOne)
print("==========")
receiveInfo(bananaOne)
print("==========")