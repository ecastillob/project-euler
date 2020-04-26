"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import datetime as dt


def es_primo(N):
    if N<= 1:
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    es = True
    for i in range(3, N, 2):
        if N%i == 0:
            es = False
            break
    return es


inicio = dt.datetime.now()
LIMITE = 10**6
suma = 0
for N in range(10, LIMITE+1):
    lista = list(str(N))
    largo = len(lista)
    son_primos = True
    for i in range(largo):
        valor_1 = int("".join(lista[i:]))
        valor_2 = int("".join(lista[:largo-i]))
        if not (es_primo(valor_1) and es_primo(valor_2)):
            son_primos = False
            break
    if son_primos:
        print("\t", N)
        suma += N
    if N%10000==0:
        print(N)
fin = dt.datetime.now()
tiempo_total = fin - inicio
print("tiempo total: ", tiempo_total)  # tiempo total:  0:51:20.473896
suma #print("suma: ", suma)  # 748317
