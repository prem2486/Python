class Student:
    def __init__(self):
        self.name = "John"


obj = Student()
try:
    print(obj.age)  # Field does not exist
except AttributeError:
    print("No Such Field Exception")
