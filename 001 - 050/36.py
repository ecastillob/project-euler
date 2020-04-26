"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def es_palindromo(N):
    N_str = str(N)
    return N_str == N_str[::-1]


def es_palindromo_binario(N):
    a = []
    while N > 0:
        valor = N%2
        a.append(valor)
        N = int(N/2)
    return a == a[::-1]


LIMITE = 10**6
suma = 0
for i in range(1, LIMITE):
    if es_palindromo(i) and es_palindromo_binario(i):
        suma += i
suma  # 872187
