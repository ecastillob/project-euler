
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be ``1 + 2 + 4 + 7 + 14 = 28``, which means that 28 is a perfect number.
# 
# A number n is called 
# * deficient if the sum of its proper divisors is less than n 
# * abundant if this sum exceeds n.
# 
# As ``12`` is the smallest abundant number, ``1 + 2 + 3 + 4 + 6 = 16``, the smallest number that can be written as the sum of two abundant numbers is ``24``. 
# 
# By mathematical analysis, it can be shown that *all integers greater than* **28123** can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# In[1]:


import numpy as np


# In[2]:


def funcion(N):
    """
    deficient < 0
    abundant > 0
    """
    suma = 0
    for i in range(1, int(N/2)+1):
        if N%i == 0:
            suma += i
    return suma - N


# In[3]:


LIMITE = 28123+1
numeros = np.array([i for i in range(1, LIMITE) if funcion(i) > 0])
sumas = set()
for i in numeros:
    for k in numeros:
        sumas.add(i+k)
suma = 0
for numero in range(1, LIMITE):
    if not (numero in sumas):
        suma += numero
suma  # 4179871
