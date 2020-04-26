"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""


contenido = None
with open("p099_base_exp.txt") as archivo:
    contenido = archivo.read()


numeros = []
for linea in contenido.splitlines():
    base, exp = linea.split(",")
    numeros.append( tuple([int(base), int(exp)]) )
numeros = tuple(numeros)
largo = len(numeros)
largo


%%time
print("Procesando ", largo, "numeros ...")
linea_mayor = 0
mayor = 0
i = 1
for base, exp in numeros:
    print(i, end=" ")
    valor = pow(base, exp)
    if mayor < valor:
        mayor = valor
        linea_mayor = i
    i+=1
print("linea_mayor:", linea_mayor)  # 709
print("Fin.")
"""
Procesando  1000 numeros ...
linea_mayor: 709
Fin.
CPU times: user 32min 45s, sys: 13.2 s, total: 32min 59s
Wall time: 34min
"""
