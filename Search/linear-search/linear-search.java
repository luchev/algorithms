import java.io.*;
import java.util.*;

class LinearSearch {
    long linearSearch(int[] haystack, int needle) {
        for (var i = 0; i < haystack.length; i++) {
            if (haystack[i] == needle) {
                return i;
            }
        }
        return -1;
    }

    void test() {
        try {
            var br = new BufferedReader(new InputStreamReader(System.in));
            var line1 = new StringTokenizer(br.readLine());
            int numberCount = Integer.parseInt(line1.nextToken());
            int targetCount = Integer.parseInt(line1.nextToken());

            var numbers = new int[numberCount];
            var line2 = new StringTokenizer(br.readLine());
            for (var i = 0; i < numberCount; i++) {
                int input = Integer.parseInt(line2.nextToken());
                numbers[i] = input;
            }

            var line3 = new StringTokenizer(br.readLine());
            for (var i = 0; i < targetCount; i++) {
                int target = Integer.parseInt(line3.nextToken());
                System.out.print(linearSearch(numbers, target));
                System.out.print(" ");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        LinearSearch solver = new LinearSearch();
        solver.test();
    }
}
