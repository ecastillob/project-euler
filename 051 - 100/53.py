"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, $^5C_3 = 10$.

In general,
$$
^nC_r = \frac{n!}{r!(n−r)!} \quad , \mathrm{where} \ r ≤ n, n! = n × (n−1) \ × \ ... \ × 3 × 2 × 1, \mathrm{and} \ 0! = 1.
$$

It is not until n = 23, that a value exceeds one-million: $^{23}C_{10} = 1144066.$

How many, not necessarily distinct, values of $^nC_r$, for $1 ≤ n ≤ 100$, are greater than one-million?
"""


def calcular_factorial(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial


def combinatoria(n, r):
    n_f = calcular_factorial(n)
    r_f = calcular_factorial(r)
    return n_f / (r_f * calcular_factorial(n - r))



contador = 0
for n in range(1, 100+1):
    for r in range(1, n):
        if combinatoria(n, r) > 1000000:
            contador += 1
contador  # 4075
