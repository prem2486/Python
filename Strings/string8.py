str1 = "Hello World"

# startswith()
print("Starts with 'Hello':", str1.startswith("Hello"))

# endswith()
print("Ends with 'World':", str1.endswith("World"))

# compareTo() equivalent
str2 = "Hello"
str3 = "World"

if str2 > str3:
    print("str2 is greater than str3")
elif str2 < str3:
    print("str2 is smaller than str3")
else:
    print("Both are equal")
