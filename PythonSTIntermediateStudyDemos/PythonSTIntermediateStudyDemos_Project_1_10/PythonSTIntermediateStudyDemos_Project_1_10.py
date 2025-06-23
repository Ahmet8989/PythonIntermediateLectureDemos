try:
    x = int(input("X..: "))
    y = int(input("Y..: "))
    result = (x/y)
    print(result)
except ZeroDivisionError:
    print("0 is not a valid option for y")
except ValueError:
    print("You should enter only numerical values for x and y.")

try:
    x = int(input("X..: "))
    y = int(input("Y..: "))
    result = (x/y)
    print(result)
except Exception as e:
    print("Please try again..: ", e)

