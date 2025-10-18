#Problem 2: Unit converter

print("=== unit converter ===")
print("1.miles to kilometers")
print("2.celsius to fahrenheit")
choice =input("choose conversion(1 or 2):")

if choice =="1":
  #miles to kilometer
  miles = float(input("Enter distance in miles:"))
  kilometers = miles*1.60934
  print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
  
elif choice =="2":
  #celsius to fahrenheit
  celsius = float(input("Enter temperature in celsius:"))
  Fahrenheit = (celsius*9/5)+32
  print(f"{Celsius} deg c is equal to{Fahrenheit:.2f} deg f.")

else:
  print("Invalid Choice! Please Enter 1 or 2.")
