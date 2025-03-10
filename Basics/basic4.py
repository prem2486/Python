global_var = "I am Global"

def my_function():
    global_var = "I am Local"
    print("Inside the function:", global_var)

my_function()
print("Outside the function:", global_var)
