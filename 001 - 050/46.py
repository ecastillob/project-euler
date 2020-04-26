#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""


# In[2]:


def es_primo_simple(N):
    es = True
    extremo = (N // 2)+1
    for i in range(3, extremo, 2):
        if N % i == 0:
            es = False
            break
    return es


# In[3]:


N = 10000
primos = (2,) + tuple(i for i in range(3, N+1, 2) if es_primo_simple(i))
s = set(primos)
len(primos), primos[:10]


# In[4]:


contador = 0
resultado = -1
for i in range(3, N, 2):
    if i in s:
        continue
    es = False
    print(i, end="\t")
    valor = 0
    for p in primos:
        for b in range(1, p):
            valor = p + 2*(b**2)
            if valor >= i:
                break
        if valor == i:
            es = True
            contador += 1
            #print(i, "\t", f"{p} + 2x({b}**2)")
            break
    if not es:
        print("\n----")
        resultado = i
        break
resultado  # 5777
