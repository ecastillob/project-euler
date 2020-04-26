"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""


%load_ext Cython


%%cython
def cy_chaining_v4(p1, p2):
    cdef unsigned int N, cota, limite, suma, i
    N = p1
    cota = p2
    s = set()
    es_valido = True
    while N not in s:
        s.add(N)
        limite = (N//2)
        suma = 0
        for i in range(1, limite+1):
            if N%i == 0:
                suma += i
        N = suma
        if N > cota:
            es_valido = False
            break
    if N == 0 or N != p1:
        es_valido = False
    return (es_valido, s)
def cy_funcion_v4(a,b, LIMITE):
    cdef unsigned int A, B, M1, menor, mayor, porcentaje, incremento, i, contador, n_numeros, aux, indice
    A = a
    B = b+1
    M1 = LIMITE
    menor = LIMITE
    mayor = 0
    porcentaje = (B-A) // 100
    incremento = 0
    conjunto = None
    for i in range(A, B):
        if i%porcentaje == 0:
            incremento += 1
            print(incremento, end=" ")
        aceptable = True
        contador = 0
        es_valido, s = cy_chaining_v4(i, M1)
        if es_valido:
            n_numeros = len(s)
            if mayor < n_numeros:
                mayor = n_numeros
                menor = min(s)
                indice = i
                conjunto = s
    print("")
    return (indice, mayor, menor, conjunto)


%%time
cy_funcion_v4(10, 50000, 10**6)  # 14316
"""
CPU times: user 54 s, sys: 72.2 ms, total: 54.1 s
Wall time: 54.5 s
"""
