from builtins import StopIteration


listOne = [1, 2, 3, 4,5]

iteratorOne = iter(listOne)

print(next(iteratorOne))
print(next(iteratorOne))
print(next(iteratorOne))
print(next(iteratorOne))
print(next(iteratorOne))
print("==========")

listTwo = [4, 5, 6, 7, 8, 9]
iteratorTwo = iter(listTwo)
while True:
    try:
        element = next(iteratorTwo)
        print(element)
    except StopIteration:
        break

class MyNumbers():

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start 
            self.start += 1
            return x
        else:
            raise StopIteration

listThree = MyNumbers(1, 19)
for item in listThree:
    print(item)