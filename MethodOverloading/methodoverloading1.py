class MyClass:
    def add(self, a):
        print("Sum with 1 parameter:", a)
    
    def add(self, a, b):
        print("Sum with 2 parameters:", a + b)


# Creating Object
obj = MyClass()
# obj.add(5)   # This will give an error because the latest method will override the first one
obj.add(5, 10)
