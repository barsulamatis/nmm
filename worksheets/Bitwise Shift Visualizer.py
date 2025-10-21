"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
print("=== Bitwise Shift Visualizer ===\n")


num = int(input("Enter an integer: "))
shift = int(input("Enter number of shift positions: "))


print(f"\nOriginal: {num} -> {bin(num)}")


left = num << shift
print(f"Left shift  {shift}: {left} -> {bin(left)}")

right = num >> shift
print(f"Right shift {shift}: {right} -> {bin(right)}")

print("\n=== End of Visualizer ===")