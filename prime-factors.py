import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
        
    choice = input("Do you want to calculate GCD or LCM? Enter 'gcd' or 'lcm': ").lower()

    if choice == 'gcd':
        result = gcd(a, b)
        factors = prime_factors(result)
        print(f"The GCD of {a} and {b} is: {result}")
        print("The prime factors of the GCD are:", ", ".join(f"{k}^{v}" for k, v in factors.items()))
    elif choice == 'lcm':
        result = lcm(a, b)
        factors = prime_factors(result)
        print(f"The LCM of {a} and {b} is: {result}")
        print("The prime factors of the LCM are:", ", ".join(f"{k}^{v}" for k, v in factors.items()))
    else:
        print("Invalid choice. Please enter 'gcd' or 'lcm'.")
    
except ValueError:
    print("Please enter valid integer numbers.")