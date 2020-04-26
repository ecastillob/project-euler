"""
Euler discovered the remarkable quadratic formula:

$$n2+n+41$$

It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \leq n \leq 39$
. However, when $n=40,40^2+40+41=40(40+1)+41$ is divisible by $41$, and certainly when $n=41,41^2+41+41$

is clearly divisible by $41$.

The incredible formula $n2−79n+1601$
was discovered, which produces 80 primes for the consecutive values $0 \leq n \leq 79$. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

$$n^2+an+b$$

, where $|a| < 1000$ and $|b| \leq 1000$

where $|n|$
is the modulus/absolute value of $n$
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, $a$
and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n=0$.
"""


def f3(n, a, b):
    return (n**2) + (a*n) + b


def es_primo(n):
    if n <= 1:
        return False
    es = True
    extremo = int(n/2)+1
    for i in range(2, extremo):
        if n%i == 0:
            es = False
            break
    return es


maximo = 0
izquierdo = 0
derecho = 0
A = 1000-1
B = 1000
for a in range(-A, A+1):
    for b in range(-B, B+1):
        contador = 0
        for n in range(500):
            valor = f3(n, a, b)
            if es_primo(valor):
                contador += 1
            else:
                break
        if maximo < contador:
            izquierdo = a
            derecho = b
            maximo = contador
print(maximo, izquierdo, derecho)
print (izquierdo * derecho)  # -59231
