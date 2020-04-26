"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


lista = []
for b in range(10, 100):
    lb = str(b)
    if "0" in lb:
        continue
    for a in range(10, b):
        la = str(a)
        if "0" in la:
            continue
        es = False
        for c in la:
            if c in lb:
                es = True
                break
        if es:
            index1 = la.find(c)
            index2 = lb.find(c)
            n_str = la[:index1] + la[index1 + 1:]
            d_str = lb[:index2] + lb[index2 + 1:]
            n = int(n_str)
            d = int(d_str)
            if (n != 0 and d != 0 and (n / d < 1)):
                if (a / b == n / d):
                    lista.append((n, d, a, b))
fracciones = [(_[-2], _[-1]) for _ in lista]
fracciones  # [(16, 64), (26, 65), (19, 95), (49, 98)]


n, d = 1, 1
for a, b in fracciones:
    n *= a
    d *= b
n, d  # (387296, 38729600)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


denominador = gcd(n, d)
d // denominador  # 100
