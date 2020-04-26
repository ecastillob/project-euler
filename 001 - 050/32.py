"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


def pandigital(N):
    productos = set()
    numeros = set([str(w) for w in range(1, 10)])
    for a in range(1, N+1):
        for b in range(1, N+1):
            c = a*b
            x, y, z = str(a), str(b), str(c)
            suma = len(x)+len(y)+len(z)
            if suma > 9:
                break
            s = set()
            for i in x:
                s.add(i)
            for i in y:
                s.add(i)
            for i in z:
                s.add(i)
            if s == numeros:
                productos.add(c)
    return sum(productos)



pandigital(10000)  # 45228
