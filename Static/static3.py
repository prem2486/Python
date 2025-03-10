class MyClass:
    static_var = 10  # Static Variable

obj1 = MyClass()
obj2 = MyClass()

# Changing the static variable through instance
obj1.static_var = 20

print("obj1 static_var:", obj1.static_var)
print("obj2 static_var:", obj2.static_var)
print("Class static_var:", MyClass.static_var)
