a1, b1 = 8, 3
a, b = 11, 4
contador = 4
i = 4
while contador < 100:
    a0, b0 = a, b
    a1, b1 = a0+a1, b0+b1
    a2, b2 = a1*i+a0, b1*i+b0
    a, b = a2+a1, b2+b1
    a0, b0 = a1, b1
    a1, b1 = a2, b2
    print(a0, b0)
    #print(a1, b1)
    print(a2, b2)
    print(a, b)
    contador += 3
    print("contador:", contador, "\n")
    i += 2
a, b, contador


numerador = a
sum(int(c) for c in str(numerador))  # 272
