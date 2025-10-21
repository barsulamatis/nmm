print("=== Datatype & I/O Exercises ===\n")

num = int(input("Enter a number: "))
print("Integer:", num, "| Type:", type(num))

flt = float(input("Enter a decimal: "))
print("Float:", flt, "| Type:", type(flt))

name = input("Enter your name: ")
print("String:", name.upper(), "| Length:", len(name))

is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"
print("Boolean:", is_student, "| Type:", type(is_student))