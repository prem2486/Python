# Program to read a file using file stream
file = open("file.txt", "r")
for line in file:
    print(line, end="")
file.close()
