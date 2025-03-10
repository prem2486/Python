num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            print(num, "is not a Prime number.")
            break
    else:
        print(num, "is a Prime number.")
else:
    print(num, "is not a Prime number.")
