print("=== Bit Masking Practice ===\n")

x = 37  
print("x in binary:", bin(x))


print("5th bit:", (x & (1 << 4)) >> 4)

x = x | (1 << 1)
print("After setting 2nd bit:", bin(x))


x = x & ~(1 << 3)
print("After clearing 4th bit:", bin(x))

x = x ^ (1 << 0)
print("After toggling 1st bit:", bin(x))

print("Number of 1s:", bin(x).count('1'))

print("\n=== End of Bit Masking Practice ===")