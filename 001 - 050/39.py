"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


from math import sqrt


def f_1():
    maximo, LIMITE, p, p_max, a, b, c = 0, 0, 0, 0, 0, 0, 0
    c_aux = 0.0
    maximo = 0
    p_max = 0
    LIMITE = 1000
    for p in range(3, LIMITE+1):
        lista = []
        for a in range(1, p-2+1):
            for b in range(1, p-2+1):
                c_aux = sqrt(a**2 + b**2)
                if a+b+c_aux == p:
                    c = int(c_aux)
                    s = set([a, b, c])
                    if s not in lista:
                        #print(a, b, c)
                        lista.append(s)
        if maximo < len(lista):
            maximo = len(lista)
            p_max = p
    return (p_max, maximo)


%%time
f_1()
"""
CPU times: user 4min 51s, sys: 32.8 ms, total: 4min 51s
Wall time: 4min 54s
(840, 8)
"""


# antes cythonmagic
%load_ext Cython


%%cython --annotate
from math import sqrt
def f_2():
    cdef unsigned int maximo, LIMITE, p, p_max, a, b, c
    cdef float c_aux
    #cdef unsigned long n, suma, resta, pj, pk
    maximo = 0
    p_max = 0
    LIMITE = 1000
    for p in range(3, LIMITE+1):
        lista = []
        for a in range(1, p-2+1):
            for b in range(1, p-2+1):
                c_aux = sqrt(a**2 + b**2)
                if a+b+c_aux == p:
                    c = int(c_aux)
                    s = set([a, b, c])
                    if s not in lista:
                        #print(a, b, c)
                        lista.append(s)
        if maximo < len(lista):
            maximo = len(lista)
            p_max = p
    return (p_max, maximo)


%%time
f_2()
"""
CPU times: user 21 s, sys: 37 ms, total: 21.1 s
Wall time: 21.9 s
(840, 8)
"""
