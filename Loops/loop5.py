a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print("Larger number:", a)
    print("Smaller number:", b)
elif b>a and b>c:
    print("Larger number:", b)
    print("Smaller number:", a)
else:
    print("Larger number:", c)
    print("Smaller number:", a)