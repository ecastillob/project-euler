"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


"""
73 74 75 76 77 78 79 80 81
72 43 44 45 46 47 48 49 50
71 42 21 22 23 24 25 26 51
70 41 20  7  8  9 10 27 52
69 40 19  6  1  2 11 28 53
68 39 18  5  4  3 12 29 54
67 38 17 16 14 14 13 30 55
66 37 36 35 34 33 32 31 56
65 64 63 62 61 60 59 58 57
"""
inicio = 1
suma, suma_acumulada = 0, 0
N = 1001
for i in range(3, N+1, 2):
    up = i-1
    valores = [
        inicio+up*1,
        inicio+up*2,
        inicio+up*3,
        inicio+up*4,
        ]
    suma = sum(valores)
    suma_acumulada += suma
    print(inicio, up, "\t", suma, valores)
    inicio = i**2
suma_acumulada += 1
print(suma_acumulada)  # 669171001
