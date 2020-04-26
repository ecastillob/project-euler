"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def es_primo(numero):
    if (numero <= 1):
        return 0
    if (numero % 2 == 0):
        if (numero == 2):
            return 1
        else:
            return 0
    i, es_numero_primo = None, 1
    extremo_derecho = int(numero / 2) + 1
    for i in range(3, extremo_derecho+1, 2):
        if (numero%i == 0):
            es_numero_primo -= 1
            break
    return es_numero_primo



#N = 10
N = 2000000
for i in range(1, N+1, 2):
    if es_primo(i):
        suma += i
suma  # 142913828922
# Advertencia: 
# - tomó 233 segundos en C sin arreglos (casi 4 minutos).
# - tomó 148 segundos en C con arreglos (casi 2 minutos y medio), en Python toma 1946 segundos con numpy


"""
    #include <stdio.h>
    #include <time.h>


    int es_primo(int numero, int inicio){
        if (numero <= 1)
            return 0;
        if (numero % 2 == 0){
            if (numero == 2)
                return 1;
            else
                return 0;
        }
        int i, es_numero_primo = 1;
        int extremo_derecho = numero / 2 + 1;
        if (inicio <= 0){
            inicio = 3;
        }
        for (i=inicio; i<=extremo_derecho; i+=2){
            if (numero%i == 0){
                es_numero_primo -= 1;
                break;
            }
        }
        return es_numero_primo;
    }

    int main()
    {
        time_t start,end;
        double dif;
        time (&start);
        
        int primos[100000];
        
        //long double suma = 0.0;
        double suma = 2.0;
        unsigned long N = 2000000;//350000;
        //int N = 2000000;
        unsigned long i;
        
        for (i=3; i<=N; i+=2){
            if (es_primo(i, -1) == 1)
                suma = suma + i;
        }
            
        printf("%lf\n", suma);
        
        time (&end);
        dif = difftime (end,start);
        printf ("Your calculations took %.2lf seconds to run.\n", dif );

        return 0;
    }
"""


"""
    #include <stdio.h>
    #include <time.h>


    int main()
    {
        time_t start,end;
        double dif;
        time (&start);
        
        // 142913828922
        
        //long double suma = 0.0;
        double suma = 2.0;
        int N = 2000000;//300000;
        //int N = 2000000;
        int i;
        int valor, in, aux;
        
        int tamano = (N/4)+5;
        //printf("\n tamano = %d", tamano);
        int primos[tamano], k;
        primos[0] = 2;
        int contador=1;
        
        for (i=3; i<=N; i+=2){
            
            aux = 1;
            for (k=0; k<contador; k++){
                if (i % primos[k] == 0){
                    aux = 0;
                    break;
                }
            }
            
            if (aux == 1){
                suma = suma + i;
                primos[contador] = i;
                contador++;
            }
        }
        
        //for (i=0; i<contador; i++){
            //printf ("%d ", primos[i] );
        //}
            
        printf("\n");
        printf("\n %lf", suma);
        printf("\n %d", contador);
        printf("\n");
        
        time (&end);
        dif = difftime (end,start);
        printf ("Your calculations took %.2lf seconds to run.\n", dif );

        return 0;
    }
"""