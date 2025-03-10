class PrivateExample:
    __name = "Prem Kumar"  # Private Field
    
    def __init__(self):
        self.__age = 22    # Private Field
    
    def __private_method(self):
        print("This is a Private Method")
    
    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        self.__private_method()

# Main Method
obj = PrivateExample()
obj.display()

# Trying to Access Private Fields (This will raise an error)
# print(obj.__name)  # AttributeError
# obj.__private_method()  # AttributeError

# Create a Subclass
class SubClass(PrivateExample):
    def access_private(self):
        # Trying to access private fields and methods from subclass
        # print(self.__name)  # AttributeError
        # self.__private_method()  # AttributeError
        print("Cannot Access Private Fields or Methods from SubClass")

# Subclass Object
sub_obj = SubClass()
sub_obj.access_private()
