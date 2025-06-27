import os

# result = dir(os)

# print(result)

# os.chdir('C:\\') -> change our current location to C: directory
# os.mkdir("newdirectory") -> generates new directory which name is ("newdirectory")
# os.makedirs("newdirectory/anothernewdirectory") -> generates folder inside another folder
# result = os.listdir("c:\\") -> it lists directories in this location
# os.rename("newdirectory", "newwwdirectory") -> change the name of the directory
# os.rmdir("newdirectory") -> remove directory
# os.removedirs("newdirectory/anothernewdirectory") -> remove directories
# os.system("notepad.exe") -> open the file

'''
for file in os.listdir():
    if (file.endswith(".py")):
        print(file)
'''

result2 = os.name
result3 = os.getcwd()
result4 = os.listdir()
# result5 = os.stat("osModuleDemo.py")
result6 = os.path.abspath('osModuleDemo.py')
result7 = os.path.dirname(result6)
# when you upload something you should check does it exists, maybe you change your file name
result8 = os.path.exists(result6)
result9 = os.path.isdir(result7)
# result10 = os.path.join("C:\\", "newFolder") -> it generates a path, not a directory
# result10 = os.path.split("C:\\newFolder")
result10 = os.path.splitext("osModuleDemo.py")
print(f"Result 2..: {result2}")
print("==========")
print(f"Result 3..: {result3}")
print("==========")
print(f"Result 4..: {result4}")
print("==========")
# print(f"Result 5..: {result5}")
print("==========")
print(f"Result 6..: {result6}")
print("==========")
print(f"Result 7..: {result7}")
print("==========")
print(f"Result 8..: {result8}")
print("==========")
print(f"Result 9..: {result9}")
print("==========")
print(f"Result 10..: {result10}")
print("==========")
