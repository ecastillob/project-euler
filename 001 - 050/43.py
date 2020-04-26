"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


p = (2, 3, 5, 7, 11, 13, 17)
N = 1406357289
s = str(N)
divisible = True
for i in range(1, 7+1):
    n = int(s[i:i+3])
    if not (n % p[i-1] == 0):
        divisible = False
        break
divisible


p = (2, 3, 5, 7, 11, 13, 17)
pandigital = set([str(i) for i in range(10)])
A = 10**9
B = int('9'*10)
suma = 0
avance = 10**8
for N in range(A, B+1):
    if N % avance == 0:
        print(N)
    s = str(N)
    if pandigital == set(s):
        divisible = True
        for i in range(1, 7+1):
            n = int(s[i:i+3])
            if not (n % p[i-1] == 0):
                divisible = False
                break
        if divisible:
            suma += N
            print("\t", N)
suma  # 16695334890


"""
	1000000000
	1100000000
	1200000000
	1300000000
	1400000000
		 1406357289
		 1430952867
		 1460357289
	1500000000
	1600000000
	1700000000
	1800000000
	1900000000
	2000000000
	2100000000
	2200000000
	2300000000
	2400000000
	2500000000
	2600000000
	2700000000
	2800000000
	2900000000
	3000000000
	3100000000
	3200000000
	3300000000
	3400000000
	3500000000
	3600000000
	3700000000
	3800000000
	3900000000
	4000000000
	4100000000
		 4106357289
		 4130952867
		 4160357289
	4200000000
	4300000000
	4400000000
	4500000000
	4600000000
	4700000000
	4800000000
	4900000000
	5000000000
	5100000000
	5200000000
	5300000000
	5400000000
	5500000000
	5600000000
	5700000000
	5800000000
	5900000000
	6000000000
	6100000000
	6200000000
	6300000000
	6400000000
	6500000000
	6600000000
	6700000000
	6800000000
	6900000000
	7000000000
	7100000000
	7200000000
	7300000000
	7400000000
	7500000000
	7600000000
	7700000000
	7800000000
	7900000000
	8000000000
	8100000000
	8200000000
	8300000000
	8400000000
	8500000000
	8600000000
	8700000000
	8800000000
	8900000000
	9000000000
	9100000000
	9200000000
	9300000000
	9400000000
	9500000000
	9600000000
	9700000000
	9800000000
	9900000000
"""
