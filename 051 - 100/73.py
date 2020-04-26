"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""


def funcion_v3(LIMITE):
    d = LIMITE
    n_fracciones = 0
    s = set()
    for d in range(1, d+1):
        for n in range(1, d):
            n_fracciones += 1
            fraccion = (1.0 * n / d)
            if 1/3 < fraccion < 1/2:
                s.add(fraccion)
    return len(s), n_fracciones


%%time
funcion_v3(12000)  # 7295372
"""
CPU times: user 18.3 s, sys: 2.15 s, total: 20.5 s
Wall time: 21.3 s
(7295372, 71994000)
"""