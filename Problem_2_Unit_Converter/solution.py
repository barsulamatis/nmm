convert = input("Enter the unit to convert from (Celsius/Fahrenheit): ")
if convert == "Celsius":
    fahrenheit = float(input("Enter temperature in Celsius: "))
    fahrenheit = (fahrenheit * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
elif convert == "Fahrenheit":
    celsius = float(input("Enter temperature in Fahrenheit: "))
    celsius = (celsius - 32) * 5/9
    print(f"Temperature in Celsius: {celsius}")
else:
    print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")