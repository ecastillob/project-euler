"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


# In[1]:


def suma_divisores(N):
    suma = 0
    for i in range(1, int(N/2)+1):
        if N%i==0:
            suma += i
    return suma


# In[2]:


amigables = set()
for i in range(1, 10000+1):
    a = suma_divisores(i)
    b = suma_divisores(a)
    c = suma_divisores(b)
    if a == c and a != b:
        amigables.add(a)
        amigables.add(b)
sum(amigables)  # 31626
