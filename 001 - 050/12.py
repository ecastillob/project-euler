#!/usr/bin/env python
# coding: utf-8

# In[5]:


def get_divisores(N):
    divisores = []
    for i in range(1,N+1):
        if N%i==0:
            divisores.append(i)
    return divisores


# In[6]:


get_divisores(28)


# In[12]:


N = 7
suma = int(N*(N+1)/2)
suma


# In[18]:


def get_cantidad_divisores(N):
    divisores = 0
    for i in range(1,N+1):
        if N%i==0:
            divisores += 1
    return divisores


# In[19]:


get_cantidad_divisores(28)


# In[16]:


N = 0
while True:
    N += 1
    suma = int(N*(N+1)/2)
    divisores = get_divisores(suma)
    print (suma, divisores)
    if len(divisores) > 5:
        break
suma


# In[21]:


N = 0
while True:
    N += 1
    suma = int(N*(N+1)/2)
    if get_cantidad_divisores(suma) > 500:
        break
suma


"""
#include <stdio.h>
#include <time.h>


int get_cantidad_divisores(int N){
    int divisores = 0;
    int i;
    for (i=1; i<N+1; i++){
        if (N%i==0)
            divisores++;
    }
    return divisores;
}

int main(){

    time_t start,end;
    double dif;
    time (&start);

    int N = 0;
    // 5    : 28, 0 seg.
    // 300  : 2162160, 7 seg.
    // 350  : 17907120, 175 seg.
    
    int suma = 0;
    while (1){
        N++;
        suma = (N*(N+1))/2;
        if (get_cantidad_divisores(suma) > 5)
            break;
    }
    printf("\n %d", suma);
    
    time (&end);
    dif = difftime (end,start);
    printf ("\nYour calculations took %.2lf seconds to run.\n", dif );
}
"""


"""
#include <stdio.h>
#include <time.h>


int get_cantidad_divisores(int N){
    int divisores = 0;
    int i;
    int extremo = (N/2) + 1;
    if (N%2 == 0){
        for (i=1; i<=extremo; i++){
            if (N%i==0){
                divisores++;
            }
        }
    }
    else{
        for (i=1; i<=extremo; i+=2){
            if (N%i==0){
                divisores++;
            }
        }
    }
    return divisores;
}

int main(){

    time_t start,end;
    double dif;
    /*
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    printf("now: %d-%d-%d %d:%d:%d\n", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);
    */
    time_t t;
    //struct tm;
    time (&start);

    // divisores    :   tiempo
    // 5    : 28, 0 seg.
    /*
        N = 7
        suma = 28
    */
    // 200  :
    /*
        LIMITE = 200
        N = 2015
        suma = 2031120
        Your calculations took 4.00 seconds to run.
    */

    /*
        LIMITE = 250
        N = 2079
        suma = 2162160
        Your calculations took 5.00 seconds to run.
    */

    /*  N = 5984
        suma = 17907120
        Your calculations took 175.00 seconds to run.

        LIMITE = 350
        N = 5984
        suma = 17907120
        Your calculations took 100.00 seconds to run.
    */

    /*
        LIMITE = 400
        N = 5984
        suma = 17907120
        Your calculations took 99.00 seconds to run.
    */

    /*
        LIMITE = 500
        N = 12375
        divisores = 576
        suma = 76576500  // este numero es la respuesta
        Your calculations took 553.00 seconds to run.
    */

    int N = 0;
    int suma = 0;
    int divisores = 0;
    const int LIMITE = 500;
    while (divisores <= LIMITE){
        N++;
        suma = (N*(N+1))/2;
        divisores = get_cantidad_divisores(suma);
        if (N % 1000 == 0){
            t = time(NULL);
            struct tm tm = *localtime(&t);
            printf("\n %d-%d-%d %d:%d:%d", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);
            printf("\n N = %d", N);
            printf("\n divisores = %d", divisores);
            printf("\n suma = %d", suma);
            printf("\n");
        }
    }
    printf("\n LIMITE = %d", LIMITE);
    printf("\n N = %d", N);
    printf("\n divisores = %d", divisores);
    printf("\n suma = %d", suma);
    printf("\n");

    time (&end);
    dif = difftime (end,start);
    printf ("\nYour calculations took %.2lf seconds to run.\n", dif );
}
"""