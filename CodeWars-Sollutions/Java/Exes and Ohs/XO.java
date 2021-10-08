import java.util.Scanner;

public class XO {

    public static boolean getXO (String str) {
        int x=0;
        int o=0;
        for (int i = 0; i < str.length(); i++){
            if(str.charAt(i)=='x'||str.charAt(i)=='X'){
                x++;
            }
            else if(str.charAt(i)=='o'||str.charAt(i)=='O'){
                o++;
            }
        }
        if(x==o)
           return true;
        else
            return false;
    }

    public static void main(String[] args) {

        Scanner console = new Scanner(System.in);
        System.out.print("Enter a String ");
        String aString = console.nextLine();
        XO xo;
        xo= new XO();
        boolean flag=xo.getXO(aString);
        System.out.println(flag);
    }
}
