def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

arr = [10, 20, 30, 40, 50]
value = int(input("Enter value to remove: "))
print("Array after removal:", remove_element(arr, value))
