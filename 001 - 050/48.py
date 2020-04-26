"""
The series, $1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317.$

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + ... + 1000^{1000}.$
"""


N = 1000
suma = sum([pow(i, i) for i in range(1, N+1)])
int(str(suma)[-10:])   # 9110846700
