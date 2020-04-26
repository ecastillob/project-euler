"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

import numpy as np


contenido = None
with open('p067_triangle.txt') as archivo:
    contenido = archivo.read()
#contenido


numeros = []
for linea in contenido.splitlines():
    numeros.append([int(j) for j in linea.split(' ')])


largo = len(numeros)
z = np.full((largo, largo), -1)
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        z[i][j] = numeros[i][j]
#z


N = len(z)
for i in range(N-2, -1, -1):
    for j in range(0, i+1):
        if z[i+1][j] > z[i+1][j+1]:
            z[i][j] = z[i][j] + z[i+1][j]
        else:
            z[i][j] = z[i][j] + z[i+1][j+1]
    #print('')
#z


z[0][0]  # 7273
