# coding: utf-8

# In[1]:


def factorial(N):
    total = 1
    for i in range(1, N+1):
        total *= i
    return total


def combinatoria(M, N):
    return factorial(M) / (factorial(N)*factorial(M-N))


# In[2]:


factorial(4)


# In[3]:


combinatoria(4, 2)


# In[4]:


N = 9
for m in range(0, N):
    for n in range(0, m+1):
        valor = int(combinatoria(m, n))
        #valor = "{}-{}".format(m, n)
        print(valor, end=' ')
    print()


# In[5]:


numero = 20
N = numero*2 + 1
b = 0
for m in range(0, N):
    a = 0
    for n in range(0, m+1):
        valor = int(combinatoria(m, n))
        #valor = "{}-{}".format(m, n)
        print(valor, end=' ')
        if (a == int(m/2)):
            b = valor
        a+= 1
    print()
b  # 137846528820
