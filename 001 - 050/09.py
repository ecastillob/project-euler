"""
A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
$$a^2 + b^2 = c^2$$

For example, $$3^2 + 4^2 = 9 + 16 = 25 = 5^2.$$

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.
Find the product $abc$.
"""


from math import sqrt


a, b, c = 0, 0, 0
terminar = False
for i in range(1, 1000):
    for j in range(1, 1000):
        a = i
        b = j
        c = sqrt(a**2 + b**2)
        if a+b+c == 1000:
            terminar = True
            break
    if terminar:
        break
a*b*c  # 31875000