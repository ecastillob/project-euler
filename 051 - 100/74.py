"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""


%load_ext Cython


%%cython --compile-args=-O3 --force

cimport cython


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cdef unsigned int calcular_factorial(unsigned int N):
    cdef unsigned int m, i
    m = 1
    for i in range(1, N+1):
        m *= i
    return m


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cdef unsigned int calcular_suma_factoriales_digitos(unsigned int numero):
    cdef unsigned int suma, d, f
    suma = 0
    #print(numero, end="\n\n")
    for c in str(numero):
        d = int(c)
        f = calcular_factorial(d)
        suma += f
        #print(f)
    return suma


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cdef unsigned int contar_loop(unsigned int numero):
    cdef unsigned int contador
    contador = 1
    s = set()
    s.add(numero)
    while True:
        numero = calcular_suma_factoriales_digitos(numero)
        if numero in s:
            break
        s.add(numero)
        contador += 1
    return contador


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
cdef unsigned int cy_funcion_aux(unsigned int LIMITE):
    cdef unsigned int limite, conteo, suma, numero
    limite = LIMITE
    conteo = 0
    suma = 0
    for numero in range(1, limite):
        conteo = contar_loop(numero)
        if conteo == 60:
            suma += 1
    return suma


def cy_funcion(LIMITE):
    cdef unsigned int resultado
    resultado = cy_funcion_aux(LIMITE)
    return resultado



%%time
cy_funcion(10**6)  # 402
