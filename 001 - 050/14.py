"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


maximo = 0
inicial = 0
for i in range(1, 1000000+1):
    n = i
    #print(n)
    contador = 1
    while not (n == 1):
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        #print(n)
        contador += 1
    if maximo < contador:
        maximo = contador
        inicial = i
print (inicial)  # 837799
