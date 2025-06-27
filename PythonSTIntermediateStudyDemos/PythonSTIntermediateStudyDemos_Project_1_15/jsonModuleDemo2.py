import json
import os
class User:
    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email

class UserRepository:

    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if(os.path.exists('users.json')):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    print(user['userName'])
                    print(user)
                    newUser = User(userName = user['userName'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user : User):
        self.users.append(user)
        self.saveToFile()
        print("USER ACCOUNT GENERATED")

    def login(self, userName, password):
        for user in self.users:
            if((user.userName == userName) and (user.password == password)):
                self.isLoggedIn = True
                self.currentUser = user
                print("LOGIN")

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("LOGOUT")

    def identity(self):
        if(self.isLoggedIn):
            print(f"Username..: {self.currentUser.userName}")
        else:
            print("There is no user logged in")

    def saveToFile(self):
        listOne = []
        for user in self.users:
            listOne.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(listOne, file)


userRepository = UserRepository()

while True:
    print("MENU".center(30, '*'))
    choosingOption = input("1-) Register\n2-) Login\n3-) Logout\n4-) Identity\n5-) Exit\nEnter Option..:")
    if(choosingOption == '1'):
        userName = input("Enter a username..: ")
        password = input("Enter a password..: ")
        email = input("Enter an email..: ")

        user = User(userName = userName, password = password, email = email)
        userRepository.register(user)

    elif(choosingOption == '2'):
        if(userRepository.isLoggedIn):
            print("You already logged in")
        else:
            userName = input("UserName..: ")
            password = input("Password..: ")
            userRepository.login(userName, password)

    elif(choosingOption == '3'):
        userRepository.logout()

    elif(choosingOption == '4'):
        userRepository.identity()

    elif(choosingOption == '5'):
        break
    else:
        print("Invalid Option")