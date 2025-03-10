from same_package import ProtectedExample

class SubClass(ProtectedExample):
    def access_protected(self):
        print("Accessing Protected Field from SubClass in Different Package")
        print("Name:", self._name)
        self._protected_method()

# Subclass Object
obj = SubClass()
obj.access_protected()

# Accessing Protected Field from Non-Subclass (will raise error)
# obj2 = ProtectedExample()
# print(obj2._name)  # Error
