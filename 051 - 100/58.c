#include<stdio.h>
#include <stdlib.h>
#include <time.h>


long currentTimeMillis() {
    struct timeval time;
    gettimeofday(&time, NULL);
    
    return time.tv_sec * 1000 + time.tv_usec / 1000;
}


int cy_es_primo_simplificado_2(int n){
    unsigned int i, N, es;
    N = n;
    if (N%2 == 0)
        return 0;
    es = 1;
    for (i=3; i<N; i+=2){
        if (N%i == 0){
            es = 0;
            break;
        }
    }
    return es;
}


int cy_funcion_3(int n){
    unsigned int inicio, N, n_primos, i, up, n_en_diagonales, k, suma;
    float porcentaje;
    inicio = 1;
    porcentaje = 100;
    N = n;
    n_primos = 0;
    unsigned int valores[] = {0, 0, 0, 0};
    for (i=3; i<N+1; i+=2){
        up = i-1;
        valores[0] = inicio+up*1;
        valores[1] = inicio+up*2;
        valores[2] = inicio+up*3;
        valores[3] = inicio+up*4;
        
        suma = 0;
        for (k=0; k<4; k++){
            suma += cy_es_primo_simplificado_2(valores[k]);
        }
        n_primos += suma;
        
        n_en_diagonales = (i*2 - 1);
        porcentaje = 1.0 * n_primos / n_en_diagonales;
        if ((i-1) % 1000 == 0)
            printf("%d \t %f \n", i, porcentaje);
        if (porcentaje < 0.1){
            printf("%d %d %f %d \n", n_primos, n_en_diagonales, porcentaje, i);
            break;
        }
        inicio = i*i;
    }
    return i;
}


int main() {
    long time1 = currentTimeMillis();
    //
    int total = cy_funcion_3(10000);
    printf("\ni: %d", total);
    //
    long time2 = currentTimeMillis();
    long elapsedMS = time2 - time1;
    printf("\ntiempo total: %ld", elapsedMS);  // tiempo total: 109741 (109.741 segundos)
}
