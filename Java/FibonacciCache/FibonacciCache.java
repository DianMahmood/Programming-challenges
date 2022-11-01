import java.util.Arrays;

public class FibonacciCache{

    public static void main(String[] args){
        store();
        System.out.println("Fibonacci Numbers[First"+fib.length+"]: "+ Arrays.toString(fib));
        reset();
        System.out.println("List has been resetted: "+ Arrays.toString(fib));
        System.out.println(get(5));
    }
    public static long[] fib = new long[20];

    public static void store(){
        int num1 = 1, num2 = 0;
        for (int i = 0; i < fib.length; i++){
            int fibnumer = num1 + num2;
            num1 = num2;
            num2 = fibnumer;
            fib[i] = fibnumer;
        }
    }
    public static void reset(){
        for (int a = 0; a < fib.length; a++){
            fib[a] = 0;
        }
    }
    public static long get(int a){
        if (a>0 && a< fib.length){
            store();
        }
        return fib[a];
    }
}