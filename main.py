from utils.py import factorial
number = int(input())
result = factorial(number)
print(fThe factorial of {number} is {result})

from utils.py import find_gcd

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

gcd = find_gcd(num1, num2)

print(f"НСД({num1}, {num2}) = {gcd}

from utils.py import unique_n
a, b = map(int, input().split())
result = [str(num) for num in range(a, b + 1) if unique_n(num)]

print(*result)
from utils.py import is_prime:
num = int(input("Введіть число: "))
if is_prime(num):
    print(f"{num} є простим числом.")
else:
    print(f"{num} є складним числом.")
