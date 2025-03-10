class MyClass:
    static_var = 10  # Static Variable

# Changing the static variable through class
MyClass.static_var = 50

obj1 = MyClass()
obj2 = MyClass()

print("obj1 static_var:", obj1.static_var)
print("obj2 static_var:", obj2.static_var)
print("Class static_var:", MyClass.static_var)
