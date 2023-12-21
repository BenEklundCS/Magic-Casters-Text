package com.beneklund.jcasters;

import java.util.ArrayList;
import java.util.Arrays;

public class JCasters {
    private Player player;
    private IO io;

    // Constructor initializes the game
    public JCasters() {
        this.player = new Player("Name", 1, 1, 1, 1, 1, 1, 1);
        this.io = IO.getInstance();
    }

    public static void main(String[] args) {
        JCasters game = new JCasters(); // create a game instance / init
        game.io.clearTerminal();
        game.io.mainMenu();
        /*
        ArrayList<String> list = new ArrayList(Arrays.asList("N", "S", "E", "W"));
        Action a = new Action(list,  "Please enter a direction: ");
        String s = a.getPlayerChoice();
        System.out.println(s);
        */
    }
}
