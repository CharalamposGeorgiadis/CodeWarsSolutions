import java.util.Scanner;

public class Kata {



    public static String createPhoneNumber(int[] numbers) {
        String p="(";
         for (int i=0; i<10; i++) {
             if (i == 3)
                 p = p + ") ";
             if (i == 6)
                 p = p + "-";
             p = p + numbers[i];
         }
         return p;
    }


    public static void main(String[] args){
        Kata phone;
        phone=new Kata();
        int[] number;
        number = new int[10];
        Scanner console = new Scanner(System.in);
        for (int i=0; i<10; i++){
            System.out.println("Give a number of the phone");
            number[i]=console.nextInt();
        }
        String phoneNumber=phone.createPhoneNumber(number);
        System.out.println(phoneNumber);

}



}
