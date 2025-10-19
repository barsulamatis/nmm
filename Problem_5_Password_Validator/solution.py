# take input from user
name=input("enter your name:").strip()
password=input("enter the password").strip()
missing_rules = []
if len(password)<8:
    missing_rules.append("password must be at least 8 characters")
if not any(char.isdigit() for char in password):
     missing_rules.append("password is at least contain one digit")
if password.lower()== name.lower():
     missing_rules.append("password is must not be the same as your name")    
if not missing_rules:
    print("Your password is strong ")
else:
    print("Your password is weak . Missing rules:")
    for rule in missing_rules:
        print("-", rule)
     