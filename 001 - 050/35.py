#!/usr/bin/env python
# coding: utf-8

# # Python

# In[1]:


import sys


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


def rotar(N):
    S = str(N)
    return tuple(
        int(S[index:] + S[0:index]) 
        for index in range(len(S)) 
    )


# In[4]:


def funcion1(N, mostrar=False):
    primos = (2,) + tuple(i for i in range(3, N+1, 2) if es_primo_simple(i))
    if mostrar:
        print("n_primos: ", len(primos))
        print("size of : ", sys.getsizeof(primos))
    s = set(primos)
    s2 = set()
    for p in primos:
        es = True
        rotados = rotar(p)
        for _ in rotados:
            if _ not in s:
                es = False
                break
        if es:
            s2.add(p)
    total = len(s2)
    return total


# In[5]:


get_ipython().run_cell_magic('time', '', 'funcion1(100, True)')


# In[6]:


get_ipython().run_cell_magic('time', '', 'funcion1(1_000, True)')


# In[7]:


get_ipython().run_cell_magic('time', '', 'funcion1(10_000, True)')


# In[8]:


get_ipython().run_cell_magic('time', '', 'funcion1(100_000)')


# # cython

# In[9]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[10]:


get_ipython().run_cell_magic('cython', '--compile-args=-O3 --force', '\nfrom libc.math cimport sqrt\nfrom array import array\nfrom cpython cimport array as c_array\ncimport cython\n\n\n@cython.boundscheck(False) \n@cython.wraparound(False)\ncdef cy_es_primo_simple(unsigned int N):\n    cdef unsigned int extremo, i\n    es = True\n    extremo = (N // 2)+1\n    for i in range(3, extremo, 2):\n        if N % i == 0:\n            es = False\n            break\n    return es\n\n\n@cython.boundscheck(False) \n@cython.wraparound(False)\ndef rotar(N):\n    S = str(N)\n    return tuple(\n        int(S[index:] + S[0:index]) \n        for index in range(len(S)) \n    )\n\n\n@cython.boundscheck(False) \n@cython.wraparound(False)\ncdef unsigned int cy_funcion1(unsigned int N):\n    cdef unsigned int i, p, v, total\n    primos = (2,) + tuple(i for i in range(3, N+1, 2) if cy_es_primo_simple(i))\n    s = set(primos)\n    s2 = set()\n    for p in primos:\n        es = True\n        rotados = rotar(p)\n        for v in rotados:\n            if v not in s:\n                es = False\n                break\n        if es:\n            s2.add(p)\n    total = len(s2)\n    return total\n\n\ndef funcion1(N):\n    return cy_funcion1(N)')


# In[11]:


get_ipython().run_cell_magic('time', '', 'funcion1(100)')


# In[12]:


get_ipython().run_cell_magic('time', '', 'funcion1(10_000)')


# In[13]:


get_ipython().run_cell_magic('time', '', 'funcion1(100_000)')


# In[14]:


get_ipython().run_cell_magic('time', '', 'funcion1(2*100_000)')


# In[15]:


get_ipython().run_cell_magic('time', '', 'funcion1(5*100_000)')


# In[16]:


get_ipython().run_cell_magic('time', '', 'funcion1(10*100_000)')


# In[ ]:




