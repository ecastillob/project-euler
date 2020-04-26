"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
    (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


from itertools import permutations


def es_primo(N):
    if N == 2:
        return True
    if N%2 == 0 or N<=1:
        return False
    es = True
    for i in range(3, N, 2):
        if N%i == 0:
            es = False
            break
    return es


primos = set([i for i in range(1000, 9999+1) if es_primo(i)])
#len(primos), type(primos)


incremento = 3330
lista = []
for i in range(1000, 9999+1):
    if i in primos:
        x = i
        y = i+incremento
        z = i+incremento*2
        if y in primos and z in primos:
            a = tuple(str(x))
            b = tuple(str(y))
            c = tuple(str(z))
            p = list(permutations(str(i)))
            if a in p and b in p and c in p:
                lista = []
                print(a)
                print(b)
                print(c)
                print("")
                lista.append(a)
                lista.append(b)
                lista.append(c)
                #break
#lista


s = ""
for item in ["".join(t) for t in lista]:
    s += item
int(s)  # 296962999629
