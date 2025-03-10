arr = [10, 20, 30, 40, 50]
element = int(input("Enter element to find: "))

if element in arr:
    print("Index of", element, ":", arr.index(element))
else:
    print("Element not found")
