"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


# antes cythonmagic
%load_ext Cython


%%cython --annotate


def cy_es_primo_simplificado(n):
    """
    asume que N es entero, impar, mayor que 2
    """
    cdef unsigned int i, N
    N = n
    es = True
    for i in range(3, N, 2):
        if N%i == 0:
            es = False
            break
    return es


def cy_generar_primos(n):
    cdef unsigned int i, N
    N = n
    primos = [2] + [i for i in range(3, N+1, 2) if cy_es_primo_simplificado(i)]
    return tuple(primos)


def cy_main(n):
    cdef unsigned int N, i, j, p, mayor, suma, contador
    N = n
    mayor = 0
    primos_t = cy_generar_primos(N)
    for p in primos_t:
        N = p
        j = 0
        while primos_t[j] < N:
            i = j
            suma = 0
            contador = 0
            while suma < N:
                suma += primos_t[i]
                i += 1
                contador += 1
            if suma == N:
                if mayor < contador:
                    print(N, j, contador)
                    mayor = contador
            j += 1
    return mayor


%%time
cy_main(100000)  # primo = 92951, mayor = 183
"""
CPU times: user 16.9 s, sys: 0 ns, total: 16.9 s
Wall time: 17.5 s
"""


%%time
cy_main(1000000)  # primo = 997651, mayor = 543
"""
CPU times: user 24min 35s, sys: 3.31 s, total: 24min 38s
Wall time: 25min 36s
"""
