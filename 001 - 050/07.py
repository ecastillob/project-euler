"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def es_primo(numero):
    if (numero <= 1):
        return 0
    if (numero % 2 == 0):
        if (numero == 2):
            return 1
        else:
            return 0
    i, es_numero_primo = None, 1
    extremo_derecho = int(numero / 2) + 1
    for i in range(3, extremo_derecho+1, 2):
        if (numero%i == 0):
            es_numero_primo -= 1
            break
    return es_numero_primo


valor = 2
contador = 0
#N = 6
N = 10001
while True:
    if es_primo(valor):
        contador += 1
    if contador == N:
        break
    valor += 1
contador, valor  # 104743