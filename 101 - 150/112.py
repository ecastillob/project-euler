#!/usr/bin/env python
# coding: utf-8

"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
    for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred,
    but just over half of the numbers below one-thousand (525) are bouncy.
    In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common
    and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""


# In[1]:


def arriba(N):
    valor = -1
    actual = -1
    for n_str in str(N):
        actual = int(n_str)
        if actual < valor:
            return False
        valor = actual
    return True


# In[2]:


def abajo(N):
    valor = 10
    actual = 10
    for n_str in str(N):
        actual = int(n_str)
        if actual > valor:
            return False
        valor = actual
    return True


# In[3]:


def es_bouncy(N):
    return not (arriba(N) or abajo(N))


# In[4]:


arriba(134468), abajo(66420), es_bouncy(155349)


# In[5]:


def contar_bouncies(RATIO_LIMITE):
    contador = 0
    ratio = 0
    i = 100
    while (ratio != RATIO_LIMITE):
        if es_bouncy(i):
            contador += 1
            ratio = contador / i
        i += 1
    return [contador, i - 1, ratio]


# In[6]:


contar_bouncies(0.5)  # [269, 538, 0.5]


# In[7]:


contar_bouncies(0.9)  # [19602, 21780, 0.9]


# In[8]:


contar_bouncies(0.99)  # [1571130, 1587000, 0.99]
