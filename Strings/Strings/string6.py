import re

str1 = "Hello123"
pattern = r"^[A-Za-z]+[0-9]+$"

if re.match(pattern, str1):
    print("String matches the pattern")
else:
    print("String does not match the pattern")
