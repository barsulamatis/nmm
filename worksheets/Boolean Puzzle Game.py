print("=== Boolean Puzzle Access System ===\n")


verified = input("Is user verified? (yes/no): ").strip().lower() == "yes"
user_id = int(input("Enter user ID (integer): "))
flags = int(input("Enter security flags (integer): "))


access = (
    verified and                     
    (user_id & 1 == 0) and           
    (flags & 0b111 != 0)           
)


if access:
    print("Access Granted!")
else:
    print("Access Denied!")

if not access:
    if not verified:
        print("- User not verified")
    if user_id & 1 != 0:
        print("- User ID is not even")
    if flags & 0b111 == 0:
        print("- Security flags last 3 bits are all 0")

print("\n=== End of Puzzle ===")