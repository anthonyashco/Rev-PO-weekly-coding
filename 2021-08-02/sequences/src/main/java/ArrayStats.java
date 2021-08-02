import java.util.ArrayList;
import java.util.Collections;

public class ArrayStats {
    /**
     * Returns an ArrayList of Integers missing from a provided sequence.
     *
     * @param sample an ArrayList of input Integers
     * @return an ArrayList of Integers missing from sample
     */
    public static ArrayList<Integer> missingValueFinder(ArrayList<Integer> sample) {
        Integer smallest = Collections.min(sample);
        Integer largest = Collections.max(sample);
        ArrayList<Integer> missing = new ArrayList<Integer>();

        for (int i = smallest; i <= largest; i++) {
            if (!sample.contains(i)) {
                missing.add(i);
            }
        }

        return missing;
    }

    /**
     * A helper method to convert an int Array to an Integer ArrayList.
     *
     * @param arr an int Array
     * @return an Integer ArrayList
     */
    public static ArrayList<Integer> arrayToArrayList(int[] arr) {
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        for (int i : arr) {
            arrayList.add(i);
        }
        return arrayList;
    }

    /**
     * Prints out the min, max, and any missing sequential values from an input int Array.
     *
     * @param sample an int Array
     */
    public static void statsPrinter(ArrayList<Integer> sample) {
        System.out.println("Min: " + Collections.min(sample));
        System.out.println("Max: " + Collections.max(sample));
        System.out.println("Missing: " + missingValueFinder(sample));
    }

    public static void main(String[] args) {
        int[] arr1 = {7, 5, 6, 1, 4, 2};
        int[] arr2 = {5, 3, 1, 2};

        statsPrinter(arrayToArrayList(arr1));
        statsPrinter(arrayToArrayList(arr2));
    }
}
