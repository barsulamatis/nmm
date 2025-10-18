password_input = input("Enter your password: ")

if len(password_input) < 8:
    print("Password must be at least 8 characters long.")
elif not any(char.isdigit() for char in password_input):
    print("Password must contain at least one number.")
elif not any(char.isupper() for char in password_input):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password_input):
    print("Password must contain at least one lowercase letter.")
elif not any(char in "!@#$%^*()_+-=" for char in password_input):
    print("Password must contain at least one special character.")
else:
    print("Password is valid.")