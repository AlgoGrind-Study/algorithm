import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        boolean flag = false;
        for (int i = 1; i <= 1000000; i++) {
            int sum = i;
            String s = String.valueOf(i);
            for (int j = 0; j < s.length(); j++) {
                sum += s.charAt(j) - '0';
            }
            if (sum == num) {
                System.out.println(i);
                flag = true;
                break;
            }
        }

        if (flag == false)
        {
            System.out.println(0);
        }
    }
}
