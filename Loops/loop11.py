num = int(input("Enter a number: "))

switch = {
    0: "Even",
    1: "Odd"
}

print(num, "is", switch[num % 2])
