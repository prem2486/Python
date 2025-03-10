def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible for Voting")


# Calling Function
check_age(15)
