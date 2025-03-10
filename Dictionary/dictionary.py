# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
students = {
    101: "John",
    102: "Mike",
    103: "Sara",
    104: "Emma",
    105: "David"
}
print("Initial Dictionary:", students)

# 1.1 Adding the values in dictionary
students[106] = "Oliver"
print("\nAfter Adding a Value:", students)

# 1.2 Updating the values in dictionary
students[102] = "Michael"
print("\nAfter Updating a Value:", students)

# 1.3 Accessing the value in dictionary
print("\nAccessing Value for ID 103:", students[103])

# 1.4 Create a nested loop dictionary
student_details = {
    101: {"name": "John", "age": 20, "course": "BCA"},
    102: {"name": "Mike", "age": 21, "course": "BCA"},
    103: {"name": "Sara", "age": 19, "course": "BCA"},
}
print("\nNested Dictionary:", student_details)

# 1.5 Access the values of nested loop dictionary
print("\nAccessing Nested Value for ID 102:", student_details[102]['name'])

# 1.6 Print the keys present in a particular dictionary
print("\nKeys in Student Dictionary:", students.keys())

# 1.7 Delete a value from a dictionary
del students[105]
print("\nAfter Deleting ID 105:", students)
