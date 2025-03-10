def insert_element(arr, index, value):
    arr.insert(index, value)
    return arr

arr = [10, 20, 30, 40, 50]
index = int(input("Enter index: "))
value = int(input("Enter value: "))
print("Array after insertion:", insert_element(arr, index, value))
