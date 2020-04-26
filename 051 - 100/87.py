"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

$$ 28 = 2^2 + 2^3 + 2^4 $$
$$ 33 = 3^2 + 2^3 + 2^4 $$
$$ 49 = 5^2 + 2^3 + 2^4 $$
$$ 47 = 2^2 + 3^3 + 2^4 $$

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""


def es_primo_impar(N):
    es = True
    extremo = N//2 + 1
    for i in range(3, extremo, 2):
        if N%i == 0:
            es = False
            break
    return es


def funcion(LIMITE):
    limite = LIMITE
    a_l = 1
    while a_l**2 + 2**3 + 2**4 <= limite:
        a_l += 1
    a_l
    primos = tuple([2] + [i for i in range(3, a_l+1, 2) if es_primo_impar(i)])
    suma = 0
    numeros = set()
    for a in primos:
        for b in primos:
            for c in primos:
                suma = (a**2) + (b**3) + (c**4)
                if suma < limite:
                    numeros.add(suma)
    return len(numeros)


%%time
funcion(5*(10**6))
"""
CPU times: user 37.3 s, sys: 16.1 ms, total: 37.3 s
Wall time: 37.4 s
"""


%load_ext Cython


%%cython
def cy_es_primo_impar(n):
    cdef unsigned int extremo, N, i
    N = n
    es = True
    extremo = N//2 + 1
    for i in range(3, extremo, 2):
        if N%i == 0:
            es = False
            break
    return es
def cy_funcion(LIMITE):
    cdef unsigned int limite, a_l, a,b,c
    cdef unsigned long long suma
    limite = LIMITE
    a_l = 1
    while a_l**2 + 2**3 + 2**4 <= limite:
        a_l += 1
    primos = tuple([2] + [i for i in range(3, a_l+1, 2) if cy_es_primo_impar(i)])
    suma = 0
    numeros = set()
    for a in primos:
        for b in primos:
            for c in primos:
                suma = (a**2) + (b**3) + (c**4)
                if suma < limite:
                    numeros.add(suma)
    return len(numeros)


%%time
cy_funcion(5*(10**6))
"""
CPU times: user 150 ms, sys: 11.8 ms, total: 162 ms
Wall time: 187 ms
"""


%%time
cy_funcion(5*(10**7))  # 1097343
"""
CPU times: user 2.88 s, sys: 273 ms, total: 3.16 s
Wall time: 3.24 s
"""
