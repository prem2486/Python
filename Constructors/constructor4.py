class Student:
    def __init__(self, name, age):
        # Attributes of Constructor
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating Object
student = Student("John", 22)
student.display()
