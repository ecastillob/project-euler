"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

$$1634 = 1^4 + 6^4 + 3^4 + 44$$
$$8208 = 8^4 + 2^4 + 0^4 + 84$$
$$9474 = 9^4 + 4^4 + 7^4 + 44$$

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def numero_str(x, y):
    n_str = str(x)
    largo = len(n_str)
    if largo < y:
        n_str = "0"*(y-largo) + n_str
    return n_str


suma_acumulada = 0
termino = 9999999
y = 5
for i in range(2, termino+1):
    n_str = numero_str(i, y)
    suma = 0
    for c in n_str:
        suma += (int(c)**y)
    if i == suma:
        #print(i)
        suma_acumulada += suma
print(suma_acumulada)  # 443839
