import java.util.Arrays;
import java.util.Scanner;

public class StringSplit {

    public static String[] solution(String s) {
        char[] temp=s.toCharArray();
        String[] sol;
                if(s.length()%2==0)
                    sol=new String[s.length()/2];
                else
                    sol=new String[s.length()/2+1];
        int j=0;
        for (int i=0; i<s.length(); i=i+2) {
            if (i + 1 != s.length()) {
                sol[j] = String.valueOf(temp[i]) + String.valueOf(temp[i + 1]);
            } else {
                sol[j] = String.valueOf(temp[i]) + "_";
            }
            j++;
        }
        return sol;
    }

    public static void main(String[] args) {

        Scanner console = new Scanner(System.in);
        System.out.print("Enter a String \n");
        String aString = console.nextLine();
        StringSplit string;
        string= new StringSplit();
        String[] split=string.solution(aString);
        System.out.println(Arrays.toString(split));
    }
}
