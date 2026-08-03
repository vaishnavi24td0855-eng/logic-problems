import java.util.Scanner;

public class PowerNumber {
    public static boolean isPowerNumber(int n) {
        if (n <= 1) {
            return false;
        }

        for (int base = 2; base <= Math.sqrt(n); base++) {
            long power = base;

            while (power < n) {
                power *= base;
            }

            if (power == n) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        if (isPowerNumber(n)) {
            System.out.println(n + " is a power number.");
        } else {
            System.out.println(n + " is not a power number.");
        }

        sc.close();
    }
}