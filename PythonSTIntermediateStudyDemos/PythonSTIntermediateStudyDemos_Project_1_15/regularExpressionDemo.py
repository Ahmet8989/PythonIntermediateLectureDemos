import re

# re MODULE

strOne = "Python Lectures : Python Programming | 40 Hours"

result = re.findall("Python", strOne)
result2 = len(result)
result3 = re.split(" ", strOne)
result4 = re.sub(" ", "-", strOne)
result5 = re.sub("\s", "-", strOne)
result6 = re.search("Python", strOne)
result7 = result6.span()
result8 = result6.start()
print(result)
print("==========")
print(result2)
print("==========")
print(result3)
print("==========")
print(result4)
print("==========")
print(result5)
print("==========")
print(result6)
print("==========")
print(result7)
print("==========")
print(f"Result 8..: {result8}")
print("==========")

# Regular Expressions

result9 = re.findall("[abc]", strOne)
result10 = re.findall("[sat]", strOne)
result11 = re.findall("[a-f]", strOne) # search (abcdef)
result12 = re.findall("[0-6]", strOne) # search (0123456)
result13 = re.findall("[^abc]", strOne) # search all characters but (abc)
result14 = re.findall("...", strOne)
result15 = re.findall("Py..on", strOne)
result16 = re.findall("^P", strOne)
result16 = re.findall("t$", strOne)