import java.util.Scanner;

public class BitCounting {
    
    public int countBits(int n){
        int counter=0;
        while(n!=0) {
            if (n % 2 == 0) {
                n = n / 2;
            }
            else {
                n = n / 2;
                counter++;
            }
        }
        return counter;
    }

    public static void main(String[] args) {

        Scanner console = new Scanner(System.in);
        System.out.print("Enter an Integer ");
        int aNumber = console.nextInt();
        BitCounting binary;
        binary= new BitCounting();
        int counter=binary.countBits(aNumber);
        System.out.println(counter);
    }
}

