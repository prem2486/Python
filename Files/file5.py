# Program to read a file from a particular index
file = open("file.txt", "r")
file.seek(5)
print(file.read())
file.close()
