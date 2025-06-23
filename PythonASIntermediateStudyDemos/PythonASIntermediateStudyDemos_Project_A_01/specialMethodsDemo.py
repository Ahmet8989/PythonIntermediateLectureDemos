class Fruit():
    def __init__(self, name, calory):
        self.name = name
        self.calory = calory

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return self.calory

fruitOne = Fruit("Banana", 355)
print(fruitOne)
print(len(fruitOne))