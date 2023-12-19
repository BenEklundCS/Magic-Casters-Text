package com.beneklund.jcasters;

public class IO {
    final int LINE_LENGTH = 100;
    public void mainMenu() {
        System.out.println("Welcome to Magic Casters!");
        System.out.println("An object-oriented text rpg by Benjamin Eklund");
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
        int n = 0; // counter for printing text
        for (char c : s.toCharArray()) {
            if (c == ' ' && n >= LINE_LENGTH) { // if c is a space
                System.out.println(c); // print with newline
                n = 0; // reset the counter
            }
            else {
                System.out.print(c); // print the char
                n++; // increment the counter
            }
        }
    }
}
