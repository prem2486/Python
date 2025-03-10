from abstractclass1 import AbstractClass

class SubClass(AbstractClass):
    
    def abstract_method(self):
        print("This is an Abstract Method (Implemented in Subclass)")

# Create Object for Subclass
obj = SubClass()

# Access Non-Abstract Method from Abstract Class
obj.non_abstract_method()
