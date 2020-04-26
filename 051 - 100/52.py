"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


N = 1000000
for i in range(1, N+1):
    a = set(str(i))
    b = set(str(i*2))
    c = set(str(i*3))
    d = set(str(i*4))
    e = set(str(i*5))
    f = set(str(i*6))
    if a == b == c == d == e == f:
        print(i)  # 142857
        break
