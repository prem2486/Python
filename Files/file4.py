# Program to read a file with random access
file = open("file.txt", "r")
file.seek(10)  # Move the cursor to 10th position
print(file.read())
file.close()
