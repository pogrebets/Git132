def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def unique_n(num):
    num_str = str(num)
    unique = []
    for i in num_str:
        if i not in unique:
            unique.append(i)
    return len(unique) == 4
