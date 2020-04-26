"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


from decimal import *


getcontext().prec = 2000



mayor = 0
numero_mayor = None
for d in range(2, 1000):
    
    #s = str(1/d)[2:]
    s = str(Decimal(1) / Decimal(d))[2:-2]
    
    #print(s)
    largo = 0
    submayor = 0
    entra = False
    for i in range(1, len(s)):
        a = None
        fue = False
        contador = 0
        for k in range(0, len(s)-i+1, i):
            #print("\t", s[k:k+i])
            if a != s[k:k+i]:
                if not fue:
                    fue = True
                else:
                    break
                a = s[k:k+i]
            else:
                contador += 1
        if contador > 0:
            largo = len(a)
            if submayor < largo:
                submayor = largo
                if entra:
                    break
                entra = True
            if d < 100:
                break
    if mayor < largo:
        mayor = largo
        numero_mayor = d
        print(mayor, numero_mayor)
    
    #print(d, largo, "\t", s)
    #print(d, largo)
mayor, numero_mayor  # 982 (numero digitos), 983 (d)
