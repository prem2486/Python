class MyClass:
    def display(self, a):
        print("Integer value:", a)
    
    def display(self, a, b):
        print("Integer and String:", a, b)


# Creating Object
obj = MyClass()
# obj.display(5)   # This will give an error because the second method overrides the first
obj.display(5, "Hello")
