with open("newfile.txt", "r+", encoding="utf-8") as file:
    listOne = file.readlines()
    listOne.insert(0, "Hello World-1\n")
    file.seek(0)
    for i in listOne:
        file.write(i)

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())

print("==========")

with open("newfile.txt", "r+", encoding="utf-8") as file:
    listOne = file.readlines()
    listOne.insert((len(listOne)), "\nHello World4\n")
    file.seek(0)
    file.writelines(listOne)

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())