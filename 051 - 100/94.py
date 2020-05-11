#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt


# In[2]:


a, b = 5, 6
area = b * sqrt(a**2 - (b**2 / 4)) / 2
area, int(area), area == int(area)


# In[3]:


def calcular_area(b):
    return b * sqrt(a**2 - (b**2 / 4)) / 2


# In[4]:


suma = 0
for a in range(2, 100_000):
    b1 = a-1
    b2 = a+1
    area1 = calcular_area(b1)
    area2 = calcular_area(b2)
    #print(a, '\t', area1, area2)
    if area1 == int(area1):
        P1 = 2*a + b1
        print(a, '\t', b1, '\t\t', area1, '\t', P1)
        suma += P1
    if area2 == int(area2):
        P2 = 2*a + b2
        print(a, '\t', b2, '\t\t', area2, '\t', P2)
        suma += P2
suma

Secuencia: https://oeis.org/A195531
Fórmula: a(n) = 3*a(n-1)+3*a(n-2)-a(n-3)
# In[5]:


a = [5, 17, 65, 241, 901]
n = len(a)
3*a[n-1] + 3*a[n-2] - a[n-3]


# In[6]:


a = [5, 17, 65, 241, 901]
base = len(a)
for n in range(base, 20):
    a.append(3*a[n-1] + 3*a[n-2] - a[n-3])
lista = a
lista


# In[7]:


suma = 0
LIMITE = 1_000_000_000
for a in lista:
    b1 = a-1
    b2 = a+1
    area1 = calcular_area(b1)
    area2 = calcular_area(b2)
    #print(a, '\t', area1, area2)
    if area1 == int(area1):
        P1 = 2*a + b1
        if P1 > LIMITE:
            break
        print(a, '\t', b1, '\t\t', area1, '\t', P1)
        suma += P1
    if area2 == int(area2):
        P2 = 2*a + b2
        if P2 > LIMITE:
            break
        print(a, '\t', b2, '\t\t', area2, '\t', P2)
        suma += P2
suma


# In[8]:


suma = 0
LIMITE = 1_000_000_000
for a in lista:
    b1 = a-1
    b2 = a+1
    area1 = calcular_area(b1)
    area2 = calcular_area(b2)
    #print(a, '\t', area1, area2)
    if area1 == int(area1):
        P1 = 2*a + b1
        if P1 < LIMITE:
            print(a, '\t', b1, '\t\t', area1, '\t', P1)
            suma += P1
    if area2 == int(area2):
        P2 = 2*a + b2
        if P2 < LIMITE:
            print(a, '\t', b2, '\t\t', area2, '\t', P2)
            suma += P2
suma


# In[9]:


897909598 - 379501250


# In[10]:


897909598 - 379501252

RESPUESTA: 518408346
# In[ ]:




