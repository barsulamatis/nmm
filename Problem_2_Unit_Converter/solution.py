# your code here
print("Choose a conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter 1 or 2: ")
if choice == '1':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit_result = (celsius * 9/5) + 32
    print("The temperature in Fahrenheit is: {fahrenheit_result:.2f}°F")
elif choice == '2':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius_result = (fahrenheit - 32) * 5/9
    print("The temperature in Celsius is: {celsius_result:.2f}°C")
else:
    print("Invalid choice.")
