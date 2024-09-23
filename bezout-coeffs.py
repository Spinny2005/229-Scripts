# S
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("GCD: ", a)
    print("s: 1")
    print("t: 0")
    print(f"{a} = 1 * {a} + 0 * {b}")

larger = a if a > b else b
smaller = a if a < b else b

s = 1
t = 0
s_prev = 0
t_prev = 1

print("\nSteps:")

while True:
    remainder = larger % smaller
    quotient = larger // smaller

    if remainder == 0:
        print("")
        print("GCD: ", smaller)
        print("s: ", s)
        print("t: ", t)
        print(f"{smaller} = {t} * {a} + {s} * {b}")
        break

    print(f"{smaller} = {t} * {a} + {s} * {b}")
    print(f"{larger} = {smaller} * {quotient} + {remainder}")
    print(f"{remainder} = {larger} - {(smaller * quotient)}\n")

    s, s_prev = s_prev - quotient*s, s
    t, t_prev = t_prev - quotient*t, t

    larger = smaller
    smaller = remainder


