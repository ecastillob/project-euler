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
