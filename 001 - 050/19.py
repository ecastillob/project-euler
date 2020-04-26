"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# In[3]:


dias_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


# In[4]:


def es_bisiesto(anho):
    es = False
    if anho % 4 == 0:
        es = True
        if anho % 100 == 0:
            if anho % 400 == 0:
                es = True
            else:
                es = False
    return es


# In[7]:


contador_dias = 0
dias_anho = 1
for anho in range(1900, 2000+1):
    for mes in range(1, 12+1):
        for day_of_month in range(1, dias_mes[mes]+1):
            if day_of_month == 1 and anho >= 1901:
                if dias_anho % 7 == 0:
                    print(anho, "\t", mes, "\t", day_of_month)
                    contador_dias += 1
            dias_anho += 1
        if mes == 2 and es_bisiesto(anho):
            dias_anho += 1
contador_dias  # 171
