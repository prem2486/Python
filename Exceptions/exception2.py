a = 10
b = 0

try:
    c = a / b
    print("Result:", c)
except ZeroDivisionError:
    print("Cannot divide by zero")
