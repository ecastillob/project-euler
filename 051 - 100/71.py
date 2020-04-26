"""
Consider the fraction, $n$/$d$, where $n$ and $d$ are positive integers. If $n<d$ and HCF($n$,$d$)=$1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d ≤ 8$ in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, **2/5**, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for $d ≤ 1,000,000$ in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""


%%cython --compile-args=-O3 --force

cimport cython


def cy_funcion_v3(LIMITE):
    cdef unsigned int limite, inf, mayor, n_mayor, d_mayor, A, d, n
    limite = LIMITE
    inf = 1
    mayor = 0
    n_mayor = 0
    d_mayor = 0
    fraccion_mayor = 0
    A = 0
    #for d in range(limite, (limite-5), -1):
    for d in range(inf, limite+1):
        if d%10000 == 0:
            print(d, end=" ")
        #print(d, end="\t")
        A = d*2//7
        for n in range(A, d):
            fraccion = (1.0 * n / d)
            if fraccion < 3.0/7:
                if fraccion_mayor < fraccion:
                    fraccion_mayor = fraccion
                    n_mayor = n
                    d_mayor = d
            else:
                break
        #print(n_mayor, d_mayor, fraccion_mayor)
    print("")
    return (n_mayor, d_mayor, fraccion_mayor)



%%time
cy_funcion_v3(1000000)  # 428570
"""
CPU times: user 2min 20s, sys: 250 ms, total: 2min 20s
Wall time: 2min 26s
(428570, 999997, 0.42857128571385716)
"""