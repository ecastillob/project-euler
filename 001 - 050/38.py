"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


N = 10000
mayor = 0
numeros = set([str(w) for w in range(1, 10)])
for a in range(1, N+1):
    s = ""
    for b in range(1, 10):
        c = a*b
        s += str(c)
        if len(s) == 9 and set(s) == numeros:
            print(a, "\t", b, "\t", int(s))
            if mayor < int(s):
                mayor = int(s)
            break
mayor  # 932718654
