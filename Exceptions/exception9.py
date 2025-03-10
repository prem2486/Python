try:
    file = open("nonexistent.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
