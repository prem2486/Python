class MyException(Exception):
    pass


def check_value(num):
    if num < 0:
        raise MyException("Negative numbers are not allowed")
    print("Number is valid")


# Calling Function
check_value(-5)
