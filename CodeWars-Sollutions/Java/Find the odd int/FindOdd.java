

public class FindOdd {

    public static int findIt(int[] a) {
        int odd = a[0];
        for (int i = 1; i < a.length; i++) {
            int count = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[i] == a[j]) {
                    count++;
                }
            }
            if(count%2==1){
                odd=a[i];
                return odd;
            }
        }
        return odd;
    }


    public static void main(String[] args) {
        int[] table={1,1,2,4,4};
        FindOdd oddNumber;
        oddNumber= new FindOdd();
        int o=oddNumber.findIt(table);
        System.out.println(o);

        }

    }


