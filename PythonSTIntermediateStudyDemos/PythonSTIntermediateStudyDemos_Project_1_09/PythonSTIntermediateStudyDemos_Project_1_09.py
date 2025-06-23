import random

# value = dir(random)
# value2 = help(random)
value3 = random.random() # 0.0 - 1.0
value4 = random.random() * 100
value5 = random.uniform(1, 15) # 1 - 15
value6 = random.randint(1, 100) # 1 - 100
names = ["Jessica", "James", "John", "Julie"]
value7 = names[random.randint(1, (len(names) - 1))]
value8 = random.choice(names)
list9 = list(range(10))
value9 = list9
value10 = random.shuffle(list9)
value14 = random.sample(list9, 3)

# print(value)
# print(value2)
print(value3)
print(value4)
print(value5)
print(value6)
print(value7)
print(value8)
print(value9)
print(value10)
print(value14)
