class MyClass:
    def __init__(self, name=None, age=None):
        if name is None and age is None:
            print("Default Constructor Called")
        elif age is None:
            print("One Argument Constructor Called")
            print("Name:", name)
        else:
            print("Two Argument Constructor Called")
            print("Name:", name)
            print("Age:", age)


# Creating objects to call all constructors
obj1 = MyClass()
obj2 = MyClass("John")
obj3 = MyClass("John", 25)
