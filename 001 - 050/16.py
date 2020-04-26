# $2^{15}$ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number $2^{1000}$?

# In[6]:


base = 2
exponente = 15
total = 1
for i in range(1, exponente+1):
    total *= base
total


# In[7]:


suma = 0
for i in str(total):
    suma += int(i)
suma


# In[8]:


base = 2
exponente = 1000
total = 1
for i in range(1, exponente+1):
    total *= base
total


# In[9]:


suma = 0
for i in str(total):
    suma += int(i)
suma  # 1366
