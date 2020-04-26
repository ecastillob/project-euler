"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


# In[1]:


def factorial(N):
    total = 1
    for i in range(1, N+1):
        total *= i
    return total


# In[2]:


def suma_digitos(N):
    numero_str = str(N)
    total = 0
    for digito in numero_str:
        total += int(digito)
    return total


# In[3]:


suma_digitos( factorial(100) )  # 648
