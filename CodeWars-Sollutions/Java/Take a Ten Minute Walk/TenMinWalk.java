import java.util.Scanner;

public class TenMinWalk {

    public static boolean isValid(char[] walk) {
        int[] flag = {0, 0, 0, 0};
        if (walk.length == 10) {
            for (char c : walk) {
                if (c == 'n')
                    flag[0]++;
                else if (c == 's')
                    flag[1]++;
                else if (c == 'w')
                    flag[2]++;
                else
                    flag[3]++;
            }
            if (flag[0] == flag[1] && flag[2] == flag[3])
                return true;
        }
        return false;
    }

    public static void main(String[] args){
        Scanner console = new Scanner(System.in);
        char[] directions=console.next().toCharArray();
        TenMinWalk dir=new TenMinWalk();
        if (dir.isValid(directions))
            System.out.println("The directions were correct");
        else
            System.out.println("The directions were incorrect");

    }
}