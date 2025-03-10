# Class 1
class Class1:
    def __init__(self):
        print("Class1 Constructor is Called")

    def display_message(self):
        print("This is Class1 Method")


# Class 2
class Class2:
    def __init__(self):
        print("Class2 Constructor is Called")

    def show_message(self):
        print("This is Class2 Method")


# Creating Object for Class1
obj1 = Class1()
obj1.display_message()

print("--------------------")

# Creating Object for Class2
obj2 = Class2()
obj2.show_message()
