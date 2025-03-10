def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


# Calling the method without try block
result = divide(10, 0)
print("Result:", result)
