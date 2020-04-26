"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
%%time
N = 10**7
largo = 2
numeros = set(str(12))
mayor = 0
for i in range(11, N+1, 2):
    s = str(i)
    largo_actual = len(s)
    if largo < largo_actual:
        largo = largo_actual
        numeros = set([str(i) for i in range(1,largo+1)])
    if set(str(i)) == numeros and es_primo_simplificado(i):
        mayor = i
mayor  # 7652413