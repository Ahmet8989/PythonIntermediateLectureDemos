def addTheNumbers(numberOne, numberTwo):
    return numberOne + numberTwo

# try - except - else - finally

while(True):
    try:
        x = int(input("Enter the first number..: "))
        y = int(input("Enter the second number..: "))
    except:
        print("Please enter a valid number")
        continue
    else:
        print("Thank you")
        break
    finally:
        # This part called always
        print("Finally called")

print(addTheNumbers(x, y))