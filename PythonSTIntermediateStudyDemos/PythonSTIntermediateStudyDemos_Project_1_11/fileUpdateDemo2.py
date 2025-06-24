with open("newfile.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "Hello World Added\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())