class MyClass:
    # Public Constructor
    def __init__(self):
        print("Public Constructor Called")
    
    # Protected Constructor
    def _protected_constructor(self):
        print("Protected Constructor Called")
    
    # Private Constructor
    def __private_constructor(self):
        print("Private Constructor Called")


# Creating Object
obj = MyClass()
obj._protected_constructor()

# Cannot call private constructor directly
# obj.__private_constructor() --> This will give error
