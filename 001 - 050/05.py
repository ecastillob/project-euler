"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#N = 2520
numero = 0
while True:
    numero += 1
    contador = 0
    for i in range(1, 20+1):
        if numero % i != 0:
            contador += 1
            break
    if contador == 0:
        break
numero  # 232792560