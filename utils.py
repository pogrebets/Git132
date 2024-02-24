def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

