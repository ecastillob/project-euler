"""
The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385$$

The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#N = 10
N = 100

suma_1 = 0
for i in range(1, N+1):
    suma_1 += i**2

suma_2 = 0
for i in range(1, N+1):
    suma_2 += i
suma_2 = suma_2**2
suma_1, suma_2, suma_2 - suma_1  # 25164150