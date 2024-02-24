from utils.py import factorial
number = int(input())
result = factorial(number)
print(fThe factorial of {number} is {result})

from utils.py import find_gcd

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

gcd = find_gcd(num1, num2)

print(f"НСД({num1}, {num2}) = {gcd}

