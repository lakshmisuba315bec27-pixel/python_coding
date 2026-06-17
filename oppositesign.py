def have_opposite_signs(x, y):
    return (x ^ y) < 0
-
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

if have_opposite_signs(num1, num2):
    print("Output: True (The signs are opposite)")
else:
    print("Output: False (The signs are the same)")
