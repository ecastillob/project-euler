#!/usr/bin/env python
# coding: utf-8

# # Problem [104](https://projecteuler.net/problem=104): Pandigital Fibonacci ends

# The Fibonacci sequence is defined by the recurrence relation:
# 
# $$ F_n = F_{n−1} + F_{n−2}, \mathrm{where} \ F_1 = 1 \ \mathrm{and} \ F_2 = 1. $$
# 
# It turns out that $F_{541}$, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And $F_{2749}$, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
# 
# Given that $F_k$ is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find $k$.

# In[1]:


s = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
s


# In[ ]:


%%time
a = 0
b = 1
k = 1
inicio, final = "", ""
while not (s.issubset(inicio) and s.issubset(final)):
    print(k, end="\t")
    b = b + a
    a = b - a
    valor = str(a)
    inicio, final = valor[:9], valor[-9:]
    k += 1
print("")
"""
329468
CPU times: user 2h 25min 32s, sys: 44.6 s, total: 2h 26min 17s
Wall time: 2h 29min 54s
""
