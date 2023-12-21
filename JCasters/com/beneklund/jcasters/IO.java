package com.beneklund.jcasters;

import java.util.Scanner;

// This should be updated to a singleton pattern since I only need one IO stream at a time to the terminal

public class IO {

    final private int LINE_LENGTH = 100;
    final private Scanner scanner = new Scanner(System.in);
    private static IO instance = null;


    public static synchronized IO getInstance()
    {
        if (instance == null)
            instance = new IO();
 
        return instance;
    }

    public void mainMenu() {
        System.out.println("\nWelcome to Magic Casters!");
        System.out.println("An object-oriented text rpg by Benjamin Eklund");
        printInputArrow();
        getText();
    }

    public void lineBreak() {
        System.out.println();
        for (int i = 0; i < LINE_LENGTH; i++) {
            System.out.print('#');
        }
        System.out.println();
        System.out.println();
    }

    // println function for "loosely contained" text.
    // Enters a newline when the current char is a space and the strlen exceeds LINE_LENGTH
    public void printText(String s) {
        // Counter
        int n = 0;
        for (char c : s.toCharArray()) {
            // Print c with a newline if c is a space and n exceeds LINE_LENGTH - then reset n
            if (c == ' ' && n >= LINE_LENGTH) { 
                System.out.println(c); 
                n = 0; 
            }
            // Otherwise, print c and increment n
            else {
                System.out.print(c); 
                n++; 
            }
        }
    }

    public String getText() {
        String s = scanner.nextLine();
        return s;
    }

    public void printInputArrow() {
        System.out.print("> ");
    }

    public void clearTerminal() {
        System.out.print("\033\143");
    }
}
