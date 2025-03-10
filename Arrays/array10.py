arr = [10, 20, 30, 40, 20, 10, 50]
duplicates = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)
