import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean []arr = new boolean[30];
        for(int i =0; i<28; i++) {
            arr[sc.nextInt()-1] = true;
        }

        int cnt =0;
        for(int i =0; i<30; i++) {
            if(arr[i] == false) {
                System.out.println(i+1);
                cnt++;
            }
            if( cnt == 2) {
                break;
            }
        }
    }
}
