class Parent:
    def __init__(self):
        print("Parent Default Constructor Called")
    
    def __init__(self, msg):
        print("Parent Argument Constructor Called")
        print("Message:", msg)


class Child(Parent):
    def __init__(self):
        super().__init__("Hello from Parent")
        print("Child Default Constructor Called")


# Creating Child Object
obj = Child()
