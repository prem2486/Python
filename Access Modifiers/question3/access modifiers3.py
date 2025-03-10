class PublicExample:
    name = "Prem Kumar"  # Public Field
    
    def __init__(self):
        self.age = 22    # Public Field
    
    def public_method(self):
        print("This is a Public Method")
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        self.public_method()

# Accessing Public Fields from Same Class
obj = PublicExample()
obj.display()

# Accessing Public Fields from Another Class
class AnotherClass:
    def access_public(self):
        print("Accessing Public Field from Another Class")
        print("Name:", obj.name)
        obj.public_method()

# Another Class Object
another_obj = AnotherClass()
another_obj.access_public()
