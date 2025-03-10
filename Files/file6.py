import os

file_name = "file.txt"

# Check Read Access
if os.access(file_name, os.R_OK):
    print("File has Read Access")
else:
    print("File does not have Read Access")

# Check Write Access
if os.access(file_name, os.W_OK):
    print("File has Write Access")
else:
    print("File does not have Write Access")
