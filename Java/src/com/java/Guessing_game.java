package com.java;

import java.util.Scanner;

public class Guessing_game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int usernumber;
        //Mini Project
        int mynumber= (int)(Math.random()*100);
        do{
            System.out.print("Guess my number(1-100):");
            usernumber = sc.nextInt();
            if(usernumber == mynumber){
                System.out.println("WOW.. Correct Number!!");
                break;
            }
            else if(usernumber > mynumber){
                System.out.println("Your number is large");
            }
            else{
                System.out.println("Your Number is small");
            }
        }while(usernumber>=0);
    }
}
