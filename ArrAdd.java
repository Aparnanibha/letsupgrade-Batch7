import java.util.*;
class ArrAdd
{
public static void main (String args[])
{
int n,i,s=0;
Scanner sc = new Scanner(System.in);
System.out.print("Enter the size of an array:");
    n = sc.nextInt();
int []a = new int[n];
System.out.print("enter the element of an array :");
for(i=0;i<n;i++)
{
  a[i] = sc.nextInt();
}
System.out.println("Array element are :");
for(i=0;i<n;i++)
{
System.out.println(a[i]+"\t");
}
for(i=0;i<n;i++)
  s=s+a[i];
System.out.println("Addition of an array"+s);
}
}