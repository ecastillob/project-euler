# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# <small> <br>
# NOTE: Do not count spaces or hyphens. For example:
# * 342 (three hundred and forty-two) contains 23 letters and 
# * 115 (one hundred and fifteen) contains 20 letters.
# 
# The use of "and" when writing out numbers is in compliance with British usage.
# </small>

# In[1]:


digitos = {
    #0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
diez = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
decenas = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}
centena = 'hundred'
sep = ''
mil = 'one' + sep + 'thousand'


# In[2]:


216%10


# In[3]:


def bajo_centena(i):
    palabra = ''
    if 1 <= i <= 9:
        palabra = digitos[i]
        #print(palabra)
    elif 10 <= i <= 19:
        palabra = diez[i]
        #print(palabra)
    elif 20 <= i <= 99:
        index = int(i/10)
        primero = decenas[index]
        palabra = primero
        index = i%10
        if index > 0:
            segundo = digitos[index]
            palabra += sep + segundo
        #print(palabra)
    return palabra


# In[4]:


total = 0
#for i in range(1, 5+1):
#for i in range(50, 1000+1, 25):
for i in range(1, 1000+1):
    if 1 <= i <= 99:
        palabra = bajo_centena(i)
        print(palabra)
    elif 100 <= i <= 999:
        index = int(i/100)
        primero = digitos[index] + sep + centena
        palabra = primero
        index = i%100
        if index > 0:
            segundo = bajo_centena(index)
            palabra += sep + 'and' + sep + segundo
        print(palabra)
    else:
        palabra = mil
        print(palabra)
    total += len(palabra)
total  # 21124
