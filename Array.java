//Create an int array with 5 values and print only odd values.

import java.util.*;
import java.io.*;
class Array
{
 public static void main(String args[])
 {
   int n,i;
   Scanner sc = new Scanner(System.in);
   System.out.print("Enter the size of an array:");
   n = sc.nextInt();
   int []a=new int[n];
   System.out.println("Enter the element of an array:");
   for(i=0;i<n;i++)
    {
     a[i] = sc.nextInt();
    }
    System.out.println("Odd element of an array are:");
     for(i=0;i<n;i++)
     {
      if(a[i] % 2!=0)
        System.out.println("Odd Element"+a[i]);
      }
  }
}