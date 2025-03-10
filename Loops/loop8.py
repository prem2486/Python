num = int(input("Enter a number: "))
original_num = num
result = 0

while original_num != 0:
    digit = original_num % 10
    result += digit ** 3
    original_num //= 10

if result == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
