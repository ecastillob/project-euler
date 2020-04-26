#!/usr/bin/env python
# coding: utf-8
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 
    6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, 
and the sum of these palindromes is 4164. 
Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
# In[1]:


from math import sqrt


# # 1

# In[2]:


def funcion(limite):
    contador = 0
    palindromos_validos = []
    for valor in range(2, limite):
        suma = 0
        valor_str = str(valor)
        if valor_str == valor_str[::-1]:
            raiz = int(sqrt(valor))
            for i in range(1, raiz):
                suma = 0
                base = i
                while suma <= valor:
                    suma_valida = suma
                    suma += (base*base)
                    base += 1
                if suma_valida == valor:
                    palindromos_validos.append(valor)
                    break
    return sum(palindromos_validos)


# In[3]:


get_ipython().run_cell_magic('time', '', 'funcion(10**3)')


# In[4]:


get_ipython().run_cell_magic('time', '', 'funcion(10**7)')


# # Cython

# ## 1

# In[5]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[6]:


get_ipython().run_cell_magic('cython', '--compile-args=-O3 --force', '\nfrom libc.math cimport sqrt\ncimport cython\n\n\n@cython.boundscheck(False)  # Deactivate bounds checking\n@cython.wraparound(False)   # Deactivate negative indexing.\ndef cy_funcion(LIMITE):\n    # NO es: 166\n    cdef unsigned int limite, contador, valor, suma, raiz, i, base, suma_valida\n    limite = LIMITE\n    contador = 0\n    palindromos_validos = []\n    for valor in range(2, limite):\n        valor_str = str(valor)\n        if valor_str == valor_str[::-1]:\n            raiz = int(sqrt(valor))\n            for i in range(1, raiz):\n                suma = 0\n                base = i\n                while suma <= valor:\n                    suma_valida = suma\n                    suma += (base*base)\n                    base += 1\n                if suma_valida == valor:\n                    palindromos_validos.append(valor)\n                    break\n    return sum(palindromos_validos)')


# In[7]:


get_ipython().run_cell_magic('time', '', 'cy_funcion(10**3)  # 4164')


# In[8]:


get_ipython().run_cell_magic('time', '', 'cy_funcion(10**7)')


# In[9]:


get_ipython().run_cell_magic('time', '', 'cy_funcion(10**8)  # 2906969179')


# In[ ]:




