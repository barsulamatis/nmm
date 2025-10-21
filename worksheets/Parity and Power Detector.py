"""

Input an integer.

Print:

Whether it’s even or odd using num & 1

Whether it’s a power of two using (num & (num - 1)) == 0
"""

n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")

if n != 0 and (n & (n-1)) == 0:
    print(f"{n} is a Power of 2")
else:
    print(f"{n} is NOT a Power of 2")