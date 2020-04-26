"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def es_palindromo(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]


mayor = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if es_palindromo(i*j) and i*j > mayor:
            mayor = i*j
mayor  # 906609