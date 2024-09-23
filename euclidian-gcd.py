# S
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("GCD: ", a)
    print("")

larger = a if a > b else b
smaller = a if a < b else b

print("Recursive calls:")
while True:
    print(f"gcd({larger}, {smaller})")
    remainder = larger % smaller
        
    if remainder == 0:
        print("GCD: ", smaller)
        break
        
    larger = smaller
    smaller = remainder

        