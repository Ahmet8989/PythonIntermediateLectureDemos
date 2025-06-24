with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())
    # Find the place of the cursor
    cursorPlace = file.tell()

print("==========")

with open("newfile.txt", "r+", encoding="utf-8") as file:
    # Send the cursor desired place
    file.seek(cursorPlace)
    file.write("\nExample")

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())

print("==========")

with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nExample")

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())