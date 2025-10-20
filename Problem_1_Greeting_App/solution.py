# your code here
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

print(f"\nHello {name}! It's great to know that your favorite food is {favorite_food}.")

birth_year = year - age
print(f"You were born in the year {birth_year}.")
