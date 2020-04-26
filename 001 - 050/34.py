"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def calcular_factorial(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial



def es_un_numero_curioso(N):
    suma = 0
    for valor_str in str(N):
        suma += factoriales[int(valor_str)]
    return N == suma



factoriales = [calcular_factorial(i) for i in range(10)]



%%time
N = 10**8; a = [i for i in range(3, N) if es_un_numero_curioso(i)]; print(sum(a))
"""
40730
CPU times: user 5min 49s, sys: 564 ms, total: 5min 50s
Wall time: 5min 56s
"""
