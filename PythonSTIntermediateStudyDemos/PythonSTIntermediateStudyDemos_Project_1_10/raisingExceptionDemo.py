x = 4

if (x > 5):
    raise Exception("X can not greater than 5")

def checkPassword(password):
    import re
    if(len(password) < 8):
        raise Exception("Password should have at least 8 characters.")
    elif(not re.search("[a-z]", password)):
        raise Exception("Password should include lower characters.")
    elif(not re.search("[A-Z]", password)):
        raise Exception("Password should include upper characters.")

try:
    checkPassword("345345345dD")
except Exception as e:
    print(e)