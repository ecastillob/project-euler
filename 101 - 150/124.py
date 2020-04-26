#!/usr/bin/env python
# coding: utf-8

# # Problem 124: Ordered radicals

# The radical of $n$, $rad(n)$, is the product of the distinct prime factors of $n$. For example, 504 = 23 × 32 × 7, so $rad(504)$ = 2 × 3 × 7 = 42.
#
# If we calculate $rad(n)$ for $1 ≤ n ≤ 10$, then sort them on $rad(n)$, and sorting on $n$ if the radical values are equal, we get:
"""
    Unsorted 	 Sorted

n 	 rad(n) 	 n 	 rad(n)  k
1 	 1 			 1 	 1 	 	 1
2 	 2 			 2 	 2 	 	 2
3 	 3 	  	  	 4 	 2 	  	 3
4 	 2 	  	  	 8 	 2 	  	 4
5 	 5 	  	  	 3 	 3 	  	 5
6 	 6 	  	  	 9 	 3 	  	 6
7 	 7 	 	 	 5 	 5 	  	 7
8 	 2 	  	  	 6 	 6 	  	 8
9 	 3 	  	 	 7 	 7 	  	 9
10 	 10 	  	 10 10 	  	 10
"""
# Let $E(k)$ be the kth element in the sorted $n$ column; for example, $E(4) = 8$ and $E(6) = 9$.
#
# If $rad(n)$ is sorted for $1 ≤ n ≤$ 100000, find $E(10000)$.

# In[1]:


def rad(N):
    d = 2
    s = set()
    while N > 1:
        if N % d == 0:
            N //= d
            s.add(d)
        else:
            d += 1
    total = 1
    for v in s:
        total *= v
    return total


# In[2]:


rad(504)  # 42


# In[ ]:


%%time
N = 100_000
valores = [(i, rad(i)) for i in range(1, N+1)]
mifu = lambda x: x[1]
ordenados = sorted(valores, key=mifu)
print(ordenados[10000 - 1])  # 21417
"""
(21417, 1947)
CPU times: user 1min 38s, sys: 888 ms, total: 1min 39s
Wall time: 1min 40s
"""
