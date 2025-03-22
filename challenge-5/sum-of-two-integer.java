import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        while (b != 0){
            int t = (a&b)<<1;
            a = a^b;
            b = t
        }
        System.out.println(b);
    }
}