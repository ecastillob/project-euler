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
