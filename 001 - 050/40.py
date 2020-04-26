"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12$^{th}$ digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

$$d_1 × d_{10} × d_{100} × d_{1000} × d_{10000} × d_{100000} × d_{1000000}$$
"""


N = 10**6
i = 0
d = ''
while len(d) <= N:
    d += str(i)
    i += 1
total = 1
for indice in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    total *= int(d[indice])
total  # 210
