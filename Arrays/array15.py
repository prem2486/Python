arr = [10, 21, 32, 41, 53, 62]

even = len([i for i in arr if i % 2 == 0])
odd = len([i for i in arr if i % 2 != 0])

print("Even Numbers:", even)
print("Odd Numbers:", odd)
