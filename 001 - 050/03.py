"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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


factores = []
#N = 30  
#N = 13195
N = 600851475143
valor = int(N)
while (valor > 1):
    print (valor)
    for i in range(2, valor+1):
        if es_primo(i) and valor % i == 0:
            valor = int(valor / i)
            factores.append(i)
            break
factores[-1]  # 6857