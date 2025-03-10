from abstractclass1 import AbstractClass

class SubClass(AbstractClass):
    
    def abstract_method(self):
        print("This is an Abstract Method (Implemented in Subclass)")

    def child_class_method(self):
        print("This is a Child Class Method")

# Create Object for Subclass
obj = SubClass()

# Call Non-Abstract Method of Parent Class
obj.non_abstract_method()

# Call Non-Abstract Method of Child Class
obj.child_class_method()
