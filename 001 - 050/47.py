"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


def factores_primos(n):
    i = 2
    lista = []
    while n > 1:
        n = int(n)
        for d in range(i, n+1):
            if n%d == 0:
                i = d
                break
        lista.append(i)
        n /= i
    return set(lista)



def funcion():
    N = 100000
    f = tuple([factores_primos(i) for i in range(N+1)])
    for i in range(2, N-4):
        a = f[i]
        b = f[i+1]
        c = f[i+2]
        d = f[i+3]
        if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
            print(i, a)
            print(i+1, b)
            print(i+2, c)
            print(i+3, d)
            print("")
            break
    return i


%%time
funcion()  # 134043
"""
CPU times: user 3min 59s, sys: 3.08 s, total: 4min 2s
Wall time: 4min 6s
"""


# antes cythonmagic
%load_ext Cython


%%cython --annotate


def cy_factores_primos(N):
    cdef unsigned int i, n, d
    n = N
    i = 2
    lista = []
    while n > 1:
        n = int(n)
        for d in range(i, n+1):
            if n%d == 0:
                i = d
                break
        lista.append(i)
        n /= i
    return set(lista)


def funcion_1(n):
    cdef unsigned int N, i
    i = 0
    N = n
    f = tuple([cy_factores_primos(i) for i in range(N+1)])
    for i in range(2, N-4):
        a = f[i]
        b = f[i+1]
        c = f[i+2]
        d = f[i+3]
        if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
            print(i, a)
            print(i+1, b)
            print(i+2, c)
            print(i+3, d)
            print("")
            break
    return i



%%time
funcion_1(200000)  # 134043
"""
CPU times: user 10.5 s, sys: 275 ms, total: 10.8 s
Wall time: 10.8 s
"""
