import java.util.Scanner;

public class bubbleSort {

    public static void main (String args[]) {
        int j, i, a[],number;
        Scanner sc=new Scanner(System.in);
	    System.out.print("How many numbers do you plan to input: ");
        number = sc.nextInt();
        a = new int[number];
        for (i=0;i<number;i++) {
	    System.out.print("Enter number: ");
            a[i] = sc.nextInt();
        }
    	for (i=0;i<number;i++) {
    	    System.out.print("Element "+(i+1)+" is "+a[i]+"\n");
    	}
        for (i=0;i<number;i++) {
            for (j=0;j<number-1-i;j++) {
                if (a[j]>a[j+1]) {
                    a[j] = a[j]+a[j+1];
                    a[j+1] = a[j]-a[j+1];
                    a[j] = a[j]-a[j+1];
                }
            }
        }
        System.out.print("Sorted!\n");
        for (i=0;i<number;i++) {
            System.out.print("Element "+(i+1)+" is "+a[i]+"\n");
        }
    }
}
