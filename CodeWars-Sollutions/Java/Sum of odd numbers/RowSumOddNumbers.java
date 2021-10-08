import java.util.Scanner;

public class RowSumOddNumbers {

    public static int rowSumOddNumbers(int n) {
        int sum= n*(n-1)+1;
        int temp=sum;
        for (int i=1; i<n; i++){
            temp+=2;
            sum+=temp;
        }
        return sum;

    }

    public static void main(String[] args){
        Scanner console = new Scanner(System.in);
        System.out.print("Enter the row number ");
        int row = console.nextInt();
        RowSumOddNumbers s;
        s= new RowSumOddNumbers();
        int sum=s.rowSumOddNumbers(row);
        System.out.println(sum);

    }
}
