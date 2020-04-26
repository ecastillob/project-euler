LIMITE = 100
contador = 0
for a in range(1, LIMITE):
    hay = False
    for b in range(1, LIMITE):
        s = str(a**b)
        if len(s) == b:
            print(a, b, s)
            contador += 1
            hay = True
    if hay:
        print("")
contador  # 49
