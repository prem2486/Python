def contains(arr, value):
    return value in arr

arr = [10, 20, 30, 40, 50]
value = int(input("Enter value to check: "))
print("Contains:", contains(arr, value))
