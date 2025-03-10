try:
    with open("file.txt", "w") as file:
        file.write("Hello")
    with open("file.txt", "r") as file:
        data = file.read()
        print(data)
except IOError:
    print("Input-Output Exception Occurred")
