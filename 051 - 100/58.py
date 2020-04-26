"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

def es_primo_simplificado(N):
    if N % 2 == 0:
        return 0
    es = 1
    for i in range(3, N, 2):
        if N%i == 0:
            es = 0
            break
    return es


def funcion(N):
    inicio = 1
    porcentaje = 100
    n_primos = 0
    for i in range(3, N+1, 2):
        up = i-1
        valores = (
            inicio+up*1,
            inicio+up*2,
            inicio+up*3,
            inicio+up*4,
        )
        n_primos += sum([es_primo_simplificado(k) for k in valores])
        n_en_diagonales = (i*2 - 1)
        porcentaje = n_primos / n_en_diagonales
        if porcentaje < 0.1:
            break
        inicio = i**2
    #n_primos, n_en_diagonales, porcentaje, i
    return i


%%time
funcion(2000)
"""
CPU times: user 24.8 s, sys: 0 ns, total: 24.8 s
Wall time: 24.9 s
"""

%%time
funcion(5000)
"""
CPU times: user 5min 49s, sys: 116 ms, total: 5min 49s
Wall time: 5min 55s
"""


# antes cythonmagic
%load_ext Cython


%%cython --annotate
def cy_es_primo_simplificado_2(n):
    cdef unsigned int i, N, es
    N = n
    if N%2 == 0:
        return 0
    es = 1
    for i in range(3, N, 2):
        if N%i == 0:
            es = 0
            break
    return es
def cy_funcion_3(n):
    cdef unsigned int inicio, N, n_primos, i, up, n_en_diagonales, k
    cdef float porcentaje
    inicio = 1
    porcentaje = 100
    N = n
    n_primos = 0
    valores = (0, 0, 0, 0)
    for i in range(3, N+1, 2):
        up = i-1
        valores = (
            inicio+up*1,
            inicio+up*2,
            inicio+up*3,
            inicio+up*4,
        )
        n_primos += sum((cy_es_primo_simplificado_2(k) for k in valores))
        n_en_diagonales = (i*2 - 1)
        porcentaje = n_primos / n_en_diagonales
        if (i-1) % 1000 == 0:
            print(i, "\t", porcentaje)
        if porcentaje < 0.1:
            print(n_primos, n_en_diagonales, porcentaje, i)
            break
        inicio = i**2
    return i


%%time
cy_funcion_3(2000)
"""
CPU times: user 1.22 s, sys: 3.01 ms, total: 1.22 s
Wall time: 1.29 s
"""


%%time
cy_funcion_3(5000)
"""
CPU times: user 16 s, sys: 26.1 ms, total: 16.1 s
Wall time: 16.4 s
"""


%%time
cy_funcion_3(10000)
"""
CPU times: user 1min 47s, sys: 0 ns, total: 1min 47s
Wall time: 1min 50s
"""


%%time
cy_funcion_3(30000)  # 26241
"""
5248 52481 0.0999980941414833 26241
CPU times: user 29min 58s, sys: 2.56 s, total: 30min 1s
Wall time: 30min 53s
"""
