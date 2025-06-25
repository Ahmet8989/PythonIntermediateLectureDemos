def outer(number):

    def inner(power):
        return number ** power

    return inner

power = outer(2)
result = power(3)
print(result)
print("==========")

def outer(page):
    def inner(role):
        if (role == "Admin"):
            message = "{0} role can reach {1} page".format(role, page)
            return message
        else:
            return "{0} role can not reach {1} page.".format(role, page)

    return inner

userOne = outer("Product Edit")
result2 = userOne("Admin")
print(result2)