"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion $(10^9)$?
"""


# antes cythonmagic
%load_ext Cython


%%cython --annotate
def cy_es_solo_impar_2(N):
    #cdef int es
    #cdef char c
    s = str(N)
    es = True
    for c in s:
        if int(c) % 2 == 0:
            es = False
            break
    return es
def cy_contar_numeros_2(n): 
    cdef unsigned int N, i, a, c, decena
    cdef int contador
    N = int(n)
    contador = 0
    decena = N // 10
    for i in range(1, N):
        a = i
        b = str(i)[::-1]
        if b[0] != '0':
            c = a + int(b)
            if cy_es_solo_impar_2(c):
                contador += 1
        if i % decena == 0:
            print(i)
    return contador


%%time
cy_contar_numeros_2(10**9)  # 608720
"""
CPU times: user 16min 56s, sys: 1.69 s, total: 16min 58s
Wall time: 17min 31s
"""
