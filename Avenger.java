//create a class avenger with
//properties (name,age,power,weapon,planet) and with
//functions-getDetails() and displayDetails().
//create 5 objects as an array in the main method and call.


import java.util.*;
class main
{
 public static void main(String args[])

  
{
    Avenger []avenger = new Avenger[5];
  for(int i=0;i<5;i++)
  {
   avenger[i] = new Avenger();
   avenger[i].getDetails() ;
  }
 for(int i=0;i<5;i++)
 {
  avenger[i].displayDetails();
 }
}
}

class Avenger
{
Scanner sc = new Scanner(System.in);
int age;
String name,power,weapon,plannet;
public void getDetails()
{
 int age;
 
 System.out.println("Enter the name of the avenger:");
 String name = sc.next();
 System.out.println("Enter the age of avenger:");
 age = sc.nextInt();
 System.out.println("Enter the power,weapon and plannet:");
 String weapon= sc.next();
 String power = sc.next();
 String plannet = sc.next();
}
 
public void displayDetails()
{
 
 System.out.println("The avenger's name:"+ name+"age:"+age+"power:"+ power+"plannet:"+ plannet+"weapon"+ weapon);
}
}

 
 