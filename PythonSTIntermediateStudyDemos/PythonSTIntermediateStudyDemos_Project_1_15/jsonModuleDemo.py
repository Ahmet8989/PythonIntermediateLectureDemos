import json
from os import name

'''
person_string = '{"name" : "Jason", "languages" : ["Pyhon", "Java", "c++"]}'
# JSON string to Dictionary
result = json.loads(person_string)
print(type(result))
print(result)
result2 = result["name"]
result3 = result["languages"]
print("==========")
print(result2)
print(result3)
'''
'''
fileOne = open("person.json", "x", encoding="utf-8")
fileOne.close()
'''
with open("person.json") as fileFive:
    data = json.load(fileFive)
    print(data)
    print("===")
    print(data["name"])
    print("===")
    print(data["languages"])

personDictionary = {"name" : "Jenny", "languages" : ["Pyhon", "Java", "c#"]}

# Dictionary to JSON String

'''
result = json.dumps(personDictionary)
print(type(result))
'''

with open("person.json", "a") as file:
    json.dump(personDictionary, file)

