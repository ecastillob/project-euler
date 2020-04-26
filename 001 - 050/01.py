
"""
>>> f1(10)
23
>>> f1(1000)
233168
"""
def f1(N=1000):
    suma = 0
    for i in range(1, N):
        if (i % 3 == 0) or (i % 5== 0):
            suma += i
    return suma


"""
>>> f2(4000000)
4613732
"""
def f2(N=10):
    contador, suma = 0, 0
    a, b, c = 1, 0, 1
    numeros = []
    while (c <= N):
        a = b
        b = c
        #numeros.append(c)
        if (c%2 == 0):
            suma += c
        c = a+b
        contador += 1
    return (numeros[1:], suma)
