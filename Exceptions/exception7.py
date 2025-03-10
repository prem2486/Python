try:
    a = 10
    b = 0
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Finally block executed")
