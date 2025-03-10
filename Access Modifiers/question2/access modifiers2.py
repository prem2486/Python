class ProtectedExample:
    _name = "Prem Kumar"  # Protected Field
    
    def __init__(self):
        self._age = 22    # Protected Field
    
    def _protected_method(self):
        print("This is a Protected Method")
    
    def display(self):
        print("Name:", self._name)
        print("Age:", self._age)
        self._protected_method()

# Accessing from Same Package
obj = ProtectedExample()
obj.display()

class AnotherClass:
    def access_protected(self):
        print("Accessing Protected Field from Another Class")
        print("Name:", obj._name)
        obj._protected_method()

# Accessing from Same Package
another_obj = AnotherClass()
another_obj.access_protected()
