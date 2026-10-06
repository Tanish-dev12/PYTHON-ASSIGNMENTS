def is_right_angled(a, b, c):
    sides = sorted([a, b, c])
    
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    return False

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if is_right_angled(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
