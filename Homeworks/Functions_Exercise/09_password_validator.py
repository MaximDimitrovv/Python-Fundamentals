def password_validator(password):

    invalid = 0
    if len(password) < 6 or len(password) > 10:
        invalid += 1
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        invalid += 1
        print("Password must consist only of letters and digits")

    digit_counter = 0

    for char in password:
        if char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        invalid += 1
        print("Password must have at least 2 digits")

    if invalid == 0:
        print("Password is valid")




string = input()

password_validator(string)