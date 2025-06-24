def calculateGrades(line):
    line = line[:-1]
    listOne = line.split(":")
    
    studentFullNmae = listOne[0]
    studentGrades = listOne[1].split(",")

    gradeOne = int(studentGrades[0])
    gradeTwo = int(studentGrades[1])
    gradeThree = int(studentGrades[2])

    gradeAvarage = (gradeOne + gradeTwo + gradeThree) / 3
    if((gradeAvarage >= 90) and (gradeAvarage <= 100)):
        letter = "AA"
    elif ((gradeAvarage >= 80) and (gradeAvarage < 90)):
        letter = "BA"
    elif ((gradeAvarage >= 70) and (gradeAvarage < 80)):
        letter = "BB"
    elif ((gradeAvarage >= 60) and (gradeAvarage < 70)):
        letter = "C"

    return studentFullNmae + ": " + letter + "\n"

def readAverages():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)

def readGradeLetters():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculateGrades(line))

def enterGrades():
    name = input("Student name..: ")
    sirname = input("Student sirname..: ")
    gradeOne = input("Grade One..: ")
    gradeTwo = input("Grade Two..: ")
    gradeThree = input("Grade Three..: ")

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        content = f"{name} {sirname}:{gradeOne},{gradeTwo},{gradeThree}\n"
        file.write(content)


def saveGrades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        listFive = []
        for line in file:
            listFive.append(calculateGrades(line))
        with open("exam_results.txt", "w", encoding="utf-8") as file2:
            for i in listFive:
                file2.write(i)

while True:
    fileOperation = input("1-) Read the Grades\n2-) Enter the Grades\n3-) Save the Grades\n4-) Quit\n")

    if (fileOperation == '1'):
        readAverages()
    elif (fileOperation == '2'):
        enterGrades()
    elif (fileOperation == '3'):
        saveGrades()
    elif (fileOperation == '4'):
        break
    else:
        print("Invalid Option Entered")