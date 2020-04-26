"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""


from decimal import Decimal, getcontext
from math import trunc, sqrt


getcontext().prec = 105
cuadrados = [i*i for i in range(1, 10+1)]
numeros = [i for i in range(1, 100+1) if i not in cuadrados]
print(numeros, end="\n\n")
sumatoria = 0
acumulados = []
for valor in numeros:
    d = Decimal(valor).sqrt()
    d_str = str(d)
    begin_index = d_str.index('.')
    parte_decimal = d_str[begin_index+1:begin_index+100]
    suma = sum([int(c) for c in parte_decimal]) + trunc(d)
    sumatoria += suma
    acumulados.append(suma)
    print(valor, '\t', len(parte_decimal), suma, '\t', len(str(trunc(d))), trunc(d))
sumatoria  # 40886