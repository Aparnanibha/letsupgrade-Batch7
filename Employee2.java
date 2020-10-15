// To check the grade of the student

import java.util.*;
import java.lang.*;
import java.io.*;
class Employee2
{
 public static void main(String args[])
 {
  int s1,s2,s3,s4,s5;
  float p; 
  Scanner sc = new Scanner(System.in);
  System.out.println("Enter the marks of the 5 subject:");
  s1 = sc.nextInt();
  s2 = sc.nextInt();
  s3 = sc.nextInt();
  s4 = sc.nextInt();
  s5 = sc.nextInt();
  p = (float)(s1+s2+s3+s4+s5) / 500  * 100;
  checkForGrade(p);
  System.out.println("Percentage of the student is:"+p);
  }

public static void checkForGrade(float p)
 {
  if(p>=90)
   System.out.println("Grade:A");
  else if(p<90 && p>=80)
   System.out.println("Grade:B");
  else if(p<80 && p>=60)
   System.out.println("Grade:C");
  else
   System.out.println("Grade:D");    
 }
}