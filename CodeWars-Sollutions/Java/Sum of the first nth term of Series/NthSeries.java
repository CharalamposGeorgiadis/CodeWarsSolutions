import java.util.Scanner;

public class NthSeries {

    public static String seriesSum(int n) {
        double div=1.00;
        double result=0.00;
        for (int i=0; i<n; i++){
            result+=1/div;
            div+=3.00;
        }
        result=Math.round(result*100.0)/100.0;
        String temp=String.valueOf(result);
        if (temp.length()==3){
            temp=temp+("0");
        }
        return temp;
    }


    public static void main(String[] args){
        Scanner console = new Scanner(System.in);
        System.out.print("Enter a Natural Number ");
        int aNumber = console.nextInt();
        NthSeries series;
        series= new NthSeries();
        System.out.println(series.seriesSum(aNumber));

    }
}