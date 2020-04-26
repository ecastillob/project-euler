public class Main {
    
    public static int calcular_factorial(int N){
        int factorial = 1, i;
        for (i=1; i<N+1; i++){ //for i in range(1, N+1)
            factorial *= i;
        }
        return factorial;
    }
    
    public static boolean es_un_numero_curioso(int N){
        String N_str = N+"";
        String valor_str;
        int suma = 0;
        int i, largo = N_str.length();
        for (i = 0; i<largo; i++){
            //    suma += factoriales[int(valor_str)]
            suma += factoriales[Integer.parseInt(N_str.charAt(i)+"")];
        }
        return N == suma;
    }
    
    static int factoriales[] = new int[10];
    
    public static void main(String args[]) {
        long startTime = System.nanoTime();    

        int i;
        for (i = 0; i<10; i++){
            factoriales[i] = calcular_factorial(i);
            //System.out.println(factoriales[i]);
        }

        int factorial = calcular_factorial(5);
        boolean es = es_un_numero_curioso(145);
        //System.out.println(factorial + " " + es);
        
        int N = 100000000;
        int suma = 0;
        System.out.println("N = " + N);
        for (i=3; i<N; i++){
            if (es_un_numero_curioso(i)){
                //System.out.println(i);
                suma += i;
            }
        } 
        System.out.println(suma);
        long estimatedTime = (System.nanoTime() - startTime) / (1000000000L);
        System.out.println("Tiempo: " + estimatedTime + " segundo(s).");
        
    }
}
/*
N = 100000000                                                                                                                                  
40730                                                                                                                                          
Tiempo: 34 segundo(s).
*/
/*
N = 2000000000
40730
Tiempo: 407 segundo(s).
*/