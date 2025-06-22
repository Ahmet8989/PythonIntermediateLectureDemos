class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Generated")

    def whoAmI(self):
        print("I am a person")

    def eat(self):
        print("I eat")

class Student(Person):
    def __init__(self, fname, lname, number):
        self.studentNumber = number
        Person.__init__(self, fname, lname)
        print("Student Generated")

    # override
    def whoAmI(self):
        print("I am a student")

    def sayHello():
        print("Hello, I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def whoAmI(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Jonathan", "Tucker")
p1.whoAmI()
p1.eat()
print(p1.firstName + " " + p1.lastName)
print("============")
s1 = Student("Jane", "North", 456567)
p1.whoAmI()
s1.eat()
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))
print("============")
t1 = Teacher("Jessica", "Black", "Math")
t1.whoAmI()